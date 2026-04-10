# Why Pydantic?

## Problem Without Validation
Without proper validation, functions accept any type of data:
```python
def insert_data(name, age):
    print(name, age)

insert_data("Alice", 30)      # Works
insert_data("Bob", "thirty")  # Works but data is wrong!
```

## Type Hints (Not Enforced at Runtime)
Type hints improve readability but don't enforce validation:
```python
def insert_data_with_types_hints(name: str, age: int):
    print(name, age)

insert_data_with_types_hints("Bob", "thirty")  # No error raised!
```

## Manual Type Checking (Error-Prone)
Manual validation leads to boilerplate code:
```python
def insert_data_with_manual_type_checking(name: str, age: int):
    if not isinstance(name, str):
        raise TypeError("Name must be a string")
    if not isinstance(age, int) or age <= 0:
        raise TypeError("Age must be positive")
```

## Pydantic Solution
Pydantic provides **automatic validation and type checking**:

```python
from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int

patient = Patient(name="Alice", age=30)  # Validates automatically
patient = Patient(name="Bob", age="thirty")  # Raises ValidationError
```

### Pydantic Workflow:
1. Define a model with desired fields and types
2. Create an instance with data
3. Pydantic automatically validates
4. Use the validated data safely in your application

### Benefits:
- Automatic validation and type checking
- Less boilerplate code
- Improved code readability and maintainability
- Built-in error handling
