import streamlit as st
import pickle
from data_preprocessing import preprocess_input
from logger import logger

# Page config
st.set_page_config(page_title="LoanMate - Eligibility Checker", page_icon="💰")

# Main Title Section
st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='color: #FF6F61;'>💰 LoanMate</h1>
        <h3 style='color: #f1f1f1;'>Your Personalized Loan Eligibility Checker </h3>
    </div>
    """, unsafe_allow_html=True
)

# Input Section Header
st.markdown("### 👤 Enter Your Details Below")

# Two-column form layout
with st.form("loan_form"):
    col1, col2 = st.columns(2)

    with col1:
        gender = st.radio("👫 Gender", ["Male", "Female"])
        married = st.radio("💍 Married?", ["Yes", "No"])
        dependents = st.selectbox("👶 Number of Dependents", ["0", "1", "2", "3+"])
        education = st.radio("🎓 Education Level", ["Graduate", "Not Graduate"])

    with col2:
        self_employed = st.radio("🧑‍💼 Self Employed?", ["Yes", "No"])
        applicant_income = st.number_input("💰 Applicant Income", min_value=0, max_value=25000, step=500)
        coapplicant_income = st.number_input("👥 Coapplicant Income", min_value=0, max_value=25000, step=500)
        loan_amount = st.slider("🏦 Loan Amount (in $1000s)", 50, 700, 150)

    loan_term = st.selectbox("⏳ Loan Term", [360, 180, 120, 60])
    credit_history = st.selectbox("📊 Credit History", [1.0, 0.0])
    property_area = st.selectbox("📍 Property Area", ["Urban", "Semiurban", "Rural"])

    # Submit Button
    submitted = st.form_submit_button("✅ Check Eligibility")

# Result
if submitted:
    input_data = {
        'Gender': gender,
        'Married': married,
        'Dependents': dependents,
        'Education': education,
        'Self_Employed': self_employed,
        'ApplicantIncome': applicant_income,
        'CoapplicantIncome': coapplicant_income,
        'LoanAmount': loan_amount,
        'Loan_Amount_Term': loan_term,
        'Credit_History': credit_history,
        'Property_Area': property_area
    }

    try:
        model = pickle.load(open("model.pkl", "rb"))
        processed = preprocess_input(input_data)
        prediction = model.predict(processed)[0]
        result = "🎉 **Loan Approved!**" if prediction == 1 else "🚫 **Loan Denied.**"

        st.markdown("---")
        st.markdown(f"### 🧾 Result: {result}")
        logger.info(f"Prediction made successfully: {result}")

    except Exception as e:
        st.error("❗ An error occurred during prediction.")
        logger.error("Prediction failed", exc_info=True)
