import joblib
import pandas as pd
from flask import Flask, render_template, request, jsonify
import warnings

warnings.filterwarnings('ignore')

app = Flask(__name__)

# Load models and scaler once upon startup
try:
    invoice_model = joblib.load('models/predict_flag_invoice.pkl')
    scaler = joblib.load('models/scaler.pkl')
    
    # Load all freight regression models
    freight_models = {
        'lr': joblib.load('models/freight_lr.pkl'),
        'dt': joblib.load('models/freight_dt.pkl'),
        'rf': joblib.load('models/freight_rf.pkl')
    }
except Exception as e:
    print(f"Error loading models. Make sure they exist in the models/ directory. Exception: {e}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/predict/invoice', methods=['POST'])
def predict_invoice():
    try:
        data = request.json
        features = [
            "invoice_quantity",
            "invoice_dollars",
            "Freight",
            "total_item_quantity",
            "total_item_dollars"
        ]
        
        # Ensure all features are present
        for f in features:
            if f not in data:
                return jsonify({"error": f"Missing feature: {f}"}), 400
                
        # Create DataFrame
        df = pd.DataFrame([data], columns=features)
        
        # Scale
        df_scaled = scaler.transform(df)
        
        # Predict
        pred = invoice_model.predict(df_scaled)[0]
        
        return jsonify({
            "success": True,
            "risk_flag": int(pred),
            "message": "Flagged as Risk" if int(pred) == 1 else "Safe (No Risk Flag)"
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/predict/freight', methods=['POST'])
def predict_freight():
    try:
        data = request.json
        if 'Dollars' not in data:
            return jsonify({"error": "Missing feature: Dollars"}), 400
        
        # Get selected model type (default to rf)
        model_type = data.get('model_type', 'rf')
        if model_type not in freight_models:
            model_type = 'rf'
            
        selected_model = freight_models[model_type]
            
        df = pd.DataFrame([{"Dollars": float(data['Dollars'])}])
        
        pred = selected_model.predict(df)[0]
        
        return jsonify({
            "success": True,
            "predicted_freight": float(round(pred)),
            "message": f"${round(pred):,.2f}",
            "model_used": model_type.upper()
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
