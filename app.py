from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    status = None

    if request.method == 'POST':
        try:
            age = float(request.form['age'])
            bp = float(request.form['restbp'])
            chol = float(request.form['cholesterol'])
            hr = float(request.form['maxhr'])

            input_data = np.array([[age, bp, chol, hr]])
            pred = model.predict(input_data)[0]
            prediction = "High Risk of Heart Disease" if pred == 1 else "Low Risk"
            status = "danger" if pred == 1 else "success"
        except:
            prediction = "Invalid Input"
            status = "warning"

    return render_template("index.html", prediction=prediction, status=status)

if __name__ == '__main__':
    app.run(debug=True)
