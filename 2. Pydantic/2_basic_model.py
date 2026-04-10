from pydantic import BaseModel, EmailStr, AnyUrl
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str
    age: int
    married: bool
    allergies: Optional[List[str]] = None
    contact_info: Dict[str, str]
    email: EmailStr
    linkedIn: AnyUrl
    

    # What is dictionary in python?
    # A dictionary in Python is a collection of key-value pairs. It is an unordered, mutable, and indexed data structure that allows you to store and retrieve values based on unique keys. Each key in a dictionary must be unique, and it is used to access the corresponding value. Dictionaries are defined using curly braces {} and can contain various data types as values, including other dictionaries, lists, and more.

patient_info = {
    "name": "John Doe",
    "age": 30,
    "married": True,
    # "allergies": ["Peanuts", "Shellfish"],
    "contact_info": {
        "email": "john.doe@example.com",
        "phone": "123-456-7890"
    },
    "email": "faisal@gmail.com",
    "linkedIn": "https://www.linkedin.com/in/johndoe"
}

def print_patient_info(patient: Patient):
    print(f"Name: {patient.name}")
    print(f"Age: {patient.age}")
    print(f"Married: {patient.married}")
    print(f"Allergies : {patient.allergies}")
    print(f"LinkedIn: {patient.linkedIn}")

print_patient_info(Patient(**patient_info))