import requests

url = 'http://localhost:5000/predict'
r = requests.post(url,json={'Height': 1.6})

print('Prediction: ', r.json(), len(r)) # This is a comment because they are useful for all things communication, readability, and accessibility there