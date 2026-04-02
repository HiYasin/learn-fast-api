## 📘 FastAPI `Query()` Function – Simple Guide

### 🔹 What is `Query()`?

The `Query()` function in **FastAPI** is used to define **query parameters** with:

* Validation rules
* Default values
* Metadata (for API documentation)

Query parameters are values passed in the URL like:

```id="9mjzgj"
/items/?limit=10&skip=0
```

---

### 🔹 Why use `Query()`?

`Query()` has **two main purposes**:

#### ✅ 1. Validation (Main Purpose)

It ensures query inputs follow specific rules.

Example:

```python id="2y5sx9"
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
def read_items(limit: int = Query(gt=0, le=100)):
    return {"limit": limit}
```

✔ `limit` must be between 1 and 100
❌ `/items/?limit=-5` → Error

---

#### 📄 2. API Documentation (Swagger UI)

It enhances docs by adding:

* Title
* Description
* Examples
* Default values

---

### 🔹 Default Values

Query parameters often have defaults:

```python id="n6f6d0"
def read_items(limit: int = Query(default=10)):
    return {"limit": limit}
```

✔ If user doesn’t provide `limit`, it defaults to 10

---

### 🔹 Required Query Parameters

To make a query parameter **required**, use `...`:

```python id="1jx8h4"
def read_items(q: str = Query(...)):
    return {"q": q}
```

✔ User must provide `q`
❌ `/items/` → Error

---

### 🔹 Common Parameters

#### 📌 Metadata

* `title` → Short name
* `description` → Explanation
* `example` → Sample value

#### 📌 Numeric Validation

* `gt`, `ge`, `lt`, `le`

#### 📌 String Validation

* `min_length`
* `max_length`
* `regex`

---

### 🔹 Example with Multiple Rules

```python id="xv36j3"
@app.get("/search/")
def search(
    q: str = Query(
        default="",
        min_length=3,
        max_length=50,
        description="Search keyword"
    ),
    page: int = Query(ge=1, default=1)
):
    return {"q": q, "page": page}
```

---

### 🔹 Without `Query()`

You can also write:

```python id="6hr0u9"
@app.get("/items/")
def read_items(limit: int = 10):
    return {"limit": limit}
```

✔ Works fine
❌ But:

* No advanced validation
* Less control over docs

---

### 🔹 Multiple Query Parameters Example

```python id="ny96xn"
@app.get("/products/")
def get_products(
    category: str = Query(default="all"),
    price: float = Query(gt=0),
    in_stock: bool = Query(default=True)
):
    return {
        "category": category,
        "price": price,
        "in_stock": in_stock
    }
```
