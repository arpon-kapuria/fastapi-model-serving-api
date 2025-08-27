import requests

url = 'http://localhost:9696/predict'

customer = {
  "gender": "male",
  "seniorcitizen": 1,
  "partner": "yes",
  "dependents": "yes",
  "phoneservice": "yes",
  "multiplelines": "no",
  "internetservice": "dsl",
  "onlinesecurity": "yes",
  "onlinebackup": "yes",
  "deviceprotection": "yes",
  "techsupport": "yes",
  "streamingtv": "yes",
  "streamingmovies": "yes",
  "contract": "month-to-month",
  "paperlessbilling": "yes",
  "paymentmethod": "electronic_check",
  "tenure": 0,
  "monthlycharges": 0,
  "totalcharges": 0
}

response = requests.post(url, json=customer)
churn = response.json()

print("Response:", churn)

if churn['churn'] == True:
    print("Send an email with promo !")
else:
    print("Don't do anything !")