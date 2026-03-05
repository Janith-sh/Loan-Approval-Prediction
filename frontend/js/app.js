// API Configuration
const API_BASE_URL = 'http://localhost:8000';

// DOM Elements
const loanForm = document.getElementById('loanForm');
const resultContainer = document.getElementById('result');
const resultContent = document.getElementById('resultContent');
const submitBtn = loanForm.querySelector('button[type="submit"]');
const btnText = submitBtn.querySelector('.btn-text');
const loader = submitBtn.querySelector('.loader');

// Event Listeners
loanForm.addEventListener('submit', handleFormSubmit);
loanForm.addEventListener('reset', handleFormReset);

// Form Submit Handler
async function handleFormSubmit(event) {
    event.preventDefault();
    
    // Get form data
    const formData = new FormData(loanForm);
    const applicationData = {
        age: parseInt(formData.get('age')),
        income: parseFloat(formData.get('income')),
        loan_amount: parseFloat(formData.get('loan_amount')),
        credit_score: parseInt(formData.get('credit_score')),
        employment_years: parseInt(formData.get('employment_years')),
        debt_to_income: parseFloat(formData.get('debt_to_income')),
        loan_purpose: formData.get('loan_purpose')
    };

    // Validate data
    if (!validateFormData(applicationData)) {
        return;
    }

    // Show loading state
    setLoadingState(true);

    try {
        // Make API call
        const result = await predictLoanRisk(applicationData);
        
        // Display result
        displayResult(result);
        
        // Scroll to result
        resultContainer.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    } catch (error) {
        displayError(error.message);
    } finally {
        setLoadingState(false);
    }
}

// Form Reset Handler
function handleFormReset() {
    resultContainer.style.display = 'none';
    resultContent.innerHTML = '';
}

// Validate Form Data
function validateFormData(data) {
    const errors = [];

    if (data.age < 18 || data.age > 100) {
        errors.push('Age must be between 18 and 100');
    }

    if (data.income <= 0) {
        errors.push('Income must be greater than 0');
    }

    if (data.loan_amount <= 0) {
        errors.push('Loan amount must be greater than 0');
    }

    if (data.credit_score < 300 || data.credit_score > 850) {
        errors.push('Credit score must be between 300 and 850');
    }

    if (data.employment_years < 0) {
        errors.push('Employment years cannot be negative');
    }

    if (data.debt_to_income < 0 || data.debt_to_income > 1) {
        errors.push('Debt-to-income ratio must be between 0 and 1');
    }

    if (errors.length > 0) {
        alert('Please fix the following errors:\n\n' + errors.join('\n'));
        return false;
    }

    return true;
}

// API Call
async function predictLoanRisk(applicationData) {
    const response = await fetch(`${API_BASE_URL}/predict`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(applicationData)
    });

    if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Failed to get prediction');
    }

    return await response.json();
}

// Display Result
function displayResult(result) {
    const riskClass = result.risk_prediction === 'low' ? 'risk-low' : 'risk-high';
    const riskIcon = result.risk_prediction === 'low' ? '✅' : '⚠️';
    const probabilityPercent = (result.risk_probability * 100).toFixed(1);

    resultContent.innerHTML = `
        <div class="result-summary">
            <div class="risk-badge ${riskClass}">
                ${riskIcon} ${result.risk_prediction.toUpperCase()} RISK
            </div>
            
            <div class="detail-item">
                <div class="detail-label">Default Probability</div>
                <div class="probability-bar">
                    <div class="probability-fill" style="width: ${probabilityPercent}%">
                        ${probabilityPercent}%
                    </div>
                </div>
            </div>

            <div class="detail-item">
                <div class="detail-label">Recommendation</div>
                <div class="detail-value">${result.recommendation}</div>
            </div>
        </div>

        <div class="result-details">
            <h3 style="margin: 20px 0 15px 0; color: var(--text-primary);">Risk Factors Analysis</h3>
            <div class="factors-grid">
                ${Object.entries(result.factors).map(([key, value]) => `
                    <div class="factor-card">
                        <div class="factor-label">${formatFactorLabel(key)}</div>
                        <div class="factor-value">${formatFactorValue(value)}</div>
                    </div>
                `).join('')}
            </div>
        </div>
    `;

    resultContainer.style.display = 'block';
}

// Display Error
function displayError(message) {
    resultContent.innerHTML = `
        <div class="error-message">
            <strong>Error:</strong> ${message}
            <br><br>
            <small>Please make sure the API server is running at ${API_BASE_URL}</small>
        </div>
    `;
    resultContainer.style.display = 'block';
}

// Set Loading State
function setLoadingState(isLoading) {
    submitBtn.disabled = isLoading;
    btnText.style.display = isLoading ? 'none' : 'inline';
    loader.style.display = isLoading ? 'inline-block' : 'none';
}

// Format Factor Label
function formatFactorLabel(label) {
    return label
        .split('_')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join(' ');
}

// Format Factor Value
function formatFactorValue(value) {
    return value
        .split('_')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join(' ');
}

// Check API Health on Load
async function checkAPIHealth() {
    try {
        const response = await fetch(`${API_BASE_URL}/health`);
        if (response.ok) {
            console.log('✅ API is healthy and ready');
        }
    } catch (error) {
        console.warn('⚠️ API is not responding. Please start the backend server.');
        console.log('Run: cd app && python main.py');
    }
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    checkAPIHealth();
    console.log('🚀 Loan Risk Prediction System initialized');
});
