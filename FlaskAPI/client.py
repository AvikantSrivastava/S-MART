import requests
from PIL import Image
from base64 import b64encode
from io import BytesIO


def ImageEncoder(image):
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_str = b64encode(buffered.getvalue())
    # print(img_str)
    return img_str


if __name__ == '__main__':
    image = Image.open('barcode_test.jpg')
    image_string = ImageEncoder(image)

    url = 'http://127.0.0.1:5000' + '/api/barcode'
    data = {'barcode_encoded_image' : image_string}

    Response = requests.post(url, data= data)
    barcode_number = Response.text
    print(Response)
    print(barcode_number)
