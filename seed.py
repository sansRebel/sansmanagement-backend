
# import asyncio
# from app.database import SessionLocal, engine
# from app.models import Base
# from app.schemas import ContactCreate, ContactCategory
# from app.crud import create_contact

# video_game_contacts = [
#     {"name": "Mario", "phone": "111-111-1111", "email": "mario@nintendo.com", "company": "Mushroom Inc.", "category": "Customer"},
#     {"name": "Link", "phone": "222-222-2222", "email": "link@hyrule.com", "company": "Triforce LLC", "category": "Partner"},
#     {"name": "Samus Aran", "phone": "333-333-3333", "email": "samus@galacticfederation.org", "company": "Bounty Corp", "category": "Employee"},
#     {"name": "Master Chief", "phone": "444-444-4444", "email": "chief@unsc.com", "company": "UNSC", "category": "Vendor"},
#     {"name": "Kratos", "phone": "555-555-5555", "email": "kratos@olympus.com", "company": "GhostWarriors", "category": "VIP"},
#     {"name": "Lara Croft", "phone": "666-666-6666", "email": "lara@croftadventures.com", "company": "Croft Ltd.", "category": "Customer"},
#     {"name": "Solid Snake", "phone": "777-777-7777", "email": "snake@foxhound.org", "company": "Outer Heaven", "category": "Partner"},
#     {"name": "Cloud Strife", "phone": "888-888-8888", "email": "cloud@avalanche.com", "company": "Shinra Rebellion", "category": "Vendor"},
#     {"name": "Geralt of Rivia", "phone": "999-999-9999", "email": "geralt@witchers.org", "company": "Witcher Guild", "category": "Employee"},
#     {"name": "Ezio Auditore", "phone": "123-456-7890", "email": "ezio@assassins.net", "company": "Brotherhood", "category": "Customer"},
#     {"name": "Doom Slayer", "phone": "222-333-4444", "email": "doom@slayer.org", "company": "Hell Busters", "category": "Vendor"},
#     {"name": "Aloy", "phone": "333-444-5555", "email": "aloy@horizontech.com", "company": "Gaia AI", "category": "Partner"},
#     {"name": "Jin Sakai", "phone": "444-555-6666", "email": "jin@ghostofjapan.jp", "company": "Samurai House", "category": "Employee"},
#     {"name": "Trevor Philips", "phone": "555-666-7777", "email": "trevor@tpe.com", "company": "TP Enterprises", "category": "VIP"},
#     {"name": "Sonic", "phone": "777-888-9999", "email": "sonic@segalabs.com", "company": "Sega Speed Co.", "category": "Customer"}
# ]

# async def seed_data():
#     async with SessionLocal() as db:
#         for entry in video_game_contacts:
#             contact = ContactCreate(**entry)
#             await create_contact(db, contact)
#         print("Seeding complete")

# if __name__ == "__main__":
#     asyncio.run(seed_data())
