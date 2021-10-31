from flask import Flask, request, jsonify
from joblib import load

model = load('app/linear_model.joblib')

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello-world'

if __name__ == '__main__':
    app.run(debug=True)