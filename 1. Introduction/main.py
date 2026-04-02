from fastapi import FastAPI, HTTPException, Path, Query
import json
from fastapi.responses import JSONResponse

app = FastAPI()




# Utility functions to load and save data from/to the JSON file
# This will act as reading and writing to a database(JSON Storage) for our simple application.

def load_data():
    with open('patient.json', 'r') as f:
        data = json.load(f)
    return data

def save_data(data):
    with open('patient.json', 'w') as f:
        json.dump(data, f, indent=4)




# Simple GET endpoint to check if the API is working

@app.get("/")
async def root():
    return {"message": "Hello World"}

# To run the application, use the following command in your terminal:
# uvicorn main:app --reload
# Access the API documentation at http://127.0.0.1:8000/docs

@app.get("/about")
async def about():
    return {"message": "This is a simple FastAPI application."}





# Simple GET endpoint

@app.get("/view")
async def view():
    data = load_data()
    return data

@app.get("/view/{patient_id}")
async def view_patient(patient_id: int = Path(..., description="The ID of the patient to retrieve")):
    # Here ... means that the parameter is required. You can also set a default value for the parameter, like patient_id: int = Path(1, description="")
    # Read Documentation/PathFunction.md for more details on how to use Path parameters
    data = load_data()
    for patient in data:
        if patient["id"] == patient_id:
            return patient
    # Raise HTTP Error
    raise HTTPException(status_code=404, detail="Patient not found")





# GET endpoint with query parameters

@app.get("/sort")
async def sort_patients(sort_by: str = Query(..., description="The field to sort patients by (e.g., 'name', 'age', gender)"), order: str = Query("asc", description="The sort order: 'asc' for ascending (default) or 'desc' for descending")):
    # Here ... means that the parameter is required. You can also set a default value for the parameter, like order: str = Query("asc", description="")
    # Read Documentation/QueryFunction.md for more details on how to use Query parameters
    valid_fields = ["id", "name", "age", "gender"]
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid sort field: {sort_by}. Valid fields are: {', '.join(valid_fields)}")
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail=f"Invalid sort order: {order}. Valid orders are: 'asc' or 'desc'")
    
    data = load_data()
    if sort_by not in data[0]:
        raise HTTPException(status_code=400, detail=f"Invalid sort field: {sort_by}")
    # sorted_data = sorted(data, key=lambda x: x[sort_by], reverse=(order == "desc"))
    sorted_data = sorted(data, key=lambda x: x.get(sort_by, 0), reverse=(order == "desc"))
    return sorted_data





# Simple POST endpoint

from pydantic import BaseModel, Field
from typing import Annotated, Literal, Optional

# Pydantic is a data validation library that is used by FastAPI to validate the incoming request data. It allows you to define data models using Python classes and automatically validate the data against the defined model when a request is made to the API endpoint.
class Patient(BaseModel):
    id: Optional[int] = None
    name: Annotated[str, Field(..., description="The name of the patient")]
    age: Annotated[int, Field(..., description="The age of the patient must be a positive integer", gt=0)]
    gender: Annotated[Literal['Male', 'Female'], Field(..., description="The gender of the patient must be 'Male', 'Female'")]
    email: Annotated[str, Field(..., description="The email address of the patient")]

@app.post("/add")
async def add_patient(patient: Patient):

    # Load existing data
    data = load_data()

    # Assign a new ID to the patient (auto-increment)
    patient.id = max(p["id"] for p in data) + 1 if data else 1

    # Append the new patient to the data and save it back to the JSON file
    # The model_dump() method is used to convert the Pydantic model instance into a dictionary that can be easily serialized to JSON.
    data.append(patient.model_dump())
    save_data(data)
    # return {"message": "Patient added successfully", "patient": patient.model_dump()}
    return JSONResponse(status_code=201, content={"message": "Patient added successfully", "patient": patient.model_dump()})





# Simple PUT endpoint

class UpdatePatient(BaseModel):
    name: Optional[str] = Field(None, description="The name of the patient")
    age: Optional[int] = Field(None, description="The age of the patient must be a positive integer", gt=0)
    gender: Optional[Literal['Male', 'Female']] = Field(None, description="The gender of the patient must be 'Male', 'Female'")
    email: Optional[str] = Field(None, description="The email address of the patient")

@app.put("/update/{patient_id}")
async def update_patient(patient_id: int, patient_update: UpdatePatient):
    
    # Load existing data
    data = load_data()
    
    # Check if the patient with the given ID exists
    if patient_id not in [p["id"] for p in data]:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    # Get the existing patient information
    patient_info = data[patient_id-1]

    # Update the patient information with the new data
    update_patient_info = patient_update.model_dump(exclude_unset=True)

    # Update the existing patient information in the data list
    for key, value in update_patient_info.items():
        patient_info[key] = value

    # Save the updated data back to the JSON file
    save_data(data)

    return JSONResponse(status_code=200, content={"message": "Patient updated successfully", "patient": patient_info})





# Simple DELETE endpoint

@app.delete("/delete/{patient_id}")
async def delete_patient(patient_id: int):
    
    # Load existing data
    data = load_data()
    
    # Check if the patient with the given ID exists
    if patient_id not in [p["id"] for p in data]:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    # Remove the patient with the given ID from the data list
    data = [p for p in data if p["id"] != patient_id]

    # Save the updated data back to the JSON file
    save_data(data)

    return JSONResponse(status_code=200, content={"message": "Patient deleted successfully"})