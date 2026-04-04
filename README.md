# AI Logistics Intelligence & Freight Predictor

A sleek, machine-learning-powered web interface built with pure Python/Flask and scikit-learn. This full-stack application allows users to predict future freight costs and flag anomalous vendor invoices using trained Random Forest Models over local inventory data. 

## ✨ Features

- **Minimalist Web UI**: Fast, responsive web interface utilizing high-contrast typography and minimalist design. 
- **Freight Cost Predictor (ML)**: Uses `predict_freight_model.pkl` to estimate shipping/freight costs given an invoice's dollar amount.
- **Invoice Risk Analyzer (ML)**: Uses `predict_flag_invoice.pkl` to analyze the relationship between Invoice Quantity, Invoice Dollars, Freight, PO Total Quantity, and PO Total Dollars, safely flagging dangerous outliers.
- **RESTful Endpoints**: Dedicated JSON POST endpoints (`/api/predict/freight` and `/api/predict/invoice`) allow for usage beyond the UI.

## 🛠️ Tech Stack
- **Frontend:** HTML, CSS (Vanilla Custom Minimalist Theme), JavaScript (Vanilla Form APi Fetching)
- **Backend:** Flask (Python)
- **Machine Learning**: `scikit-learn` Random Forest Regressor & Classifiers, `joblib` for model extraction, `pandas` for dataframe scaling. 

## 🚀 Getting Started

### Local Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/ai-logistics-app.git
   cd ai-logistics-app
   ```
2. **Setup a virtual environment (optional but recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate    # On Mac/Linux
   .venv\Scripts\activate       # On Windows
   ```
3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the application!**
   ```bash
   python app.py
   ```
5. Visit `http://127.0.0.1:5000` in your web browser.

## 📦 Deployment (Render / Vercel)
This application is fully equipped with a `requirements.txt` specifically supporting a `gunicorn==20.1.0` WSGI interface.
To host on Render.com:
1. Connect your GitHub repository to a new Render "Web Service" 
2. Set the Build Command to `pip install -r requirements.txt`
3. Set the Start Command to `gunicorn app:app`

*Note: The original database `inventory.db` is intentionally omitted via `.gitignore` to maintain server load speeds, as only the serialized `.pkl` models are strictly necessary during inference.*
