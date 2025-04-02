"""Є вiдкритий API NASA 
який дозволяє за певними параметрами отримати данi 
у виглядi JSON про фото зробленi ровером “Curiosity” на Марсi. 
Серед цих даних є посилання на фото 
якi потрiбно розпарсити
i потiм за допомогою додаткових запитiв скачати 
i зберiгти цi фото як локальнi файли mars_photo1.jpg , mars_photo2.jpg . 
Завдання потрiбно зробити використовуючи модуль requests"""

# Початкові дані
# url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY"
# params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

import requests

def get_photo_from_curiosity(url:str = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos", params:dict = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}
):
    """Method to get 2 photos from Curiosity rover from Mars"""
    response = requests.get(url, params=params)
    recieved_data = response.json()
    get_photo = recieved_data.get("photos", [])

    for i, photo in enumerate(get_photo[:2], start=1):
        img_url = photo['img_src']
        img_response = requests.get(img_url)
        if img_response.status_code == 200:
            with open(f'mars_photo{i}.jpg', 'wb') as file:
                file.write(img_response.content)
                print(f"Image 'mars_photo{i}.jpg' was saved")
        else:
            print(f'Failed to download mars_photo{i}.jpg')
    

if __name__ =="__main__":
    get_photo_from_curiosity()