# Dataset Catalog API

A Flask-based REST API to manage datasets and their associated quality logs, backed by MongoDB. Built as part of a backend developer internship assessment.

---

## Overview of Features

* Full CRUD operations on datasets (with soft delete support)
* Quality log tracking for each dataset (status: PASS or FAIL)
* Filtering datasets by `owner` or `tag`
* Modular Flask blueprint routing:

  * `routes/dataset_routes.py` – for dataset management
  * `routes/quality_log_routes.py` – for quality log management
* Schema validation with Marshmallow
* Auto-generated API documentation via Swagger (Flasgger)
* Pytest-based testing support

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/datawise-backend.git
cd datawise-backend/backend
```

### 2. Create a Virtual Environment

```bash
py -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure MongoDB (Optional)

By default, it uses `mongodb://localhost:27017`. You can update this in `config.py`:

```python
MONGO_URI = "your_mongodb_connection_string"
```

### 5. Run the Server

```bash
py app.py
```

Visit: [http://localhost:5000/apidocs](http://localhost:5000/apidocs) for Swagger UI

---

## Assumptions Made

* MongoDB is running locally or accessible remotely without auth setup for demo
* No user authentication is needed for this assignment
* `ObjectId` is stringified when returned in API responses
* Soft delete is handled using an `is_deleted` boolean flag
* `created_at` and `updated_at` are added at the time of insert/update manually

---

## Libraries & Tools Used

| Tool / Library    | Purpose                         |
| ----------------- | ------------------------------- |
| Flask             | Web framework                   |
| PyMongo           | MongoDB driver for Python       |
| Marshmallow       | Schema validation               |
| Flasgger          | Swagger UI & OpenAPI docs       |
| Pytest            | Testing framework               |
| dotenv (optional) | Environment variable management |

---

## Project Structure

```
backend/
├── app.py                     # Main entry point
├── config.py                  # MongoDB URI config
├── requirements.txt
├── .gitignore
├── README.md
│
├── models/
│   └── schemas.py             # Marshmallow schemas
│
├── routes/
│   ├── dataset_routes.py      # Dataset CRUD APIs
│   └── quality_log_routes.py  # Quality log APIs
│
├── services/
│   ├── dataset_service.py     # Dataset logic
│   └── quality_log_service.py # Quality log logic
│
├── utils/
│   └── db.py                  # MongoDB connection helper
│
├── tests/
│   └── test_datasets.py       # Sample test cases
└── venv/                      # Virtual environment (ignored)
```

---

## Testing (Optional)

```bash
pytest tests/
```

---

## License

This project is licensed for educational and assessment purposes only.
