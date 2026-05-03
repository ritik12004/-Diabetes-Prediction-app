# DiabetaCheck — Full Stack Diabetes Risk Predictor

A full-stack web application that uses your trained **Gaussian Naive Bayes** model to predict diabetes risk from the PIMA Indians dataset.

## 📁 Project Structure

```
diabetes_app/
├── app.py                 # Flask backend (API + routing)
├── naive_model.pkl        # Pre-trained GaussianNB model
├── diabetes.csv           # Dataset (optional, for reference)
├── requirements.txt       # Python dependencies
├── README.md
└── templates/
    └── index.html         # Beautiful frontend UI
```

## 🚀 Quick Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the app
```bash
python app.py
```

### 3. Open in browser
```
http://localhost:5000
```

## 🔌 API Endpoints

### `POST /predict`
Send patient data, receive diabetes risk prediction.

**Request body (JSON):**
```json
{
  "Pregnancies": 3,
  "Glucose": 120,
  "BloodPressure": 70,
  "SkinThickness": 20,
  "Insulin": 80,
  "BMI": 26.0,
  "DiabetesPedigreeFunction": 0.35,
  "Age": 33
}
```

**Response:**
```json
{
  "prediction": 0,
  "risk_score": 23.5,
  "risk_level": "Low",
  "no_diabetes_prob": 76.5,
  "diabetes_prob": 23.5
}
```

### `GET /health`
Returns model health status.

## 🎨 Features
- Interactive sliders for all 8 health parameters
- Real-time risk gauge with animated fill
- Probability bars (diabetic vs non-diabetic)
- Color-coded risk levels: Low / Moderate / High
- Responsive design — works on mobile & desktop
- Medical-grade dark UI aesthetic

## 🧠 Model Details
- **Algorithm**: Gaussian Naive Bayes
- **Dataset**: PIMA Indians Diabetes (768 samples)
- **Features**: 8 health metrics
- **Output**: Binary classification (0 = No Diabetes, 1 = Diabetes)
