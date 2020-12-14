from flask import Flask, request
from pyzbar.pyzbar import decode
# from PIL import image

app = Flask('Mart API')


@app.route('/api/barcode', methods=['POST'])
def barcode():
    if request.method == 'POST':

      # testing dummy post request 

      # Write this in your terminal
      
      # # curl -X POST -F 'dummy=avikant' http://127.0.0.1:5000/api/barcode
      
      # uncomment the following lines to check post request
      dummyText = request.form.get('dummy')
      print(dummyText)
      return 'Okay daddy\n'

      # barcodeImageEncoded = request.form.get('barcode_encoded_image')
      

if __name__ == '__main__':
    app.run(debug=True)
