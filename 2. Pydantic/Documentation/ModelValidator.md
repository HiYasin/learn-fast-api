# Model Validator

`model_validator` validates across **multiple fields** or enforces constraints on the entire model.

## When to Use

Use `model_validator` when validation depends on multiple fields or requires cross-field constraints.

## Example: Cross-Field Validation

```python
from pydantic import BaseModel, model_validator
from typing import Dict

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    email: str
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        # Check emergency contact based on age
        if model.age > 60:
            if 'emergency_contact' not in model.contact_details:
                raise ValueError(
                    "Emergency contact required for patients over 60"
                )
        return model
```

## How It Works

1. All fields are validated individually first
2. Model validator receives the complete model instance
3. Access fields using dot notation: `model.age`, `model.name`
4. Return the (possibly modified) model
5. Raise `ValueError` for validation errors

## Validator Mode

### Mode: 'after' (most common)
Validates after individual field validators:

```python
@model_validator(mode='after')
def check_constraints(cls, model):
    # All fields are already validated
    # Apply cross-field logic
    return model
```

### Mode: 'before'
Validates before field validators (receives dict):

```python
@model_validator(mode='before')
def process_data(cls, data):
    # data is still a dictionary
    # Useful for data preprocessing
    return data
```

## Key Points

- Validates the entire model, not individual fields
- Use for cross-field dependencies
- Receives model instance with `mode='after'`
- Receives data dict with `mode='before'`
- Return modified model/data or raise error
