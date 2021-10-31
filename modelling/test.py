from joblib import load

model = load('modelling/linear_model.joblib')
pred = model.predict([[1.7]])[0][0]

print(pred)