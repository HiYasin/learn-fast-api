
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


# Converting the Pydantic model instance to a dictionary
temp = patient1.model_dump()
print(temp)
print(type(temp))



# Converting the Pydantic model instance to JSON
temp_json = patient1.model_dump_json()
print(temp_json)
print(type(temp_json))



# Controlled dumping with include, exclude and exclude_unset parameters
temp_include = patient1.model_dump(include={"name", "age"})
# Only include the name and age fields in the output dictionary
print("Include example:")
print(temp_include)

temp_exclude = patient1.model_dump(exclude={"name", "age"})
# Exclude the name and age fields from the output dictionary
print("Exclude example:")
print(temp_exclude)

# Exclude unset fields from the output dictionary
temp_exclude_unset = patient1.model_dump(exclude_unset=True)
# This will exclude the gender field from the output dictionary since it was not set during the creation of the patient1 instance and has a default value.
print("Exclude unset example:")
print(temp_exclude_unset)