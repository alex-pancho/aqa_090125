import requests
from pathlib import Path

def download_mars_photos(sol, camera, api_key, output_dir="."):
    """ Завантажує за заданий сол всі фотографії з марсохода Curiosity з API NASA. """

    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
    params = {'sol': sol, 'camera': camera, 'api_key': api_key}

    response = requests.get(url, params=params)
    data = response.json()
    photos = data.get('photos', [])

    if photos:
        output_path = Path(output_dir)
        if not output_path.exists():
            output_path.mkdir(parents=True)

        for i, photo in enumerate(photos):
            img_url = photo['img_src']
            img_response = requests.get(img_url, stream=True)

            filename = f"mars_photo{i + 1}.jpg"
            filepath = output_path / filename
            with filepath.open('wb') as f:
                for chunk in img_response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"Saved {filepath}")
    else:
        print("Not found.")


if __name__ == '__main__':

    sol = 1000
    camera = 'fhaz'
    api_key = 'DEMO_KEY'
    output_dir = "mars_photos"

    download_mars_photos(sol, camera, api_key, output_dir)