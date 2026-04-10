
from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    height: float
    gender: str = "Not specified" 

patient_info = {
    "name": "John Doe",
    "age": 30,
    "weight": 70.5,
    "height": 175.0
}
patient1 = Patient(**patient_info)