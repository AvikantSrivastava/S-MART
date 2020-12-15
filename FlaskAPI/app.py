from flask import Flask, request
from pyzbar.pyzbar import decode
from PIL import Image
from base64 import b64decode
from io import BytesIO


app = Flask('Mart API')


def getBarcode(image_string):
    image = Image.open(BytesIO(b64decode(image_string)))
    barcode_data = decode(image)
    barcode_number = getattr(barcode_data[0], 'data')
    print(barcode_number)
    return barcode_number


@app.route('/api/barcode', methods=['POST'])
def barcode():
    if request.method == 'POST':

        #   # testing dummy post request
        #   # Write this in your terminal
        #   # # curl -X POST -F 'dummy=avikant' http://127.0.0.1:5000/api/barcode
        #   # uncomment the following lines to check post request
        #   dummyText = request.form.get('dummy')
        #   print(dummyText)
        #   return 'Okay daddy\n'

        barcodeImageString = request.form.get('barcode_encoded_image')
        print('got image')
        # print(barcodeImageString)
        barcode_number = getBarcode(barcodeImageString)
        return barcode_number


if __name__ == '__main__':
    app.run(debug=True)
