import requests

def download_photo(img_url: str, file_name: str):
    try:
        response = requests.get(img_url)
        response.raise_for_status()
        with open(file_name, 'wb') as file:
            file.write(response.content)
        return True
    except requests.exceptions.RequestException as e:
        print(f"Не вдалося скачати фото {file_name}: {e}")
        return False

def get_api_params() -> dict:
    return {
        'sol': 1000,
        'camera': 'fhaz',
        'api_key': 'DEMO_KEY'
    }

def get_nasa_photos(url: str, params: dict, max_photos=2):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        try:
            data = response.json()
        except ValueError:
            print("Помилка: відповідь не у форматі JSON")
            return []
        
        saved_files = []
        for i, photo in enumerate(data.get('photos', [])[:max_photos], start=1):
            img_url = photo.get('img_src')
            if not img_url:
                continue
                
            file_name = f'mars_photo{i}.jpg'
            if download_photo(img_url, file_name):
                saved_files.append(file_name)

        return saved_files

    except requests.exceptions.RequestException as e:
        print(f"Помилка запиту: {e}")
        return []

if __name__ == "__main__":
    api_url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
    params = get_api_params()

    downloaded = get_nasa_photos(api_url, params)
    print("Скачані файли:", downloaded)