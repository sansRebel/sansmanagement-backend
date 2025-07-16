
from sqlalchemy import Column, Integer, String, Enum
from .database import Base
import enum

class ContactCategory(str, enum.Enum):
    CUSTOMER = "Customer"
    VENDOR = "Vendor"
    VIP = "VIP"
    PARTNER = "Partner"
    EMPLOYEE = "Employee"

class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    company = Column(String, nullable=True)
    category = Column(Enum(ContactCategory), nullable=False)
