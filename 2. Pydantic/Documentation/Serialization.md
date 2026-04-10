# Serialization

Serialization converts Pydantic models to dictionaries or JSON for storage, transmission, or API responses.

## Convert to Dictionary

```python
from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    height: float
    gender: str = "Not specified"

patient = Patient(name="John Doe", age=30, weight=70.5, height=175.0)

# Convert to dict
data_dict = patient.model_dump()
print(data_dict)
# {'name': 'John Doe', 'age': 30, 'weight': 70.5, 'height': 175.0, 'gender': 'Not specified'}
print(type(data_dict))  # <class 'dict'>
```

## Convert to JSON

```python
# Convert to JSON string
json_data = patient.model_dump_json()
print(json_data)
# '{"name":"John Doe","age":30,"weight":70.5,"height":175.0,"gender":"Not specified"}'
print(type(json_data))  # <class 'str'>
```

## Include/Exclude Fields

```python
# Include only specific fields
data = patient.model_dump(include={"name", "age"})
# {'name': 'John Doe', 'age': 30}

# Exclude specific fields
data = patient.model_dump(exclude={"name", "age"})
# {'weight': 70.5, 'height': 175.0, 'gender': 'Not specified'}
```

## Exclude Unset Fields

```python
# Exclude fields with default values that weren't explicitly set
data = patient.model_dump(exclude_unset=True)
# {'name': 'John Doe', 'age': 30, 'weight': 70.5, 'height': 175.0}
# (excludes 'gender' since it was not provided during creation)
```

## Serialization Methods

| Method | Output | Use Case |
|--------|--------|----------|
| `model_dump()` | Python dict | Database storage, local processing |
| `model_dump_json()` | JSON string | API responses, file storage, transmission |

## Common Parameters

- `include`: Set of fields to include
- `exclude`: Set of fields to exclude
- `exclude_unset`: Exclude fields with default values
- `exclude_defaults`: Exclude fields with default values
- `exclude_none`: Exclude fields with None values
