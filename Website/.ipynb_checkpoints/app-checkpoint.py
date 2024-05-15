from flask import Flask, render_template, request
import sqlite3
import pandas as pd
import joblib

app = Flask(__name__)

# Define paths to database files
AMES_DB_PATH = "/Database/ames_housing.db"
TITANIC_DB_PATH = "/Database/titanic.db"

# Load trained models
ames_regression_model = joblib.load("/Models/ames_regression_model.pkl")
ames_classification_model = joblib.load("/Models/ames_classification_model.pkl")
titanic_regression_model = joblib.load("/Models/titanic_regression_model.pkl")
titanic_classification_model = joblib.load("/Models/titanic_classification_model.pkl")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about_ames")
def about_ames():
    conn = sqlite3.connect(AMES_DB_PATH)
    df = pd.read_sql_query("SELECT * FROM ames_housing LIMIT 10", conn)
    conn.close()
    return render_template("about_ames.html", data=df.to_dict(orient="records"))


@app.route("/about_titanic")
def about_titanic():
    conn = sqlite3.connect(TITANIC_DB_PATH)
    df = pd.read_sql_query("SELECT * FROM titanic LIMIT 10", conn)
    conn.close()
    return render_template("about_titanic.html", data=df.to_dict(orient="records"))


@app.route("/ames_regression", methods=["GET", "POST"])
def ames_regression():
    if request.method == "POST":
        # Get user input
        # Example: age = request.form.get("age")
        # Perform prediction using the regression model
        # Example: prediction = ames_regression_model.predict([[age]])
        return render_template("regression_prediction.html", prediction="prediction_value")
    return render_template("ames_regression.html")


@app.route("/ames_classification", methods=["GET", "POST"])
def ames_classification():
    if request.method == "POST":
        # Get user input
        # Example: feature1 = request.form.get("feature1")
        # Perform prediction using the classification model
        # Example: prediction = ames_classification_model.predict([[feature1]])
        return render_template("classification_prediction.html", prediction="prediction_value")
    return render_template("ames_classification.html")


@app.route("/titanic_regression", methods=["GET", "POST"])
def titanic_regression():
    if request.method == "POST":
        # Get user input
        # Example: age = request.form.get("age")
        # Perform prediction using the regression model
        # Example: prediction = titanic_regression_model.predict([[age]])
        return render_template("regression_prediction.html", prediction="prediction_value")
    return render_template("titanic_regression.html")


@app.route("/titanic_classification", methods=["GET", "POST"])
def titanic_classification():
    if request.method == "POST":
        # Get user input
        # Example: feature1 = request.form.get("feature1")
        # Perform prediction using the classification model
        # Example: prediction = titanic_classification_model.predict([[feature1]])
        return render_template("classification_prediction.html", prediction="prediction_value")
    return render_template("titanic_classification.html")


if __name__ == "__main__":
    app.run(debug=True)
