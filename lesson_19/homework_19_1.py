import requests


def get_photos(url: str, params: dict):
    response = requests.get(url, params=params)
    response.raise_for_status() 
    data = response.json()
    photos = data.get('photos', [])
    saved_files = []

    for idx, photo in enumerate(photos, start=1):
        img_url = photo['img_src']
        img_data = requests.get(img_url).content
        file_name = f'mars_photo{idx}.jpg'

        with open(file_name, 'wb') as file:
            file.write(img_data)

        saved_files.append(file_name)
    
    return saved_files


if __name__ == "__main__":
    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
    params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}
    
    print(get_photos(url, params))
