from database import SessionLocal
from model import User

db = SessionLocal()
users = db.query(User).all()
for user in users:
    print(user.id, user.name, user.email)