## 📘 Pydantic Basics – Simple Guide

### 🔹 What is Pydantic?

Pydantic is a Python library for data validation and settings management using Python type annotations. It is used heavily in FastAPI to define and validate request and response data.

---

### 🔹 Why use Pydantic?

- Ensures data is the correct type and format
- Provides automatic error messages for invalid data
- Generates clear API documentation in FastAPI

---

### 🔹 Defining a Model

A Pydantic model is a Python class that inherits from `BaseModel`:

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
```

---

### 🔹 Using a Model in FastAPI

You can use a Pydantic model as a request body:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str

@app.post("/users/")
async def create_user(user: User):
    return user
```

---

### 🔹 Field Validation

You can add validation rules using type hints and Field:

```python
from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    price: float = Field(..., gt=0)
```

---

### 🔹 Optional Fields

Use `Optional` for fields that are not required:

```python
from typing import Optional

class User(BaseModel):
    id: int
    name: str
    email: Optional[str] = None
```

---

### 🔹 Model to Dictionary

Convert a model to a dictionary (Pydantic v2):

```python
user_dict = user.model_dump()
```
Convert the Pydantic model instance into a dictionary that can be easily serialized to JSON since we use JSON formatted data in REST API.

---

### 🔹 Summary

- Pydantic models provide strong data validation
- Use type hints and Field for rules
- Integrates seamlessly with FastAPI
- Recommended for all FastAPI APIs
