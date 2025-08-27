# ML Model Serving with FastAPI

A lightweight backend API for deploying and serving machine learning models. Built on FastAPI with Dockerized infrastructure and uv for dependency management.

<br>

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-white?logo=python" alt="Python" />
  </a>
  <a href="https://uv.sh/">
    <img src="https://img.shields.io/badge/UV-white?logo=uv" alt="uv" />
  </a>
  <a href="https://fastapi.tiangolo.com/">
    <img src="https://img.shields.io/badge/FastAPI-white?logo=fastapi" alt="FastAPI" />
  </a>
  <a href="https://www.docker.com/">
    <img src="https://img.shields.io/badge/Docker-white?logo=docker" alt="Docker" />
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-informational" alt="License" />
  </a>
</p>


---

## 📂 Project Structure

```text
fastapi-model-serving-api/
│
├─ src/
│   ├─ predict.py       # FastAPI inference endpoints
│   ├─ schemas.py       # Pydantic request/response validation
│   ├─ marketing.py     # Test script to query deployed API
│   └─ train.py         # Model training and serialization
│
├─ notebooks/
│   └─ draft_code.ipynb # Exploratory analysis & prototyping
│
├─ models/
│   └─ weights.bin      # Serialized ML model
│
├─ pyproject.toml       # Dependency declaration (uv-managed)
├─ uv.lock              # Locked dependencies for reproducibility
├─ Dockerfile           # Docker container configuration
├─ README.md
├─ .python-version
├─ .gitignore
└─ .venv
```

---

## 🛠️ Tech Stack

- **Python 3.13.1**
- **FastAPI** - REST API and Model Serving
- **Pydantic** - Request/response validation
- **UV** - Dependency management
- **Docker** - Containerized deployment
- **Pickle** - Model serialization

---

## 📦 Prerequisites

Depending on how you want to run -

**Option 1: Running Locally without Docker**

- Python 3.13
- [uv](https://uv.sh/) package manager
- Git

> This is only required if you want to run the API directly on your host machine.

**Option 2: Using Docker (Recommended)**

- Docker installed on your system.

> No need to install Python, uv, or packages locally. Docker contains everything.

---

## 🚀 Quick Start Guide

#### 1. Clone the repository

```bash
git clone https://github.com/arpon-kapuria/fastapi-model-serving-api.git
cd fastapi-model-serving-api
```

#### 2. Install dependencies

```bash
# Using uv package manager
uv sync --locked

# This creates a .venv and installs all required packages.
```

#### 3. Run Locally

```bash
# Run the FastAPI application locally 
uv run uvicorn src.predict:app --host 0.0.0.0 --port 9696 --reload

# --host 0.0.0.0 makes it accessible from all network interfaces
# --port 9696 sets the port to 9696
# --reload enables automatic server reload when code changes
```

#### 4. Run with Docker

```bash
# Build the Docker image
docker build -t fastapi-model-serving-api-cp .

# Run the container (the --rm flag deletes the container automatically after it stops)
docker run -it --rm -p 9696:9696 fastapi-model-serving-api-cp
```

#### 5. Testing the API

The API will be available at: **http://127.0.0.1:9696**  
Interactive API documentation (Swagger UI): **http://127.0.0.1:9696/docs**  

>`marketing.py` demonstrates sending sample requests and retrieving predictions.

Example test from terminal:

```bash 
curl -X 'POST' \
    'http://0.0.0.0:9696/predict' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
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
}'
```

#### API Endpoints

Request & Response schema: See `src/schemas.py`

| Endpoint   | Method | Description                               |
| ---------- | ------ | ----------------------------------------- |
| `/predict` | POST   | Returns the predicted probability & class |


#### Training

```bash
# Train the model and save it as models/weights.bin.
python src/train.py
```

---

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
