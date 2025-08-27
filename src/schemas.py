from pydantic import BaseModel, Field
from typing import Annotated, Literal

# request validation using pydantic model

class CustomerData(BaseModel):
    gender: Literal["male", "female"]
    seniorcitizen: Annotated[int, Field(ge=0, le=1, description="0 = not senior, 1 = senior")]
    partner: Literal["yes", "no"]
    dependents: Literal["yes", "no"]
    phoneservice: Literal["yes", "no"]
    multiplelines: Literal["no", "yes", "no_phone_service"]
    internetservice: Literal["dsl", "fiber_optic", "no"]
    onlinesecurity: Literal["yes", "no", "no_internet_service"]
    onlinebackup: Literal["yes", "no", "no_internet_service"]
    deviceprotection: Literal["yes", "no", "no_internet_service"]
    techsupport: Literal["yes", "no", "no_internet_service"]
    streamingtv: Literal["yes", "no", "no_internet_service"]
    streamingmovies: Literal["yes", "no", "no_internet_service"]
    contract: Literal["month-to-month", "one_year", "two_year"]
    paperlessbilling: Literal["yes", "no"]
    paymentmethod: Literal[
        "electronic_check", 
        "mailed_check", 
        "bank_transfer_(automatic)", 
        "credit_card_(automatic)"
    ]
    tenure: Annotated[int, Field(ge=0, description="Customer tenure in months (0–72)")]
    monthlycharges: Annotated[float, Field(ge=0)]
    totalcharges: Annotated[float, Field(ge=0)]

    class Config:
        extra = "forbid"


# response validation using pydantic model

class PredictResponse(BaseModel):
    churn_probability: float
    churn: bool