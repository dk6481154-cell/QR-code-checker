
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from pathlib import Path
from urllib.parse import urlparse
import cv2
import os
import uuid

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024

ALLOWED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".bmp"}


# Check allowed image formats
def allowed_file(filename):
    extension = Path(filename).suffix.lower()
    return extension in ALLOWED_EXTENSIONS


# Analyze QR code URL
def analyze_url(url):

    risk = 0
    reasons = []

    parsed = urlparse(url)
    domain = parsed.hostname or ""

    if parsed.scheme not in ["http", "https"] or not domain:
        return {
            "status": "Unknown",
            "risk": 0,
            "reasons": ["QR code does not contain a valid website URL."]
        }

    if parsed.scheme == "http":
        risk += 15
        reasons.append("Website does not use HTTPS.")

    if "@" in parsed.netloc:
        risk += 30
        reasons.append("URL contains a suspicious @ symbol.")

    if domain.startswith("xn--") or ".xn--" in domain:
        risk += 25
        reasons.append("Domain uses unusual encoded characters.")

    if len(domain) > 35:
        risk += 10
        reasons.append("Domain name is unusually long.")

    suspicious_words = [
        "login",
        "verify-account",
        "password",
        "free-gift",
        "claim-prize",
        "account-update"
    ]

    for word in suspicious_words:
        if word in url.lower():
            risk += 20
            reasons.append("Suspicious keyword found: " + word)

    risk = min(risk, 100)

    if risk >= 40:
        status = "Suspicious"
    else:
        status = "No obvious warning signs"

    if not reasons:
        reasons.append(
            "No obvious suspicious patterns found. "
            "This does not guarantee the website is safe."
        )

    return {
        "status": status,
        "risk": risk,
        "reasons": reasons
    }


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# QR Code Scanner
@app.route("/scan", methods=["POST"])
def scan():

    file = request.files.get("qr_image")

    if not file or file.filename == "":
        return render_template(
            "index.html",
            error="Please select a QR code image."
        )

    filename = secure_filename(file.filename)

    if not filename or not allowed_file(filename):
        return render_template(
            "index.html",
            error="Invalid image format."
        )

    image_path = os.path.join(
        UPLOAD_FOLDER,
        str(uuid.uuid4()) + Path(filename).suffix.lower()
    )

    try:

        file.save(image_path)

        image = cv2.imread(image_path)

        if image is None:
            return render_template(
                "index.html",
                error="Unable to read image."
            )

        detector = cv2.QRCodeDetector()

        data, points, _ = detector.detectAndDecode(image)

        if not data:
            return render_template(
                "index.html",
                error="No QR code found. Try another image."
            )

        analysis = analyze_url(data)

        return render_template(
            "result.html",
            data=data,
            result=analysis["status"],
            risk=analysis["risk"],
            reasons=analysis["reasons"]
        )

    finally:
        if os.path.exists(image_path):
            os.remove(image_path)


# File size error
@app.errorhandler(413)
def file_too_large(error):
    return render_template(
        "index.html",
        error="Image is too large. Maximum size is 5 MB."
    ), 413


# Run application
if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
