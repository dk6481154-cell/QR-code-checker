
from flask import Flask, render_template, request
import cv2
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/scan", methods=["POST"])
def scan():

    file = request.files.get("qr_image")

    if not file or file.filename == "":
        return "Please upload a QR code image"

    path = os.path.join(UPLOAD_FOLDER, "qr_image.png")
    file.save(path)

    image = cv2.imread(path)

    detector = cv2.QRCodeDetector()
    data, points, _ = detector.detectAndDecode(image)

    os.remove(path)

    if not data:
        return "QR Code not detected!"

    return f"QR Code Content: {data}"


if __name__ == "__main__":
    app.run(debug=True)
