# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 13:50:41 2025

@author: sammy
"""

import streamlit as st
import pandas as pd
import joblib

# Load the trained model
with open("Downloads\salary_predictor_decision_tree.pkl", "rb") as file:  # <-- updated model filename
    model = joblib.load(file)

# Title
st.title("💼💰 Salary Midpoint Predictor 🌍🧠")

# Description
st.write("🔍 This app predicts a data scientist’s **estimated salary midpoint** (in dollars 💵) based on your background and experience. Fill in your details below! 👇")

# Input fields
country = st.selectbox("🌎 Country", ["United States", "India", "United Kingdom", "Germany", "Canada", "Other"])
gender = st.selectbox("🧑‍🤝‍🧑 Gender", ["Man", "Woman", "Prefer not to say", "Other"])
education = st.selectbox("🎓 Education Level", [
    "Bachelor’s degree", 
    "Master’s degree", 
    "Doctoral degree", 
    "Some college/university study without earning a bachelor’s degree",
    "No formal education past high school",
    "Professional degree",
    "Other"
])
years_coding = st.selectbox("💻 Years of Coding Experience", [
    "< 1 year", "1-2 years", "3-5 years", "5-10 years", "10-20 years", "20+ years"
])
job_title = st.selectbox("🧑‍💼 Job Title", [
    "Data Scientist", "Machine Learning Engineer", "Research Scientist",
    "Data Analyst", "Statistician", "Business Analyst", "Other"
])

# Prediction
if st.button("🔮 Predict Salary Midpoint"):
    input_data = pd.DataFrame({
        "Country": [country],
        "Gender": [gender],
        "Education_Level": [education],
        "Years_Coding": [years_coding],
        "Job_Title": [job_title]
    })

    prediction = model.predict(input_data)[0]
    st.success(f"🎉 Estimated Salary Midpoint: **${prediction:,.2f}** 🏆")