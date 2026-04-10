
from pydantic import BaseModel, EmailStr, Field, model_validator
from typing import Dict, Annotated

# field_validator doesn't allow us to validate multiple fields together or enforce constraints that depend on the values of multiple fields. Here model_validator comes into play.

# model_validator allows you to define custom validation logic which depends on multiple fields or when you want to enforce certain constraints across the entire model.

class Patient(BaseModel):
    name: str
    age: int
    weight: Annotated[float, Field(strict=True)]
    email: EmailStr
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60:
            if 'emergency_contact' not in model.contact_details:
                raise ValueError("Emergency contact is required for patients between 18 and 60 years old.")
        return model
    # This model_validator checks emergency contact based on age.
    
patient_info = {
    "name": "John Doe",
    "age": 30,
    # "age": 65,
    "weight": 70.5,
    "email": "faisal@gmail.com",
    "contact_details": {
        "phone": "123-456-7890",
        # "emergency_contact": "Jane Doe"
    }
}

patient1 = Patient(**patient_info)

def print_patient_info(patient: Patient):
    print(f"Name: {patient.name}")
    print(f"Age: {patient.age}")
    print(f"Weight: {patient.weight}")
    print(f"Email: {patient.email}")


print_patient_info(patient1)