from pydantic import BaseModel, EmailStr, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title="Name of patient", description="The patient's full name")]
    # Field is used to add metadata and custom type validation rules to the field, such as max_length, title, and description.
    # Annotated is used to provide additional type information and metadata for the name field, which can be used for validation and specially documentation purposes.
    age: int

    # weight: float
    # The weight field is defined as a float, which means it can accept decimal values. However, if you want, you can also pass string values.
    # This means sometime pydantic allows something which is not expected.
    # So it's better to use strict when you are doubting about the type of data you are going to receive.

    weight: Annotated[float, Field(strict=True)]
    married: bool
    allergies: Annotated[Optional[List[str]], Field(default=None, description="List of allergies, if any")]
    # Setting default value with field.
    contact_info: Dict[str, str]
    email: EmailStr


patient_info = {
    "name": "John Doe",
    "age": 30,
    # "weight": '70.5',
    "weight": 70.5,
    "married": True,
    # "allergies": ["Peanuts", "Shellfish"],
    "contact_info": {
        "email": "john.doe@example.com",
        "phone": "123-456-7890"
    },
    "email": "faisal@gmail.com",
    "linkedIn": "https://www.linkedin.com/in/johndoe"
    # The linkedIn field is not defined in the Patient model, so it will be ignored when creating the Patient instance.
}

patient1 = Patient(**patient_info)

def print_patient_info(patient: Patient):
    print(f"Name: {patient.name}")
    print(f"Age: {patient.age}")
    print(f"Weight: {patient.weight}")
    print(f"Married: {patient.married}")
    print(f"Allergies : {patient.allergies}")


print_patient_info(patient1)