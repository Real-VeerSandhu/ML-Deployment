import requests

url = 'http://localhost:5000/predict'
r = requests.post(url,json={'Height': 1.6})

print('Prediction: ', r.json(), len(r))