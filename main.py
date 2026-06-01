import models, schemas, crud
from fastapi import FastAPI, HTTPException, Depends
from database import engine, SessionLocal, Base
from sqlalchemy.orm import Session
from typing import List
 
Base.metadata.create_all(bind=engine)
 
app = FastAPI()
 
# Dependency: provides a DB session per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
 
# Create a new employee
@app.post('/employees', response_model=schemas.EmployeeOut)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.creat_employee(db, employee)
 
# Get all employees
@app.get('/employees', response_model=List[schemas.EmployeeOut])
def get_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)  # FIX: was calling get_employees which matched the old typo
 
# Get a specific employee by ID
@app.get('/employees/{emp_id}', response_model=schemas.EmployeeOut)
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = crud.get_employee(db, emp_id)
    if employee is None:
        raise HTTPException(status_code=404, detail='Employee not found')
    return employee
 
# Update an employee
@app.put('/employees/{emp_id}', response_model=schemas.EmployeeOut)
def update_employee(emp_id: int, employee: schemas.EmployeeUpdate, db: Session = Depends(get_db)):
    db_employee = crud.update_employee(db, emp_id, employee)
    if db_employee is None:
        raise HTTPException(status_code=404, detail='Employee not found')
    return db_employee
 
# Delete an employee
@app.delete('/employees/{emp_id}', response_model=schemas.EmployeeOut)
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = crud.delete_employee(db, emp_id)
    if employee is None:
        raise HTTPException(status_code=404, detail='Employee not found')
    return employee
 