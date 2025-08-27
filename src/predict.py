import os
import pickle

from src.schemas import CustomerData, PredictResponse

from fastapi import FastAPI, status


app = FastAPI(title='churn-prediction')


model_path = os.path.join(os.path.dirname(__file__), "..", "models", "weights.bin")
with open(model_path, 'rb') as f_in:
    pipeline = pickle.load(f_in)


def predict_single(customer):
    result = pipeline.predict_proba(customer)[0, 1]
    return float(result)


@app.post("/predict", status_code=status.HTTP_200_OK, response_model=PredictResponse)
def predict(customer: CustomerData):
    prob = predict_single(customer.model_dump())

    return {
        "churn_probability": prob,
        "churn": prob >= 0.5
    }


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=9696)





