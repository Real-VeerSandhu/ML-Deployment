from joblib import load

model = load('modelling/linear_model.joblib')
output = round(model.predict([[1.7]])[0][0], 1)
prediction = f'{output} kg.'

print(prediction)