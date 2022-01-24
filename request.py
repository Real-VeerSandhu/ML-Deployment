from urllib import request
import requests

url = 'http://localhost:5000/predict'
r = requests.post(url,json={'Height': 1.6})

print('Prediction: ', r.json(), len(r))

def read(link, response, input):
    out = request.post(link, json={'Height:': input})

    print('Type:', type(out))