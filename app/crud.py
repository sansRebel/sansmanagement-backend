
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy import update, delete
from . import models, schemas

# CREATE
async def create_contact(db: AsyncSession, contact: schemas.ContactCreate):
    new_contact = models.Contact(**contact.dict())
    db.add(new_contact)
    await db.commit()
    await db.refresh(new_contact)
    return new_contact

# READ (all)
async def get_all_contacts(db: AsyncSession):
    result = await db.execute(select(models.Contact))
    return result.scalars().all()

# READ (by ID)
async def get_contact_by_id(db: AsyncSession, contact_id: int):
    result = await db.execute(select(models.Contact).where(models.Contact.id == contact_id))
    return result.scalar_one_or_none()

# UPDATE
async def update_contact(db: AsyncSession, contact_id: int, data: schemas.ContactUpdate):
    existing = await get_contact_by_id(db, contact_id)
    if not existing:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(existing, key, value)
    await db.commit()
    await db.refresh(existing)
    return existing

# DELETE
async def delete_contact(db: AsyncSession, contact_id: int):
    contact = await get_contact_by_id(db, contact_id)
    if not contact:
        return None
    await db.delete(contact)
    await db.commit()
    return contact
