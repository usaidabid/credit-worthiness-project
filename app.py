import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load(r'C:\Users\Zunnurain.Badar\credit_risk_model.pkl')

# App title
st.title("Credit Risk Prediction App")

# User input fields
st.subheader("Enter the following information:")
revolving_utilization = st.number_input("💳 Credit Utilization Ratio (%)", min_value=0.0, max_value=1.0)
age = st.number_input("👤 Age (Umar)", min_value=18, max_value=100)
num_30_59_late = st.number_input("🕒 30–59 Days Late Payments", min_value=0)
debt_ratio = st.number_input("📉 Debt-to-Income Ratio", min_value=0.0)
monthly_income = st.number_input("💰 Monthly Income ", min_value=0.0)
open_credit_lines = st.number_input("🏦 Total Active Loans/Credit Lines", min_value=0)
num_90_late = st.number_input("⏰ 90+ Days Late Payments", min_value=0)
real_estate_loans = st.number_input("🏘️ Real Estate Loans Count", min_value=0)
num_60_89_late = st.number_input("🕓 60–89 Days Late Payments", min_value=0)
dependents = st.number_input("👪 Dependents ", min_value=0)
serious_default = st.selectbox("⚠️ Any Serious Default in Last 2 Years?", [0, 1])

# Predict button
if st.button("Predict Credit Risk"):
    # Create input data
    input_data = pd.DataFrame({
        'Credit Utilization': [revolving_utilization],
        'Age': [age],
        '30-59 Days Late Payments': [num_30_59_late],
        'Debt-to-Income Ratio': [debt_ratio],
        'Monthly Income': [monthly_income],
        'Active Credit Lines': [open_credit_lines],
        '90+ Days Late Payments': [num_90_late],
        'Real Estate Loans': [real_estate_loans],
        '60-89 Days Late Payments': [num_60_89_late],
        'Dependents': [dependents],
    })

    # Remove 'Unnamed: 0' column if it exists in the input_data (this matches the training dataset)
    input_data = input_data[['Credit Utilization', 'Age', '30-59 Days Late Payments', 'Debt-to-Income Ratio',
                             'Monthly Income', 'Active Credit Lines', '90+ Days Late Payments', 'Real Estate Loans',
                             '60-89 Days Late Payments', 'Dependents']]

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Show result
    if prediction == 1:
        st.error("UnReliable Borrower ❌")
    else:
        st.success("Reliable Borrower ✅")
 
