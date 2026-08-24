import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("student_performance_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓"
)

# Title
st.title("🎓 Student Performance Predictor")

st.write(
    "Enter the student's academic information below to predict "
    "their final marks."
)

# Input fields
study_hours = st.number_input(
    "Study Hours",
    min_value=0.0,
    max_value=24.0,
    value=5.0
)

attendance = st.number_input(
    "Attendance (%)",
    min_value=0.0,
    max_value=100.0,
    value=75.0
)

previous_score = st.number_input(
    "Previous Score",
    min_value=0.0,
    max_value=100.0,
    value=60.0
)

assignments_score = st.number_input(
    "Assignment Score",
    min_value=0.0,
    max_value=100.0,
    value=60.0
)

# Prediction
if st.button("Predict Final Marks"):

    student_data = pd.DataFrame({
        "Study_Hours": [study_hours],
        "Attendance": [attendance],
        "Previous_Score": [previous_score],
        "Assignments_Score": [assignments_score]
    })

    prediction = model.predict(student_data)[0]

    st.success(
        f"Predicted Final Marks: {prediction:.2f}"
    )
