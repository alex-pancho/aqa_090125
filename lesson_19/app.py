from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Завантаження зображення
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    
    return jsonify({"image_url": f"http://127.0.0.1:8080/uploads/{file.filename}"}), 201

# Отримання зображення
@app.route('/image/<filename>', methods=['GET'])
def get_image(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    if not os.path.exists(file_path):
        return jsonify({"error": "Image not found"}), 404
    
    if request.headers.get('Content-Type') == 'text':
        return jsonify({"image_url": f"http://127.0.0.1:8080/uploads/{filename}"}), 200
    
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Видалення зображення
@app.route('/delete/<filename>', methods=['DELETE'])
def delete_image(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    if not os.path.exists(file_path):
        return jsonify({"error": "Image not found"}), 404
    
    os.remove(file_path)
    
    return jsonify({"message": f"Image {filename} successfully deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=8080)
