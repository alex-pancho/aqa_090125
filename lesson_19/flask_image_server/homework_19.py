import requests

SERVER_URL = "http://127.0.0.1:8080"
IMAGE_FILE = "example.jpg"

def main():
    try:
        with open(IMAGE_FILE, 'rb') as f:
            response = requests.post(f"{SERVER_URL}/upload", files={'image': f})
            image_url = response.json()['image_url']
            print("Фото завантажено на сервер. URL:", image_url)

        
        filename = image_url.split('/')[-1]
        headers = {'Content-Type': 'text'}
        response = requests.get(f"{SERVER_URL}/image/{filename}", headers=headers)
        
        if response.status_code == 200:
            print("Отриманий URL з сервера:", response.json()['image_url'])
        else:
            print("Помилка:", response.json())

        
        response = requests.delete(f"{SERVER_URL}/delete/{filename}")
        print("Результат видалення:", response.json()['message'])

    except Exception as e:
        print("Сталася помилка:", e)

if __name__ == "__main__":
    main()