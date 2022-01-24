from re import X
from flask import Flask, request, jsonify
from joblib import load

app = Flask(__name__)
model = load('modelling/linear_model.joblib')

@app.route('/')
def home():
    return 'App Initialized...'

@app.route('/predict', methods=['POST'])
def predict():
    message = request.get_json(force=True)
    length = len(message)
    
    output = round(model.predict([[message['Height']]])[0][0], 1)
    print(output)
    return jsonify(output)

def test():
    return 'Test Complete'

def calc(x, y, z):
    total = x + y + z
    max = max([x,y,z])
    min = min([x,y,z])

    return total, max, min

if __name__ == '__main__':
    app.run(debug=True)