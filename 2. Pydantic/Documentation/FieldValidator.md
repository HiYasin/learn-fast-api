# Field Validator

`field_validator` defines custom validation logic for specific fields.

## Basic Example

```python
from pydantic import BaseModel, field_validator, EmailStr

class Patient(BaseModel):
    name: str
    email: EmailStr

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']
        domain = value.split('@')[-1]
        
        if domain not in valid_domains:
            raise ValueError("Not a valid email domain")
        return value
```

## Transformation Using Validators

Validators can also transform data:

```python
@field_validator('name')
@classmethod
def transform_name(cls, value):
    return value.upper()  # Convert to uppercase

# Input: "john" → Output: "JOHN"
```

## Validator Modes

### Mode: 'before'
Validates/transforms **before** standard Pydantic type validation:

```python
@field_validator('weight', mode='before')
@classmethod
def validate_weight(cls, value):
    if isinstance(value, str):
        try:
            return float(value)
        except ValueError:
            raise ValueError("Weight must be a number")
    return value

# "70.5" → Converts to float before type check
```

### Mode: 'after' (default)
Validates **after** standard Pydantic type validation:

```python
@field_validator('age', mode='after')
@classmethod
def validate_age(cls, value):
    if value < 0:
        raise ValueError("Age must be positive")
    return value

# Type check happens first, then custom validation
```

## Key Points

- `@classmethod` decorator required
- Receives field `value` as parameter
- Return the (possibly modified) value
- Raise `ValueError` for validation errors
- `mode='before'` for type coercion
- `mode='after'` for constraint validation
