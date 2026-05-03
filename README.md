# 🩺 DiabetaCheck — Full Stack Diabetes Risk Predictor

DiabetaCheck is a full-stack Machine Learning web application that predicts diabetes risk using a trained Gaussian Naive Bayes model based on the PIMA Indians Diabetes Dataset.

The application provides an interactive and modern medical-style interface where users can enter health parameters and instantly receive a diabetes risk prediction along with probability scores and risk analysis.

---

# 📁 Project Structure

```bash id="m6d1w2"
diabetes_app/
├── app.py                 # Flask backend (API + routing)
├── naive_model.pkl        # Trained GaussianNB model
├── diabetes.csv           # Dataset (optional)
├── requirements.txt       # Python dependencies
├── README.md
│
├── templates/
│   └── index.html         # Frontend UI
│
├── static/
│   ├── style.css
│   └── script.js
```

---

# 🚀 Quick Setup

## 1️⃣ Clone Repository

```bash id="u8x2e1"
git clone https://github.com/ritik12004/DiabetaCheck.git
```

## 2️⃣ Move Into Project Directory

```bash id="d9n4k3"
cd DiabetaCheck
```

## 3️⃣ Install Dependencies

```bash id="h3j7v5"
pip install -r requirements.txt
```

## 4️⃣ Run the Application

```bash id="k7r2q8"
python app.py
```

---

# 🌐 Open in Browser

```bash id="w1c9p4"
http://localhost:5000
```

---

# 🔌 API Endpoints

## POST `/predict`

Predicts diabetes risk from patient health data.

### Request Body (JSON)

```json id="e5f7m2"
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

### Response

```json id="r4y8u1"
{
  "prediction": 0,
  "risk_score": 23.5,
  "risk_level": "Low",
  "no_diabetes_prob": 76.5,
  "diabetes_prob": 23.5
}
```

---

## GET `/health`

Checks backend and model status.

### Response

```json id="t8p5n6"
{
  "status": "Model is running successfully"
}
```

---

# 🎨 Features

* 🎯 Diabetes risk prediction using Machine Learning
* 🎚️ Interactive sliders for all 8 health parameters
* 📊 Real-time animated risk gauge
* 📈 Probability comparison bars
* 🎨 Color-coded risk levels:

  * 🟢 Low Risk
  * 🟠 Moderate Risk
  * 🔴 High Risk
* 📱 Fully responsive design
* 🌙 Modern medical dark-themed UI
* ⚡ Fast Flask backend API

---

# 🧠 Model Details

| Attribute | Details                       |
| --------- | ----------------------------- |
| Algorithm | Gaussian Naive Bayes          |
| Dataset   | PIMA Indians Diabetes Dataset |
| Samples   | 768                           |
| Features  | 8 Health Parameters           |
| Output    | Binary Classification         |

### Prediction Labels

| Value | Meaning           |
| ----- | ----------------- |
| 0     | No Diabetes       |
| 1     | Diabetes Detected |

---

# 📊 Health Parameters Used

* Pregnancies
* Glucose Level
* Blood Pressure
* Skin Thickness
* Insulin
* BMI
* Diabetes Pedigree Function
* Age

---

# ⚙️ Technologies Used

## Backend

* Python
* Flask
* Scikit-learn
* NumPy
* Pandas

## Frontend

* HTML5
* CSS3
* JavaScript

---

# 🔄 Project Workflow

1. User enters medical details
2. Frontend sends data to Flask API
3. GaussianNB model processes input
4. Prediction probabilities are generated
5. Risk analysis is displayed instantly

---

# 🎯 Objective

The goal of this project is to provide a simple and intelligent diabetes risk prediction system using Machine Learning techniques that can help users gain early health awareness.

---

# 🔮 Future Improvements

* User authentication system
* Cloud deployment
* Medical report PDF export
* Deep Learning integration
* Real-time health monitoring
* Doctor consultation integration

---

# 🤝 Contribution

Contributions are welcome.
Feel free to fork the repository and improve the project.

---

# 📜 License

This project is developed for educational and learning purposes only.

---

# 👨‍💻 Author

**Ritik Gujre**
B.Tech CSE Student | Machine Learning & Full Stack Enthusiast

📧 Email: [ritik26cs103@satiengg.in](mailto:ritik26cs103@satiengg.in)
🐙 GitHub: https://github.com/ritik12004
💼 LinkedIn: https://www.linkedin.com/in/ritikgujre/

---

# 🌟 Support

If you like this project, give it a ⭐ on GitHub and share it with others.



