import pandas as pd

def preprocess_input(input_dict):
    df = pd.DataFrame([input_dict])
    df = pd.get_dummies(df)
    
    # Align columns to match model training columns
    required_columns = [
        'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History',
        'Gender_Female', 'Gender_Male', 'Married_No', 'Married_Yes', 'Dependents_0', 'Dependents_1',
        'Dependents_2', 'Dependents_3+', 'Education_Graduate', 'Education_Not Graduate',
        'Self_Employed_No', 'Self_Employed_Yes', 'Property_Area_Rural', 'Property_Area_Semiurban',
        'Property_Area_Urban'
    ]
    for col in required_columns:
        if col not in df.columns:
            df[col] = 0
    df = df[required_columns]
    return df
