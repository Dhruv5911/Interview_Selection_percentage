# Interview Selection Prediction

This project is a machine learning web application that predicts a candidate’s  
**interview selection probability (percentage)** based on academic performance.

---

## Project Overview

The application uses a trained machine learning model to estimate the likelihood
of interview selection using academic inputs such as MCAT marks and CGPA.
The trained model is loaded from a serialized `.pkl` file and predictions are
served through a Flask web interface.

---

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Flask
- HTML
- CSS
- Joblib

---

## Machine Learning Model

- Algorithm: Linear Regression
- The trained model is stored as `model.pkl`
- The model predicts:
  - Interview selection percentage
  - Selection likelihood based on a threshold

---

## Project Structure

Interview_Selection_Prediction/
│
├── app.py # Flask application
├── data.py # Data preprocessing logic
├── model.py # Model training script
├── model.pkl # Trained ML model
├── Student.csv # Dataset
├── README.md # Project documentation
│├── templates/
│ └── index.html # Frontend HTML
│
└── static/
└── style.css # CSS styling

---

## How to Run the Project

### 1. Install required libraries
```bash
pip install flask pandas scikit-learn joblib
python model.py
python app.py
http://127.0.0.1:5000

---


