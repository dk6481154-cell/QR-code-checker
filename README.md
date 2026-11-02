
# 🛡️ QR Shield - AI Powered QR Code Checker

QR Shield is an AI-powered QR Code Security Checker built using Python, Streamlit, OpenCV, and Groq API.

The application scans QR code images, extracts their content, checks basic URL security indicators, and uses Groq AI to provide a preliminary security assessment.

## 🚀 Features

- Upload QR code images.
- Decode QR codes automatically.
- Extract website URLs.
- Detect basic suspicious URL patterns.
- AI-powered security analysis using Groq API.
- Display security warnings.
- Provide safety recommendations.
- Modern Streamlit interface.

## 🛠️ Technologies Used

- Python
- Streamlit
- OpenCV
- NumPy
- Groq API
- Llama 3.3 70B Versatile

## 📁 Project Structure

```text
QR-Code-Checker/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd QR-Code-Checker
```

### 3. Create virtual environment

```bash
python -m venv .venv
```

### 4. Activate environment

Windows:

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Groq API Configuration

1. Visit https://console.groq.com/
2. Create your Groq account.
3. Generate an API key.
4. Never publish your API key on GitHub.

For local Streamlit development, create this folder:

```text
.streamlit/
```

Inside it create:

```text
secrets.toml
```

Add:

```toml
GROQ_API_KEY = "YOUR_GROQ_API_KEY"
```

Replace the example with your actual API key.

## ▶️ Run the Application

Execute:

```bash
streamlit run app.py
```

Your application will open in your browser.

## ☁️ GitHub Deployment

1. Create a GitHub repository.
2. Upload app.py, requirements.txt and README.md.
3. Connect your repository to Streamlit Community Cloud.
4. Add GROQ_API_KEY under the application's Secrets settings.
5. Deploy the application.

Do not upload secrets.toml or your actual API key to GitHub.

## 🔒 Security Limitations

- AI results are preliminary assessments, not proof.
- The application does not visit the destination URL.
- It does not currently use a live phishing database.
- A low-risk result does not guarantee a legitimate website.
- AI may make incorrect assessments.

## 👨‍💻 Project Purpose

This project is developed for educational purposes to demonstrate QR code processing, AI integration, and cybersecurity awareness.

## 📜 License

MIT License
