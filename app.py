

from flask import Flask, request, render_template, redirect, url_for
import pandas as pd
import pickle

app = Flask(__name__)

def cleaned_data(data):
    cleaned = {
        'gestation': float(data['gestation']),
        'parity': int(data['parity']),
        'age': float(data['age']),
        'height': float(data['height']),
        'weight': float(data['weight']),
        'smoke': float(data['smoke'])
    }
    return cleaned

# Home page: project description
@app.route("/")
def home():
    return render_template("home.html")

# Prediction page: form and result
@app.route("/predict", methods=["GET", "POST"])
def predict():
    prediction = None
    if request.method == "POST":
        baby_data = request.form
        baby_data_cleaned = cleaned_data(baby_data)
        baby_df = pd.DataFrame([baby_data_cleaned])
        linear_model = pickle.load(open('model/linear_regression_model.pkl', 'rb'))
        prediction = round(float(linear_model.predict(baby_df)), 2)
    return render_template("predict.html", prediction=prediction)

# About page
@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)