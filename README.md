# Cipher Toolkit — Simple Encryption Web App

A small Flask web app that demonstrates text encryption and decryption using two classic educational ciphers:

- Monoalphabetic substitution cipher (preserves case)
- Caesar cipher (rotational shift, shift 1–25)

This project is intended for learning and demonstration purposes only.

<img width="1919" height="995" alt="Screenshot 2025-10-22 005052" src="https://github.com/user-attachments/assets/77bdcee7-9c49-453b-864a-56643dc6c833" />


## Features
- Encrypt and decrypt text with Monoalphabetic or Caesar ciphers
- Select cipher and action (Encrypt / Decrypt)
- Specify Caesar shift (1–25)
- Simple, local web interface — runs in your browser

## Requirements
- Python 3.8+
- pip

## Installation

Clone the repo:
```bash
git clone https://github.com/abdelazizounissi/encryption-decryption_app.git
cd encryption-decryption_app
```

Create and activate a virtual environment:

- macOS / Linux:
```bash
python -m venv venv
source venv/bin/activate
```

- Windows (PowerShell):
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the app
```bash
python app.py
```
Open your browser to: http://127.0.0.1:5000

## How to Use
1. Enter the input text.
2. Choose a cipher (Monoalphabetic or Caesar).
3. Choose action: Encrypt or Decrypt.
4. If Caesar, enter a shift value (1–25).
5. Click "Run Cipher" to see the result.

## Important security note
Monoalphabetic and Caesar ciphers are NOT secure for real-world use. They are classical ciphers used for teaching and demonstration only. For any real confidentiality needs, use well-maintained cryptographic libraries (for example, the `cryptography` package with AES-GCM or an asymmetric scheme backed by a key management system). Do not store or commit private keys or secrets in the repository.

## How it works (brief)
- Server: Flask receives the form POST and runs the chosen cipher implementation on the server side.
- Monoalphabetic: substitution mapping preserves letter case; non-letter characters are preserved.
- Caesar: each letter is shifted by the chosen amount; preserves case and non-letter characters.

## Development notes
- Add tests under `tests/` (pytest recommended).
- Consider adding input validation, CSRF protection (Flask-WTF), and escaping/sanitization of user input when rendering results to avoid XSS.
- Use POST for form submissions and add rate limiting for public deployments.

## Contributing
Contributions welcome! Please open an issue or a pull request. Add tests for any new functionality and follow the project linting.

## Screenshot
- The file `screenshot.png` is referenced above. If you include the screenshot file in the repo root, it will be shown here on GitHub.
- Optional: crop/remove any UI overlay (e.g., full-screen hints) before committing for a cleaner image.

## License
This project is open-source. Add a LICENSE file (e.g., MIT) to make the license explicit.
