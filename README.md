# Loan Risk Prediction API

A complete machine learning system for predicting loan default risk with a REST API and web interface.

## Project Structure

```
loan-risk-api/
│
├── data/                   # Training data
│   └── loan_data.csv
│
├── notebooks/              # Jupyter notebooks for training
│   └── training.ipynb
│
├── model/                  # Trained models
│   └── loan_model.pkl
│
├── app/                    # FastAPI application
│   ├── main.py            # API endpoints
│   ├── schema.py          # Pydantic schemas
│   └── predictor.py       # Prediction logic
│
├── utils/                  # Utility functions
│   └── preprocessing.py
│
├── frontend/               # Web interface
│   ├── index.html
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── app.js
│   └── README.md
│
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Train the Model

Open and run the Jupyter notebook:

```bash
jupyter notebook notebooks/training.ipynb
```

Run all cells to train and save the model.

### 3. Start the API Server

```bash
cd app
python main.py
```

The API will be available at: `http://localhost:8000`

### 4. Open the Frontend

Open `frontend/index.html` in your browser, or serve it:

```bash
cd frontend
python -m http.server 8080
```

Visit: `http://localhost:8080`

## API Documentation

Once the server is running, visit:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Example API Request

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 35,
    "income": 75000,
    "loan_amount": 250000,
    "credit_score": 720,
    "employment_years": 10,
    "debt_to_income": 0.35,
    "loan_purpose": "home"
  }'
```

### API Response

```json
{
  "risk_prediction": "low",
  "risk_probability": 0.15,
  "recommendation": "Approved - Low risk applicant with favorable profile",
  "factors": {
    "credit_score": "excellent",
    "debt_to_income": "healthy",
    "employment": "very stable",
    "loan_to_income": "reasonable"
  }
}
```

## Features

### Backend API
- ✅ FastAPI framework for high performance
- ✅ Pydantic data validation
- ✅ Machine learning prediction with scikit-learn
- ✅ Risk factor analysis
- ✅ Comprehensive error handling
- ✅ CORS support for frontend integration
- ✅ Auto-generated API documentation

### Frontend
- ✅ Modern, responsive design
- ✅ Real-time form validation
- ✅ Interactive result visualization
- ✅ Risk probability gauge
- ✅ Detailed factor analysis
- ✅ Mobile-friendly interface

### Machine Learning
- ✅ Random Forest Classifier
- ✅ Feature preprocessing pipeline
- ✅ Model persistence with joblib
- ✅ Training notebook included

## Development

### Running Tests

```bash
pytest
```

### Code Structure

**app/main.py**: Main FastAPI application with endpoints
**app/schema.py**: Request/response models using Pydantic
**app/predictor.py**: Model loading and prediction logic
**utils/preprocessing.py**: Data preprocessing utilities
**notebooks/training.ipynb**: Model training workflow

## Model Details

The system uses a Random Forest Classifier trained on the following features:
- Age
- Annual Income
- Loan Amount
- Credit Score
- Employment Years
- Debt-to-Income Ratio
- Loan Purpose

## Requirements

- Python 3.8+
- FastAPI
- scikit-learn
- pandas
- numpy
- uvicorn

See `requirements.txt` for complete list.

## Production Deployment

For production deployment:

1. Update CORS origins in `app/main.py`
2. Use environment variables for configuration
3. Set up proper logging
4. Use production ASGI server (Gunicorn + Uvicorn)
5. Implement authentication/authorization
6. Add rate limiting
7. Set up monitoring

## License

MIT License

## Contributing

Pull requests are welcome! Please ensure code quality and add tests for new features.
