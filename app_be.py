
from doc_parsing import extract_and_upload
from flask import Flask, request, jsonify
import config

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Document Parsing API! Use the /upload endpoint to upload an image file."

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    result = extract_and_upload(file)
    return jsonify(({"response": result}))

if __name__ == '__main__':
    app.run(host=config.APP_HOST, port=config.APP_PORT)