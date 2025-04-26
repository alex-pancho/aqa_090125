import requests
import logging

# Налаштовуємо логер
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

BASE_URL = 'http://127.0.0.1:8080'
IMAGE_PATH = r"C:\Users\HP\Рабочий стол\aqa_090125\lesson_19\mars_photos\mars_photo1.jpg"
FILENAME = 'mars_photo1.jpg'

def upload_image(file_path):
    url = f'{BASE_URL}/upload'
    try:
        with open(file_path, 'rb') as file:
            files = {'image': file}
            response = requests.post(url, files=files)
        response.raise_for_status()
        logging.info(f"Uploaded: {response.json()['image_url']}")
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
    except requests.RequestException as e:
        logging.error(f"Upload error: {e}")

def get_image(filename):
    url = f'{BASE_URL}/image/{filename}'
    headers = {'Content-Type': 'text'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        logging.info(f"Image URL: {response.json()['image_url']}")
    except requests.RequestException as e:
        logging.error(f"Fetch error: {e}")

def delete_image(filename):
    url = f'{BASE_URL}/delete/{filename}'
    try:
        response = requests.delete(url)
        response.raise_for_status()
        logging.info(f"Deleted: {response.json()['message']}")
    except requests.RequestException as e:
        logging.error(f"Delete error: {e}")

if __name__ == "__main__":
    upload_image(IMAGE_PATH)
    get_image(FILENAME)
    delete_image(FILENAME)
