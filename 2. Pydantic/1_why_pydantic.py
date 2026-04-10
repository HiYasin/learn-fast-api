# Simple function to insert data without validation
def insert_data(name, age):
    print("Inserting data...")
    print(name)
    print(age)

# Example usage
insert_data("Alice", 30)
insert_data("Bob", "thirty")





# Using type hints for better code readability
def insert_data_with_types_hints(name: str, age: int):
    print("Inserting data with type hints...")
    print(name)
    print(age)

# Example usage
insert_data_with_types_hints("Alice", 30)
insert_data_with_types_hints("Bob", "thirty")  # This will not raise an error because type hints are not enforced at runtime





# Checking type manually
def insert_data_with_manual_type_checking(name: str, age: int):

    # if type(name)!= str or type(age) != int:
    if not isinstance(name, str):
        raise TypeError("Name must be a string")
    if not isinstance(age, int) or age <= 0:
        raise TypeError("Age must be a positive integer")
    print("Inserting data with manual type checking...")
    print(name)
    print(age)
# Example usage
insert_data_with_manual_type_checking("Alice", 30)
insert_data_with_manual_type_checking("Bob", "thirty")
# This will raise a TypeError because age is not an integer

# Checking types manually can be error-prone and can lead to a lot of boilerplate code, especially when dealing with complex data structures.

# This is where Pydantic comes in handy, as it provides a way to define data models with built-in validation and type checking, reducing the amount of manual code needed and improving code readability and maintainability.





# Pydantic workflow:
# 1. Define a Pydantic model(class) with the desired fields and types.
# 2. Create an instance(object) of the model with the data to be validated. 
# 3. Pydantic will automatically validate the data and raise errors if the data does not conform to the defined types or constraints.
# 4. Use the validated data in your application logic, knowing that it is correct and safe to use.


# Example of a Pydantic model
from pydantic import BaseModel, ValidationError
class Patient(BaseModel):
    name: str
    age: int

def insert_patient(patient: Patient):
    print("Inserting patient data...")
    print(patient.name)
    print(patient.age)

def update_age(patient: Patient, new_age: int):
    patient.age = new_age
    print("Updated patient age...")
    print(patient.name)
    print(patient.age)

patientInfo = {"name": "Alice", "age": 30}
patient = Patient(**patientInfo)

insert_patient(patient)
update_age(patient, 31)