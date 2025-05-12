import requests
import os

def get_mars_photo_data(sol, camera, api_key):
    """
    Fetches data about Mars photos from NASA API using a request to the API.
    Returns JSON with photo information.
    """
    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
    params = {
        'sol' : sol,
        'camera' : camera,
        'api_key' : api_key
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("HTTP request error:", e)
        return
    except ValueError:
        print("Error: response is not valid JSON.")
        return

def download_photo(image_url, filename):
    """
    Downloads a photo from the given URL and saves it locally.
    """
    try:
        image_response = requests.get(image_url)
        image_response.raise_for_status()
        with open(filename, 'wb') as file:
            file.write(image_response.content)
        print(f"Photo saved as {filename}")
    except requests.exceptions.RequestException as e:
        print("Error while downloading the image:", e)
        return

def download_mars_photos(sol, camera, api_key, max_photos=5):
    """
    Main function to download up to max_photos from Mars NASA API.
    """
    data = get_mars_photo_data(sol, camera, api_key)

    if data is None:
        return

    photos = data.get('photos', [])

    if not photos:
        print("No photos found")
        return

    os.makedirs("lesson_19/mars_photos", exist_ok=True)

    for idx, photo in enumerate(photos[:max_photos], 1):
        image_url = photo.get('img_src')
        if not image_url:
            print(f"Photo #{idx} does not have a valid URL.")
            continue

        filename = f"lesson_19/mars_photos/mars_photo{idx}.jpg"
        print(f"Downloading photo #{idx}: {image_url}")
        download_photo(image_url, filename)

if __name__ == "__main__":
    download_mars_photos(sol=1000, camera='fhaz', api_key='DEMO_KEY')
