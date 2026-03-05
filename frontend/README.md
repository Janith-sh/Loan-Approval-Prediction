# Frontend - Loan Risk Prediction System

This is the frontend interface for the Loan Risk Prediction API.

## Features

- Clean, modern UI with responsive design
- Real-time form validation
- Interactive prediction results
- Risk factor analysis visualization
- Mobile-friendly interface

## Getting Started

### Option 1: Open Directly in Browser

Simply open `index.html` in your web browser:

```bash
# Windows
start index.html

# Or double-click the index.html file
```

### Option 2: Use a Local Server

For better CORS handling, use a local server:

```bash
# Using Python
python -m http.server 8080

# Using Node.js (if http-server is installed)
npx http-server -p 8080

# Using PHP
php -S localhost:8080
```

Then visit: `http://localhost:8080`

## Configuration

The API endpoint is configured in `js/app.js`:

```javascript
const API_BASE_URL = 'http://localhost:8000';
```

Update this URL if your backend API runs on a different address.

## Requirements

- Modern web browser (Chrome, Firefox, Safari, Edge)
- Backend API must be running (see ../app/README.md)

## Project Structure

```
frontend/
├── index.html          # Main HTML file
├── css/
│   └── style.css      # Styling
├── js/
│   └── app.js         # Application logic
└── README.md          # This file
```

## Usage

1. Fill in the loan application form with required details:
   - Age (18-100)
   - Annual Income
   - Loan Amount
   - Credit Score (300-850)
   - Employment Years
   - Debt-to-Income Ratio (0-1)
   - Loan Purpose

2. Click "Predict Risk" to get the assessment

3. View the results including:
   - Risk level (Low/High)
   - Default probability
   - Recommendation
   - Detailed risk factors analysis

## Troubleshooting

### API Connection Issues

If you see connection errors:

1. Ensure the backend API is running:
   ```bash
   cd ../app
   python main.py
   ```

2. Check that the API is accessible at `http://localhost:8000`

3. Verify CORS settings in the backend allow your frontend origin

### Browser Compatibility

This application works best on:
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+
