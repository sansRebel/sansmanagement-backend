
from pydantic import BaseModel, EmailStr, Field
from enum import Enum

# Match the same enum values as in models.py
class ContactCategory(str, Enum):
    CUSTOMER = "Customer"
    VENDOR = "Vendor"
    VIP = "VIP"
    PARTNER = "Partner"
    EMPLOYEE = "Employee"

# Base schema shared by create/update
class ContactBase(BaseModel):
    name: str = Field(..., example="John Doe")
    phone: str = Field(..., example="123-456-7890")
    email: EmailStr = Field(..., example="john@example.com")
    company: str | None = Field(default=None, example="Acme Inc.")
    category: ContactCategory

# For creating new contacts
class ContactCreate(ContactBase):
    pass

# For updating contacts (all fields optional)
class ContactUpdate(BaseModel):
    name: str | None = None
    phone: str | None = None
    email: EmailStr | None = None
    company: str | None = None
    category: ContactCategory | None = None

# What API returns (with ID)
class ContactOut(ContactBase):
    id: int

    class Config:
        orm_mode = True
