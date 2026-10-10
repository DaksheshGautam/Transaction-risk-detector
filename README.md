# 🚨 Transaction Risk Detector – Fraud Detection System

A machine learning demo for transaction risk detection, built using **XGBoost**, **Flask**, and **Docker**, with a **Render** deployment configuration.

This system predicts the **fraud probability** of a transaction and classifies it as **Low Risk** or **High Risk**, handling highly imbalanced fraud data effectively.

---

## 🌐 Live Demo

🔗 **Live Application:** [Transaction Risk Detector](https://transaction-risk-detector-dakshesh.onrender.com)

> ⚠️ *Note:* Hosted on Render Free Tier — the service may spin down after inactivity and take ~30–50 seconds to wake up.

---

## 🖥️ Application Preview

### 🔹 Input Form (Transaction Details)
![Input Form](ui_form.png)

### 🔹 Prediction Result (Risk & Probability)
![Prediction Result](ui_result.png)

---

## 🧠 Machine Learning Model

- **Algorithm:** XGBoost Classifier (Gradient Boosted Decision Trees)
- **Problem Type:** Binary Classification (Fraud / Non-Fraud)
- **Imbalance Handling:** `scale_pos_weight`
- **Evaluation Metric:** PR-AUC (Precision–Recall AUC)
- **Output:**
  - Fraud Probability
  - Final Risk Classification (Low Risk / High Risk)

### 📌 Why PR-AUC?
Fraud datasets are highly imbalanced. PR-AUC focuses on **precision and recall of the minority (fraud) class**, making it more reliable than accuracy.

---

## ⚙️ Features

- ✅ Real-time transaction risk prediction  
- ✅ Probability-based fraud scoring  
- ✅ Handles severe class imbalance  
- ✅ Clean and responsive UI  
- ✅ End-to-end ML inference pipeline  
- ✅ Dockerized deployment  
- ✅ Render deployment configuration
- ✅ Production-style logging & exception handling  

---

## 🏗️ Tech Stack

### Backend
- Python
- Flask
- Pandas, NumPy
- XGBoost
- scikit-learn

### Frontend
- HTML5
- CSS3

### Deployment & DevOps
- Docker
- Render
- Git & GitHub

---

## 📂 Project Structure

```text
Transaction-Risk-Detector/
│
├── app.py                     # Flask application entry point
├── Dockerfile                 # Docker configuration for deployment
├── requirements.txt           # Python dependencies
│
├── artifacts/
│   └── model.pkl              # Trained ML model
│
├── src/
│   └── transaction/
│       ├── pipelines/
│       │   └── prediction_pipeline.py   # Inference pipeline
│       │
│       ├── logger/             # Custom logging module
│       └── exception/          # Custom exception handling
│
├── templates/
│   └── index.html              # Frontend HTML template
│
├── static/
│   └── css/
│       └── styles.css          # UI styling
│
├── README.md                   # Project documentation
```

## 🔁 ML Workflow

1. User enters transaction details via UI  
2. Data is converted into a Pandas DataFrame  
3. Preprocessing & encoding handled in pipeline  
4. XGBoost model predicts fraud probability  
5. Result displayed as:
   - **Low Risk** ✅ or **High Risk** 🚨  
   - Fraud Probability score  

---

## 🚀 Deployment

- Application is **containerized using Docker**
- Deployed on **Render Web Service**
- `render.yaml` configures a free Python web service using Python 3.12.
- Install command: `pip install -r requirements.txt`
- Start command: `gunicorn --workers 1 --threads 2 --timeout 120 --bind 0.0.0.0:$PORT app:app`
- `/healthz` checks that both trained artifacts can be loaded.
- Docker also binds to the host's `PORT` (default: 10000).
- Dependency versions match the saved scikit-learn 1.8.0 and XGBoost 3.1.2 artifacts.
- Linux uses the CPU-only XGBoost package to keep the deployment small.
- Hosted on a free Render instance in Singapore.
- This service was created from the public GitHub repository URL. For future
  updates, use **Manual Deploy → Deploy latest commit** in the Render dashboard.
  Connect the GitHub provider or create a Blueprint if you want automatic deploys.

### Run locally

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open `http://localhost:10000`. Test with synthetic transaction values only.

### Verify the app

```bash
python -m unittest discover -s tests -v
```

The smoke tests exercise the real saved model, static assets, input errors,
readiness failures, and artifact loading from a different working directory.

---

## 🛡️ Disclaimer

This project is built for **educational and demonstration purposes** only.  
It should **not** be used as a standalone fraud prevention system in production financial environments without additional security, monitoring, and compliance layers.

---

## 🎤 Interview One-Liner

> “I built an end-to-end machine learning fraud detection system using XGBoost, handled class imbalance with scale_pos_weight, deployed it as a Dockerized Flask app on Render, and exposed a real-time prediction UI.”

---

## ⭐ Future Improvements

- Model explainability (SHAP)
- Confidence threshold tuning
- Authentication & rate limiting
- API versioning
- Database logging of transactions

