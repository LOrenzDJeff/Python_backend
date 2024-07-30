import base64
import requests

def upload_image(image_path, url):
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
    
    encoded_image = base64.b64encode(image_data).decode('utf-8')
    
    payload = {
        'image': encoded_image
    }
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        print("Изображение успешно загружено!")
    else:
        print(f"Ошибка загрузки изображения. Статус-код: {response.status_code}")

image_path = "sendsib.jpeg"
upload_url = "http://78.24.222.170:8080/api/test/upload"

upload_image(image_path, upload_url)
