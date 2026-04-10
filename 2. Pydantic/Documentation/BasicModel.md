# Basic Model

A basic Pydantic model defines fields with types and automatically validates data.

## Simple Example

```python
from pydantic import BaseModel, EmailStr
from typing import Optional, List, Dict

class Patient(BaseModel):
    name: str
    age: int
    married: bool
    allergies: Optional[List[str]] = None
    contact_info: Dict[str, str]
    email: EmailStr
```

## Creating an Instance

```python
patient_info = {
    "name": "John Doe",
    "age": 30,
    "married": True,
    "contact_info": {
        "email": "john.doe@example.com",
        "phone": "123-456-7890"
    },
    "email": "faisal@gmail.com"
}

patient = Patient(**patient_info)
```

## Field Types

- **Basic Types**: `str`, `int`, `float`, `bool`
- **Optional Fields**: `Optional[Type] = None` - field is optional with default None
- **Collections**: `List[Type]`, `Dict[str, Type]`
- **Email**: `EmailStr` - validates email format (requires `pip install 'pydantic[email]'`)

## Accessing Fields

```python
print(patient.name)
print(patient.contact_info["phone"])
```

## Key Features

- Automatic type validation
- Default values for optional fields
- Nested dictionaries support
- Built-in validation for email format
