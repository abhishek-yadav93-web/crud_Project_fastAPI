from pydantic import BaseModel, EmailStr
from typing import Optional
 
class EmployeeBase(BaseModel):
    name: str
    email: EmailStr
 
class EmployeeCreate(EmployeeBase):
    email: Optional[EmailStr] = None  # FIX: Optional must have a default value (None)
 
class EmployeeUpdate(EmployeeBase):
    pass
 
class EmployeeOut(EmployeeBase):
    id: int
 
    class Config:
        from_attributes = True  # Allows Pydantic to read data from SQLAlchemy objects
 