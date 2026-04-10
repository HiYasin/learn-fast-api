# Computed Field

`computed_field` defines a property computed from other fields. Useful for derived values calculated from existing data.

## Basic Example

```python
from pydantic import BaseModel, computed_field
import math

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    height: float

    @computed_field
    @property
    def bmi(self) -> float:
        # BMI = weight (kg) / (height (m))^2
        return round(self.weight / (self.height / 100) ** 2, 2)
```

## Usage

```python
patient_info = {
    "name": "John Doe",
    "age": 30,
    "weight": 70.5,
    "height": 175.0
}

patient = Patient(**patient_info)
print(patient.bmi)  # Output: 23.0 (calculated from weight and height)
```

## How It Works

1. `@computed_field` marks a property as a computed field
2. `@property` decorator allows access like a regular attribute
3. Method receives `self` (model instance)
4. Return type annotation is required
5. Value is calculated on access, not stored

## When to Use

- Calculating derived values (BMI, total price, etc.)
- Formatting data from existing fields
- Aggregating multiple field values
- Computing percentages, ratios, or statistics

## With Serialization

Computed fields are included when serializing:

```python
patient.model_dump()
# Output: {
#     "name": "John Doe",
#     "age": 30,
#     "weight": 70.5,
#     "height": 175.0,
#     "bmi": 23.0
# }
```
