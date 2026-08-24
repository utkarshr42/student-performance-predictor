# Student Performance Predictor

## Machine Learning Internship Project

A machine learning project that predicts a student's final marks based on
study hours, attendance, previous academic performance, and assignment score.

---

## 📌 Project Objective

The objective of this project is to develop a machine learning model that
can predict student final marks using academic performance-related features.

The project follows a complete machine learning workflow:

- Data preprocessing
- Exploratory Data Analysis (EDA)
- Feature selection
- Train-test splitting
- Model training
- Model evaluation
- Model comparison
- Prediction
- Model saving

---

## 📊 Dataset

The dataset contains student academic performance information.

### Features

| Feature | Description |
|---|---|
| Study_Hours | Number of hours spent studying |
| Attendance | Student attendance percentage |
| Previous_Score | Previous academic score |
| Assignments_Score | Assignment performance score |
| Final_Marks | Final marks to be predicted |

`Final_Marks` is the target variable.

---

## 🔍 Exploratory Data Analysis

EDA was performed to understand the relationships between the input
features and final marks.

The analysis included:

- Distribution of final marks
- Study Hours vs Final Marks
- Attendance vs Final Marks
- Previous Score vs Final Marks
- Assignment Score vs Final Marks
- Correlation analysis
- Correlation heatmap

### Correlation with Final Marks

| Feature | Correlation |
|---|---:|
| Study_Hours | 0.56 |
| Previous_Score | 0.50 |
| Assignments_Score | 0.39 |
| Attendance | 0.28 |

Study Hours showed the strongest positive correlation with Final Marks
among the features in the dataset.

---

## 🤖 Machine Learning Models

Two regression models were trained and evaluated:

### 1. Linear Regression

Used as the baseline regression model.

### 2. Random Forest Regressor

Used as a second regression model for comparison.

---

## 📈 Model Evaluation

The models were evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score

### Results

| Model | MAE | MSE | R² Score |
|---|---:|---:|---:|
| Linear Regression | 3.6141 | 20.6096 | 0.7889 |
| Random Forest | 4.3129 | 27.4090 | 0.7192 |

### 🏆 Final Model

Linear Regression was selected as the final model because it achieved
lower MAE and MSE and a higher R² score than Random Forest on the test data.

---

## 🔮 Prediction

The trained model can predict final marks for new students using:

- Study Hours
- Attendance
- Previous Score
- Assignments Score

### Example

Input:

```text
Study Hours: 8
Attendance: 90%
Previous Score: 80
Assignments Score: 85
