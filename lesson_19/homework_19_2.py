import requests
from pathlib import Path

SERVER_URL = 'http://127.0.0.1:8080'

def upload_image(image_path):
    with Path(image_path).open('rb') as image_file:
        files = {'image': (Path(image_path).name, image_file, 'image/jpeg')}
        response = requests.post(f'{SERVER_URL}/upload', files=files)
        return response.json().get('image_url')

def get_image_url(image_filename):
    headers = {'Content-Type': 'text'}
    response = requests.get(f'{SERVER_URL}/image/{image_filename}', headers=headers)
    return response.json().get('image_url')

def delete_image(image_filename):
    response = requests.delete(f'{SERVER_URL}/delete/{image_filename}')
    return response.status_code == 200


if __name__ == '__main__':

    script_dir = Path(__file__).resolve().parent
    image_to_upload = script_dir / 'test_image.jpg'

    uploaded_url = upload_image(image_to_upload)
    if uploaded_url:
        print(f"Зображення завантажено: {uploaded_url}")
        filename = image_to_upload.name
        retrieved_url = get_image_url(filename)
        print(f"URL зображення: {retrieved_url}")
        if delete_image(filename):
            print(f"Зображення {filename} видалено.")
        else:
            print(f"Не вдалося видалити зображення {filename}.")
    else:
        print("Не вдалося завантажити зображення.")
