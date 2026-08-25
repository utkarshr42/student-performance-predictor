#  Student Performance Predictor

A Machine Learning project that predicts a student's final marks based on their academic performance.

##  Project Overview

This project uses Machine Learning to predict a student's Final Marks using:

- Study Hours
- Attendance
- Previous Score
- Assignment Score

The project includes data analysis, visualization, model training, model evaluation, and a Streamlit web application.

##  Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook

##  Machine Learning Models

Two regression models were evaluated:

1. Linear Regression
2. Random Forest Regression

### Model Comparison

| Model | MAE | MSE | R² Score |
|---|---:|---:|---:|
| Linear Regression | 3.614 | 20.610 | 0.789 |
| Random Forest | 4.313 | 27.409 | 0.719 |

Based on the evaluation results, **Linear Regression performed better** for this dataset.

##  Important Features

The Linear Regression coefficients showed:

- Study Hours: 2.1499
- Previous Score: 0.3050
- Assignments Score: 0.2396
- Attendance: 0.1813

Study Hours had the strongest coefficient among the input features.

##  Live Application

The trained model is deployed using Streamlit.

**Live Demo:**  
https://student-performance-predictor-jzegep7rwzctkn42mgf5pu.streamlit.app/

##  Project Structure

  text
student-performance-predictor/
│
├── app.py
├── requirements.txt
├── student_performance.csv
├── student_performance_features.pkl
├── student_performance_model.pkl
├── student_performance_prediction.ipynb
├── student_prediction_result.xls
└── README.md
