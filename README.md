# 🚛 AI Logistics Intelligence & Freight Predictor

A high-performance, machine-learning-powered web interface built with **Python/Flask** and **Scikit-learn**. This platform empowers logistics teams to predict freight costs and detect anomalous invoice risks before payment processing.

---

## 🏗️ How It Was Created
This project was built as a solution for data-driven logistics management. The development followed a rigorous engineering pipeline to ensure model accuracy and production reliability.

### **1. Data Engineering & Exploration**
*   **Source:** Utilized a **400MB+ SQLite database** (`inventory.db`) containing historical purchase orders and vendor invoices.
*   **Preprocessing:** Cleaned raw data using **Pandas**, handling null values and aligning purchase order totals with actual invoice payments.
*   **Feature Engineering:** Isolated key drivers like *Invoice Quantity*, *Dollar Value*, and *Freight Ratios* to create a robust multi-dimensional feature set.

### **2. Machine Learning Pipeline**
*   **Freight Estimation (Regression):** Compared **Linear Regression**, **Decision Trees**, and **Random Forest Regressors**. The Random Forest model was selected for production due to its superior handling of non-linear pricing structures.
*   **Risk Flagging (Classification):** Developed a binary classifier to identify "Anomaly Invoices." Features were scaled using `StandardScaler` to ensure the model isn't biased by large dollar amounts.
*   **Serialization:** Models were exported using `Joblib` into `.pkl` format for lightweight, high-speed inference.

### **3. Backend Architecture**
*   **REST API:** Designed a **Flask** backend with modular API endpoints (`/api/predict`) to decouple the machine learning logic from the UI.
*   **Inference Engine:** Optimized the startup script to load models once into memory, ensuring sub-100ms response times for prediction requests.

### **4. Modern UI & Responsive Design**
*   **Minimalist Aesthetic:** Built from scratch using **Vanilla CSS** with a focus on "Glassmorphism" and a dark/light minimalist color palette.
*   **Mobile First:** Implemented advanced CSS Media Queries to ensure the dashboard fits perfectly on mobile, tablet, and ultra-wide screens.

---

## 🛤️ The Path of Making
The development journey followed these specific milestones:

1.  **Discovery:** Identified the "Financial Leakage" problem in manual logistics auditing.
2.  **Model Selection:** Ran 50+ training iterations to find the optimal balance between accuracy and model size.
3.  **UI Crafting:** Designed the user interface to be "Instruction-First," ensuring non-technical users can understand ML outputs.
4.  **Deployment Optimization:** Converted the entire project to **UTF-8** and configured `vercel.json` for cloud-based serverless deployment.

---

## ✨ Key Features
-   **Multi-Model Predictor**: Toggle between Random Forest, Decision Tree, and Linear Regression for freight estimation.
-   **Risk Analysis Dashboard**: Visual indicators (Safe vs. Risk) with intuitive color coding.
-   **Instructional Overlay**: Built-in "How it Works" section to explain the AI logic to end-users.
-   **Mobile Mastery**: Fully responsive layouts optimized for on-the-go logistics auditing.

---

## 🛠️ Tech Stack
-   **Frontend:** HTML5, CSS3 (Custom Design System), JavaScript (ES6+)
-   **Backend:** Python 3.x, Flask
-   **Data Science:** Scikit-Learn, Pandas, Numpy, Joblib, SQLite

---

## 🚀 Getting Started

### Local Installation
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/ai-logistics-app.git
    cd ai-logistics-app
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the app:**
    ```bash
    python app.py
    ```
4.  Visit `http://127.0.0.1:5000` in your browser.

---

## 📦 Deployment
The application is pre-configured for **Vercel** and **Render**:
-   **Start Command:** `gunicorn app:app`
-   **Build Command:** `pip install -r requirements.txt`

*Note: The `inventory.db` is ignored in Git to keep the repo clean. Inference relies solely on the high-performance `.pkl` files in the `models/` folder.*
