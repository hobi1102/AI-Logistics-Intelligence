import joblib
from pathlib import Path

from data_preprocessing import load_vendor_invoice_data, prepare_features, split_data
from model_evaluation import (
    train_linear_regression,
    train_decision_tree,
    train_random_forest,
    evaluate_model
)

def main():
    db_path = Path(__file__).parent.parent / "inventory.db"
    model_dir = Path("models")
    model_dir.mkdir(exist_ok=True)
    df = load_vendor_invoice_data(db_path)

    # Prepare data
    X, y = prepare_features(df)
    X_train, X_test, y_train, y_test = split_data(X, y)

    # Train models
    lr_model = train_linear_regression(X_train, y_train)
    dt_model = train_decision_tree(X_train, y_train)
    rf_model = train_random_forest(X_train, y_train)

    # Evaluate models
    results = []
    results.append(evaluate_model(lr_model, X_test, y_test, "Linear Regression"))
    results.append(evaluate_model(dt_model, X_test, y_test, "Decision Tree Regression"))
    results.append(evaluate_model(rf_model, X_test, y_test, "Random Forest Regression"))

    # Select best model (lowest MAE)
    best_model_info = min(results, key=lambda x: x["mae"])
    best_model_name = best_model_info["model_name"]

    best_model = {
        "Linear Regression": lr_model,
        "Decision Tree Regression": dt_model,
        "Random Forest Regression": rf_model,
    }[best_model_name]

    # Save all models
    joblib.dump(lr_model, model_dir / "freight_lr.pkl")
    joblib.dump(dt_model, model_dir / "freight_dt.pkl")
    joblib.dump(rf_model, model_dir / "freight_rf.pkl")
    # Also save as default
    joblib.dump(best_model, model_dir / "predict_freight_model.pkl")

    print(f"All models saved (Linear, Decision Tree, Random Forest)")

if __name__ == "__main__":
    main()