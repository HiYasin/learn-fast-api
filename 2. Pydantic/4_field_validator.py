from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import List, Dict, Optional, Annotated

# field_validator allows you to define custom validation logic for specific fields in your Pydantic model.
# field_validator can be used to transfromation also.

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title="Name of patient", description="The patient's full name")]
    age: int
    weight: Annotated[float, Field(strict=True)]
    email: EmailStr


    # Custom validation logic using field_validator
    @field_validator('email')
    @classmethod
    def email_validator(cls, value): #custom validator get class and value as parameter
        valid_domains = ['hdfc.com', 'icici.com']
        domain = value.split('@')[-1]
        # .split method split the email into parts using '@' as the separator and returns a list of parts. Exampl: ['faisal', 'gmail.com']
        # The [-1] index is used to access the last part of the list"
        # In this case, it retrieves the domain part of the email address.

        if domain not in valid_domains:
            raise ValueError("Not a valid email domain")
        return value
    

    # Transformation using field_validator
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    

    # field_validator can be used in two modes (before and after) to control the order of validation and transformation
    # The 'before' mode allows you to perform validation or transformation before the standard Pydantic type validation occurs
    # The 'after' mode allows you to perform validation or transformation after the standard Pydantic type validation has been completed.
    @field_validator('weight', mode='before')
    @classmethod
    def validate_weight(cls, value):
        if isinstance(value, str):
            try:
                return float(value)
            except ValueError:
                raise ValueError("Weight must be a number")
        return value
    # Now if we run this code with weight as string, it will be converted to float before the standard Pydantic type validation occurs. If the conversion fails, a ValueError will be raised.
    # If we run this code with mode='after', the validation will occur after the standard Pydantic type validation, which means that if the weight is provided as a string, it will fail the standard Pydantic type validation before it reaches the custom validator.
    # field_validator mode allow us to control complex validation logic flexible way.

patient_info = {
    "name": "John Doe",
    "age": 30,
    "weight": '70.5',
    # "email": "faisal@gmail.com",
    # This email will fail validation because the domain 'gmail.com' is not in the list of valid domains defined in the email_validator method.

    "email": "faisal@icici.com",
}

patient1 = Patient(**patient_info)

def print_patient_info(patient: Patient):
    print(f"Name: {patient.name}")
    print(f"Age: {patient.age}")
    print(f"Weight: {patient.weight}")
    print(f"Email: {patient.email}")


print_patient_info(patient1)