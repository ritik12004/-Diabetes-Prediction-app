from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import pandas as pd
import os

app = Flask(__name__)

# Load the trained Naive Bayes model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "naive_model.pkl")
model = joblib.load(MODEL_PATH)

# Dataset stats for reference ranges (from diabetes.csv)
FEATURE_STATS = {
    "Pregnancies":           {"min": 0,    "max": 17,    "normal": "0–6",      "unit": "count"},
    "Glucose":               {"min": 0,    "max": 199,   "normal": "70–140",   "unit": "mg/dL"},
    "BloodPressure":         {"min": 0,    "max": 122,   "normal": "60–80",    "unit": "mm Hg"},
    "SkinThickness":         {"min": 0,    "max": 99,    "normal": "10–40",    "unit": "mm"},
    "Insulin":               {"min": 0,    "max": 846,   "normal": "16–166",   "unit": "µU/mL"},
    "BMI":                   {"min": 0,    "max": 67.1,  "normal": "18.5–24.9","unit": "kg/m²"},
    "DiabetesPedigreeFunction": {"min": 0.078, "max": 2.42, "normal": "0.1–0.5","unit": "score"},
    "Age":                   {"min": 21,   "max": 81,    "normal": "21–50",    "unit": "years"},
}

@app.route("/")
def index():
    return render_template("index.html", stats=FEATURE_STATS)


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        features = [
            float(data["Pregnancies"]),
            float(data["Glucose"]),
            float(data["BloodPressure"]),
            float(data["SkinThickness"]),
            float(data["Insulin"]),
            float(data["BMI"]),
            float(data["DiabetesPedigreeFunction"]),
            float(data["Age"]),
        ]
        input_array = np.array(features).reshape(1, -1)
        prediction = int(model.predict(input_array)[0])
        proba = model.predict_proba(input_array)[0]
        risk_score = round(float(proba[1]) * 100, 2)

        # Risk level
        if risk_score < 30:
            risk_level = "Low"
        elif risk_score < 60:
            risk_level = "Moderate"
        else:
            risk_level = "High"

        return jsonify({
            "prediction": prediction,
            "risk_score": risk_score,
            "risk_level": risk_level,
            "no_diabetes_prob": round(float(proba[0]) * 100, 2),
            "diabetes_prob": round(float(proba[1]) * 100, 2),
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/health")
def health():
    return jsonify({"status": "ok", "model": "GaussianNB", "dataset": "Pima Indians Diabetes"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
