import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def preprocess_data(df):
    """
    Preprocess the loan data for training
    
    Args:
        df: DataFrame containing loan data
        
    Returns:
        X: Feature matrix
        y: Target vector
    """
    # Create a copy to avoid modifying original data
    data = df.copy()
    
    # Separate features and target
    X = data.drop(['default', 'loan_id'], axis=1)
    y = data['default']
    
    # Encode categorical variables
    le = LabelEncoder()
    X['loan_purpose'] = le.fit_transform(X['loan_purpose'])
    
    return X, y

def preprocess_single_application(application):
    """
    Preprocess a single loan application for prediction
    
    Args:
        application: LoanApplication schema object
        
    Returns:
        Preprocessed feature array
    """
    # Mapping for loan purpose
    loan_purpose_map = {
        'home': 0,
        'auto': 1,
        'education': 2,
        'business': 3,
        'other': 4
    }
    
    # Create feature array in the correct order
    features = pd.DataFrame([{
        'age': application.age,
        'income': application.income,
        'loan_amount': application.loan_amount,
        'credit_score': application.credit_score,
        'employment_years': application.employment_years,
        'debt_to_income': application.debt_to_income,
        'loan_purpose': loan_purpose_map.get(application.loan_purpose, 4)
    }])
    
    return features

def calculate_risk_metrics(application):
    """
    Calculate additional risk metrics from application data
    
    Args:
        application: Dictionary or object with application details
        
    Returns:
        Dictionary of risk metrics
    """
    metrics = {}
    
    # Loan-to-income ratio
    metrics['loan_to_income_ratio'] = application.loan_amount / application.income
    
    # Credit utilization indicator
    metrics['credit_health'] = 'good' if application.credit_score >= 700 else 'poor'
    
    # Employment stability score
    if application.employment_years >= 10:
        metrics['employment_score'] = 'high'
    elif application.employment_years >= 5:
        metrics['employment_score'] = 'medium'
    else:
        metrics['employment_score'] = 'low'
    
    return metrics
