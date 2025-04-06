import requests


BASE_URL = "http://127.0.0.1:8080"
IMAGE_FILE = "example.jpg"

def photo():
    try:
        upload_url = f"{BASE_URL}/upload"
        with open(IMAGE_FILE, "rb") as img:
            files = {"image": img}
            response = requests.post(upload_url, files=files)
            response.raise_for_status()  

        image_url = response.json().get("image_url")
        print(f"Image is upload: {image_url}")


        filename = IMAGE_FILE
        get_url = f"{BASE_URL}/image/{filename}"
        headers = {"Content-Type": "text"} 

        response = requests.get(get_url, headers=headers)
        response.raise_for_status()

        image_info = response.json()
        print(f"Images link: {image_info['image_url']}")

    
        delete_url = f"{BASE_URL}/delete/{filename}"
        response = requests.delete(delete_url)
        response.raise_for_status()
        print(f"Image {filename} deleted.")
        
    except requests.exceptions.RequestException as e:
        print(f"Error during request execution: {e}")


if __name__ == "__main__":
    photo()