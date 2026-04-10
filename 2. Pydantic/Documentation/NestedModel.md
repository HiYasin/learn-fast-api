# Nested Model

Nested models embed one model within another for representing complex, related data structures.

## Basic Example

```python
from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    zip_code: str

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    height: float
    address: Address  # Nested model
```

## Creating Nested Data

```python
# Method 1: Create nested model first
address = Address(city="New York", state="NY", zip_code="10001")
patient = Patient(
    name="John Doe",
    age=30,
    weight=70.5,
    height=175.0,
    address=address
)

# Method 2: Pass nested dict directly
patient = Patient(
    name="John Doe",
    age=30,
    weight=70.5,
    height=175.0,
    address={
        "city": "New York",
        "state": "NY",
        "zip_code": "10001"
    }
)
```

## Accessing Nested Data

```python
print(patient.name)                    # "John Doe"
print(patient.address.city)            # "New York"
print(patient.address.zip_code)        # "10001"
```

## Benefits

- **Better Organization**: Related data grouped logically
- **Improved Readability**: Clear data relationships
- **Reusability**: Address model can be used elsewhere
- **Automatic Validation**: Nested data validated automatically
- **Type Safety**: IDE provides autocomplete and type checking

## Example with Multiple Nested Models

```python
class ContactInfo(BaseModel):
    email: str
    phone: str

class MedicalHistory(BaseModel):
    allergies: List[str]
    medications: List[str]

class Patient(BaseModel):
    name: str
    age: int
    address: Address
    contact: ContactInfo
    medical_history: MedicalHistory
```
