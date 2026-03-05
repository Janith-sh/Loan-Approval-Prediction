import requests
import json

# Test the home endpoint
try:
    response = requests.get("http://127.0.0.1:8000/")
    print("=" * 60)
    print("TEST 1: GET / endpoint")
    print("=" * 60)
    print("Status Code:", response.status_code)
    print("Response:", response.json())
    print()
except Exception as e:
    print(f"Error testing home endpoint: {e}")

# Test Case 1: High-value applicant (Graduate, Not Self-employed)
print("=" * 60)
print("TEST 2: High-value Graduate Applicant")
print("=" * 60)
try:
    test_data = {
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
    
    response = requests.post("http://127.0.0.1:8000/predict-loan", json=test_data)
    print("Status Code:", response.status_code)
    print("Response:", json.dumps(response.json(), indent=2))
    print()
except Exception as e:
    print(f"Error: {e}\n")

# Test Case 2: Moderate applicant (Not Graduate, Self-employed)
print("=" * 60)
print("TEST 3: Moderate Self-employed Applicant")
print("=" * 60)
try:
    test_data = {
        "no_of_dependents": 1,
        "income_annum": 4500000,
        "loan_amount": 1800000,
        "loan_term": 10,
        "cibil_score": 650,
        "residential_assets_value": 3000000,
        "commercial_assets_value": 500000,
        "luxury_assets_value": 800000,
        "bank_asset_value": 1200000,
        "education": "Not Graduate",
        "self_employed": "Yes"
    }
    
    response = requests.post("http://127.0.0.1:8000/predict-loan", json=test_data)
    print("Status Code:", response.status_code)
    print("Response:", json.dumps(response.json(), indent=2))
    print()
except Exception as e:
    print(f"Error: {e}\n")

# Test Case 3: Low income applicant
print("=" * 60)
print("TEST 4: Lower Income Applicant")
print("=" * 60)
try:
    test_data = {
        "no_of_dependents": 3,
        "income_annum": 2400000,
        "loan_amount": 1000000,
        "loan_term": 8,
        "cibil_score": 580,
        "residential_assets_value": 1500000,
        "commercial_assets_value": 0,
        "luxury_assets_value": 0,
        "bank_asset_value": 150000,
        "education": "Graduate",
        "self_employed": "No"
    }
    
    response = requests.post("http://127.0.0.1:8000/predict-loan", json=test_data)
    print("Status Code:", response.status_code)
    print("Response:", json.dumps(response.json(), indent=2))
    print()
except Exception as e:
    print(f"Error: {e}\n")

print("=" * 60)
print("All tests completed!")
print("=" * 60)
