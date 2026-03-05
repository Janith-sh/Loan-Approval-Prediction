from pydantic import BaseModel

class LoanInput(BaseModel):
    no_of_dependents: int
    income_annum: float
    loan_amount: float
    loan_term: int
    cibil_score: int
    residential_assets_value: float
    commercial_assets_value: float
    luxury_assets_value: float
    bank_asset_value: float
    education: str  # "Graduate" or "Not Graduate"
    self_employed: str  # "Yes" or "No"
    
    class Config:
        json_schema_extra = {
            "example": {
                "no_of_dependents": 2,
                "income_annum": 9600000,
                "loan_amount": 2940000,
                "loan_term": 12,
                "cibil_score": 778,
                "residential_assets_value": 7600000,
                "commercial_assets_value": 1230000,
                "luxury_assets_value": 2200000,
                "bank_asset_value": 3800000,
                "education": "Graduate",
                "self_employed": "No"
            }
        }