import os
from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import cv2
import numpy as np

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = './media'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'mp4', 'wav'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the media directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Image Steganography (Example with LSB)
def lsb_steganography(image_path, data):
    img = cv2.imread(image_path)
    binary_data = ''.join(format(ord(i), '08b') for i in data)
    data_index = 0
    for row in img:
        for pixel in row:
            for i in range(3):  # For RGB channels
                if data_index < len(binary_data):
                    pixel[i] = int(bin(pixel[i])[2:-1] + binary_data[data_index], 2)
                    data_index += 1
    return img

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return jsonify({'message': 'File uploaded successfully', 'filepath': filepath}), 200
    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/process_image', methods=['POST'])
def process_image():
    data = request.form.get('data')
    filepath = request.form.get('filepath')

    if not data or not filepath:
        return jsonify({'error': 'Data or file path missing'}), 400

    if not os.path.exists(filepath):
        return jsonify({'error': 'File not found'}), 404

    output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'stego_' + os.path.basename(filepath))
    img_with_data = lsb_steganography(filepath, data)
    cv2.imwrite(output_path, img_with_data)
    return jsonify({'message': 'Image processed', 'output_path': output_path}), 200

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
