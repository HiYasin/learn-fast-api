# Field and Annotated

`Field` and `Annotated` provide advanced metadata and validation for model fields.

## Using Field

`Field` adds metadata and custom validation rules to fields:

```python
from pydantic import BaseModel, Field
from typing import Annotated, Optional, List

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title="Name", description="Patient's full name")]
    age: int
    weight: Annotated[float, Field(strict=True)]
    email: str
    allergies: Annotated[Optional[List[str]], Field(default=None, description="List of allergies")]
```

## Field Parameters

| Parameter | Purpose |
|-----------|---------|
| `max_length=50` | Validates string length |
| `strict=True` | No type coercion (e.g., "70.5" won't convert to float) |
| `default=None` | Sets default value |
| `title="Name"` | Display title for documentation |
| `description="..."` | Field description |

## Using Annotated

`Annotated` provides additional type information and metadata:

```python
# Without Annotated
age: int = Field(ge=0, le=150)

# With Annotated (preferred)
age: Annotated[int, Field(ge=0, le=150, description="Patient age")]
```

## Example with Strict Type Checking

```python
class Patient(BaseModel):
    weight: Annotated[float, Field(strict=True)]

patient = Patient(weight=70.5)    # ✓ Works
patient = Patient(weight="70.5")  # ✗ Error - no coercion with strict=True
```

## Benefits

- Clear field constraints and metadata
- Better documentation generation
- Type safety with strict validation
- Self-documenting code
