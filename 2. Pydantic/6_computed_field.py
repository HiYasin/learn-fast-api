
from pydantic import BaseModel, computed_field

# computed_field allows us to define a property that is computed based on other fields in the model. This is useful when you want to derive values that are not directly provided but can be calculated from existing data.

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    height: float

    @computed_field
    @property
    # computed_field get an instance of the model as an argument
    def bmi(self) -> float:
        return round(self.weight / (self.height / 100) ** 2, 2)

patient_info = {
    "name": "John Doe",
    "age": 30,
    "weight": 70.5,
    "height": 175.0
}

patient1 = Patient(**patient_info)

def print_patient_info(patient: Patient):
    print(f"Name: {patient.name}")
    print(f"Age: {patient.age}")
    print(f"Weight: {patient.weight}")
    print(f"Height: {patient.height}")
    print(f"BMI: {patient.bmi}")


print_patient_info(patient1)