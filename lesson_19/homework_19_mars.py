import requests

def get_nasa_photos(url: str, params: dict, max_photos=2):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()    # Перевірка на HTTP помилки
        
        try:
            data = response.json()  # Спроба отримати JSON
        except ValueError:
            print("Помилка: відповідь не у форматі JSON")
            return []
        
        photos = data.get('photos', [])[:max_photos]
        saved_files = []

        for i, photo in enumerate(photos, start=1):
            img_url = photo.get('img_src')
            if not img_url:
                continue
                
            try:
                img_data = requests.get(img_url).content
                file_name = f'mars_photo{i}.jpg'
                
                with open(file_name, 'wb') as file:
                    file.write(img_data)
                
                saved_files.append(file_name)
            except requests.exceptions.RequestException as e:
                print(f"Не вдалося скачати фото {i}: {e}")

        return saved_files

    except requests.exceptions.RequestException as e:
        print(f"Помилка запиту: {e}")
        return []

if __name__ == "__main__":
    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos' 
    params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

    downloaded = get_nasa_photos(url, params)
    print("Скачані файли:", downloaded)