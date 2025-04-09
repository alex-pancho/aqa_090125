import requests

def get_mars_photo_data(sol, camera, api_key):
    """
    Fetches data about Mars photos from NASA API using a request to the API.
    Returns JSON with photo information.
    """
    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
    params = {
        'sol': sol,
        'camera': camera,
        'api_key': api_key
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()  # Parse the JSON response
        if 'photos' not in data:
            print("Error: No photos found in the response.")
            return None
        return data
    except requests.exceptions.RequestException as e:
        print("HTTP request error:", e)
        return None
    except ValueError:
        print("Error: response is not valid JSON.")
        return None

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

def download_mars_photos(sol, camera, api_key, filename):
    """
    Main function to download Mars photos from NASA API.
    """
    data = get_mars_photo_data(sol, camera, api_key)

    if not data:
        return

    photos = data.get('photos', [])

    if not photos:
        print("No photos found for the given parameters.")
        return

    for idx, photo in enumerate(photos):
        image_url = photo.get('img_src')
        if not image_url:
            print("Photo does not have a valid URL.")
            continue  # Skip this photo

        # Create a unique filename for each photo
        unique_filename = f"{filename}_{idx+1}.jpg"
        print(f"Downloading photo: {image_url}")

        download_photo(image_url, unique_filename)

if __name__ == "__main__":
    custom_filename = "mars_photo"
    download_mars_photos(1000, 'fhaz', 'DEMO_KEY', custom_filename)