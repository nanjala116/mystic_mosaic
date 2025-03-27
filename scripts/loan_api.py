from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel

# Define the request schema using Pydantic
class LoanInput(BaseModel):
    age: int
    income: float
    loan_amount: float
    credit_score: int

# Initialize the FastAPI app
app = FastAPI(
    title="Loan Default Prediction API",
    description="An API to predict loan default probability.",
    version="1.0.0"
)

# Load the trained model from the models folder
model_path = "../models/loan_model.pkl"
try:
    model = joblib.load(model_path)
    print("Model loaded successfully from", model_path)
except Exception as e:
    print("Error loading model:", e)
    model = None

@app.post("/predict")
def predict_loan_default(loan: LoanInput):
    """
    Predict the probability of loan default.
    Expected JSON input:
    {
      "age": 30,
      "income": 65000,
      "loan_amount": 20000,
      "credit_score": 720
    }
    Returns JSON response:
    {
      "loan_default_probability": 0.15
    }
    """
    if model is None:
        return {"error": "Model not loaded."}
    
    # Arrange features in the same order as during model training
    features = np.array([[loan.age, loan.income, loan.loan_amount, loan.credit_score]])
    
    # Predict probability: assume index 1 corresponds to the default probability.
    probability = model.predict_proba(features)[0][1]
    return {"loan_default_probability": float(probability)}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
