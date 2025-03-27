from fastapi import FastAPI, HTTPException
from pathlib import Path
import joblib
import numpy as np
from pydantic import BaseModel
import sys
import os

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

# Get the absolute path to the model file
try:
    # Resolve the path relative to this script's location
    SCRIPT_DIR = Path(__file__).parent.resolve()
    MODEL_PATH = SCRIPT_DIR.parent / "models" / "loan_model.pkl"
    
    # Verify the model file exists
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
    
    # Load the model
    model = joblib.load(MODEL_PATH)
    print(f"Model loaded successfully from {MODEL_PATH}")
    
except Exception as e:
    print(f"Error loading model: {str(e)}", file=sys.stderr)
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
        raise HTTPException(
            status_code=503,
            detail="Model not loaded. Service unavailable."
        )
    
    try:
        # Arrange features in the same order as during model training
        features = np.array([
            [loan.age, loan.income, loan.loan_amount, loan.credit_score]
        ])
        
        # Predict probability (assuming index 1 is default probability)
        probability = model.predict_proba(features)[0][1]
        
        return {
            "loan_default_probability": round(float(probability), 4)
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction error: {str(e)}"
        )

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)