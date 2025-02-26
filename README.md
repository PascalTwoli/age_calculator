# Age Calculator Web App

This is a simple Age Calculator web application that allows users to enter their birth date and calculates their age in years, months, and days.

## Features
- User-friendly interface to input birth date
- Calculates and displays age in years, months, and days
- Frontend built with HTML, CSS, and JavaScript
- Backend API built using Flask
- Hosted on Vercel (frontend) and Render (backend)

## Tech Stack
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python (Flask)
- **Deployment:** Vercel (Frontend), Render (Backend)

## Setup Instructions
### Prerequisites
Ensure you have the following installed:
- Python (>=3.7)
- Flask
- flask-cors (for handling CORS issues)

### Backend Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/age-calculator.git
   cd age-calculator
   ```
2. Install dependencies:
   ```bash
   pip install flask flask-cors
   ```
3. Run the Flask app:
   ```bash
   python app.py
   ```
4. The backend will start at `http://127.0.0.1:5000`

### Frontend Setup
1. Open `index.html` in a browser or use a local server:
   ```bash
   python -m http.server 5500  # For local testing
   ```
2. Update the `fetch` request in `script.js` to match the backend URL.

## Deployment
### Frontend
The frontend is deployed on **Vercel**:
- Hosted at: `https://tells-your-age.vercel.app`

### Backend
The Flask API is deployed on **Render**:
- Hosted at: `https://age-calculator-15xf.onrender.com`

## Troubleshooting
### CORS Issues
If you face CORS errors, ensure your Flask backend has the following:
```python
from flask_cors import CORS
CORS(app)
```

### API Not Found (404)
Ensure that the correct endpoint is being called from the frontend:
```javascript
fetch("https://age-calculator-15xf.onrender.com/age_calculations", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ year, month, day })
})
```

## License
This project is open-source and available under the MIT License.

---

Feel free to contribute or raise issues if you encounter any problems!

