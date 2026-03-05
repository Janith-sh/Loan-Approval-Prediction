from fastapi import FastAPI
import joblib
import pandas as pd
from app.schema import LoanInput

app = FastAPI(title="Loan Risk Prediction API", version="1.0.0")

model = joblib.load("model/loan_model.pkl")
features = joblib.load("model/features.pkl")

@app.get("/")
def home():
    return {"message": "Loan Prediction API", "version": "1.0.0"}

@app.post("/predict-loan")
def predict_loan(data: LoanInput):
    # Prepare the input data with exact feature names (with leading space)
    # and in the exact order the model expects
    input_dict = {
        ' no_of_dependents': data.no_of_dependents,
        ' income_annum': data.income_annum,
        ' loan_amount': data.loan_amount,
        ' loan_term': data.loan_term,
        ' cibil_score': data.cibil_score,
        ' residential_assets_value': data.residential_assets_value,
        ' commercial_assets_value': data.commercial_assets_value,
        ' luxury_assets_value': data.luxury_assets_value,
        ' bank_asset_value': data.bank_asset_value,
        ' education_ Not Graduate': 1 if data.education == "Not Graduate" else 0,
        ' self_employed_ Yes': 1 if data.self_employed == "Yes" else 0
    }
    
    # Create DataFrame with correct column order
    input_data = pd.DataFrame([input_dict])
    
    # Ensure columns are in the same order as features
    input_data = input_data[features.tolist()]

    # Make prediction
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    # Determine risk level
    risk = "Low"
    if probability < 0.4:
        risk = "High"
    elif probability < 0.7:
        risk = "Medium"

    return {
        "approval_probability": round(float(probability), 2),
        "risk_level": risk,
        "loan_approved": bool(prediction)
    }