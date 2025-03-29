import requests
from pathlib import Path

from lesson_19.logger import logger

URL = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
PARAMS = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

DIR_PATH = Path(__file__).parent / "mars_photo"
DIR_PATH.mkdir(exist_ok=True)


def get_img_urls(site_url):
    """Get image urls from mars site"""
    response = requests.get(site_url, params=PARAMS)
    response.raise_for_status()
    data = response.json()

    if not data or not data.get("photos", False) or not data["photos"]:
        raise ValueError("No photos found", data)

    return [photo.get("img_src") for photo in data["photos"]]


def download_images(site_url):
    """Download images from mars site"""
    img_paths = []
    try:
        urls = get_img_urls(site_url)

        for i, img_url in enumerate(urls, start=1):

            img_path = DIR_PATH / f"mars_photo{i}.jpg"

            try:
                img_response = requests.get(img_url)
                img_response.raise_for_status()

                with open(img_path, 'wb') as file:
                    file.write(img_response.content)

                logger.info(f"Photo successfully uploaded: {img_path}")
                img_paths.append(img_path)

            except requests.exceptions.RequestException as e:
                logger.error("Download error:", e)
                return []

    except requests.exceptions.HTTPError as e:
        logger.error('HTTP Error:', e)
        return []

    except ValueError as e:
        logger.error(e)
        return []

    return img_paths


if __name__ == '__main__':
    print(download_images(URL))
