
from pydantic import BaseModel

# Nested models in Pydantic allow you to define complex data structures by embedding one model within another
# This is particularly useful when you want to represent related data that has its own set of fields.
# Better organization of data.
# Improved readability.
# Reusability of models.
# Validation of nested data structures automatically.

class Address(BaseModel):
    city: str
    state: str
    zip_code: str

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    height: float
    address: Address

address_dict = {
    "city": "New York",
    "state": "NY",
    "zip_code": "10001"
}
patient_address = Address(**address_dict)

patient_info = {
    "name": "John Doe",
    "age": 30,
    "weight": 70.5,
    "height": 175.0,
    "address": patient_address
}
patient1 = Patient(**patient_info)

def print_patient_info(patient: Patient):
    print(f"Name: {patient.name}")
    print(f"Age: {patient.age}")
    print(f"Weight: {patient.weight}")
    print(f"Height: {patient.height}")
    print(f"Address: {patient.address.city}, {patient.address.state}-{patient.address.zip_code}")


print_patient_info(patient1)