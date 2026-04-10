# Pydantic Learning Module

This module covers Pydantic fundamentals for data validation and modeling in Python.

## Installation

### 1. Create a Virtual Environment

```bash
# On Windows (Command Prompt)
python -m venv .env

# Activate it
.env\Scripts\activate

# On macOS/Linux (Bash)
python3 -m venv .env
source .env/bin/activate
```

### 2. Install Pydantic

```bash
# Basic installation
pip install pydantic

# With email validation support (required for some examples)
pip install "pydantic[email]"
```

## Running the Examples

Each file demonstrates a specific Pydantic concept:

### Quick Start
```bash
python 1_why_pydantic.py
```

### Run All Examples
```bash
python 2_basic_model.py
python 3_field_annotated.py
python 4_field_validator.py
python 5_model_validator.py
python 6_computed_field.py
python 7_nested_model.py
python 8_serialization.py
```

## Module Topics

| File | Topic | Description |
|------|-------|-------------|
| `1_why_pydantic.py` | Why Pydantic | Comparison: unvalidated → type hints → manual checks → Pydantic |
| `2_basic_model.py` | Basic Models | Define and use simple Pydantic models |
| `3_field_annotated.py` | Field & Annotated | Add metadata and validation constraints |
| `4_field_validator.py` | Field Validators | Custom validation for individual fields |
| `5_model_validator.py` | Model Validators | Cross-field validation logic |
| `6_computed_field.py` | Computed Fields | Derived fields calculated from other fields |
| `7_nested_model.py` | Nested Models | Embed models within other models |
| `8_serialization.py` | Serialization | Convert models to dict/JSON |

## Documentation

Detailed documentation for each topic is available in the `Documentation/` folder:

- `WhyPydantic.md` - Why use Pydantic
- `BasicModel.md` - Basic model concepts
- `FieldAnnotated.md` - Field constraints and metadata
- `FieldValidator.md` - Single field validation
- `ModelValidator.md` - Multi-field validation
- `ComputedField.md` - Computed/derived fields
- `NestedModel.md` - Nested data structures
- `Serialization.md` - Convert to JSON/dict

## Key Concepts

### Validation
Pydantic automatically validates data types and constraints:
```python
class Patient(BaseModel):
    name: str
    age: int

patient = Patient(name="John", age=30)  # ✓ Valid
patient = Patient(name="John", age="30")  # ✗ Raises ValidationError
```

### Type Support
- Primitives: `str`, `int`, `float`, `bool`
- Collections: `List`, `Dict`, `Set`, `Tuple`
- Optional: `Optional[Type]`
- Nested: Other Pydantic models

## Deactivate Virtual Environment

```bash
deactivate
```
