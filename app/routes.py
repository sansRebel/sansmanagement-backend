
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from . import schemas, crud
from .database import get_db

router = APIRouter(prefix="/contacts", tags=["Contacts"])

# CREATE
@router.post("/", response_model=schemas.ContactOut, status_code=status.HTTP_201_CREATED)
async def create(contact: schemas.ContactCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_contact(db, contact)

# READ ALL
@router.get("/", response_model=List[schemas.ContactOut])
async def read_all(db: AsyncSession = Depends(get_db)):
    return await crud.get_all_contacts(db)

# READ ONE
@router.get("/{contact_id}", response_model=schemas.ContactOut)
async def read_one(contact_id: int, db: AsyncSession = Depends(get_db)):
    contact = await crud.get_contact_by_id(db, contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact

# UPDATE
@router.put("/{contact_id}", response_model=schemas.ContactOut)
async def update(contact_id: int, data: schemas.ContactUpdate, db: AsyncSession = Depends(get_db)):
    updated = await crud.update_contact(db, contact_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Contact not found")
    return updated

# DELETE
@router.delete("/{contact_id}", response_model=schemas.ContactOut)
async def delete(contact_id: int, db: AsyncSession = Depends(get_db)):
    deleted = await crud.delete_contact(db, contact_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Contact not found")
    return deleted
