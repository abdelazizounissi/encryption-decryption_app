from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# --- CIPHER FUNCTIONS ---
def mono_encryption(text):
    p = "abcdefghijklmnopqrstuvwxyz"
    e = "wxehyztkcpjiuadglqmnrsfvbo"
    result = ""
    for ch in text.lower():
        found = False
        for j in range(len(p)):
            if p[j] == i:
                res += e[j]
                found = True
                break
        if not found:
            res += i
    return res

def mono_decryption(text):
    p = "abcdefghijklmnopqrstuvwxyz"
    e = "wxehyztkcpjiuadglqmnrsfvbo"
    result = ""
    for ch in text.lower():
        found = False
        for j in range(len(p)):
            if e[j] == i:
                res += p[j]
                found = True
                break
        if not found:
            res += i
    return res

def caesar_encryption(text, k):
    res = ""
    for ch in text:
        if ch.isalpha():
            base = ord('a') if ch.islower() else ord('A')
            res += chr((ord(ch) - base + k) % 26 + base)
        else:
            res += ch
    return res

def caesar_decryption(text, k):
    return caesar_encryption(text, -k)

# --- ROUTES ---
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    cipher = data.get('cipher')
    action = data.get('action')
    text = data.get('text')
    key = int(data.get('key', 3))  # default Caesar key
    
    if cipher == "monoalphabetic":
        result = mono_encryption(text) if action == "encrypt" else mono_decryption(text)
    elif cipher == "caesar":
        result = caesar_encryption(text, key) if action == "encrypt" else caesar_decryption(text, key)
    else:
        result = "Invalid cipher"

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
