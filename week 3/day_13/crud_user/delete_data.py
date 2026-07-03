from database import SessionLocal
from model import User

db= SessionLocal()
user = db.query(User).filter(User.id==1).first()

if user:
    db.delete(user)
    db.commit()
    print("deleted successfully")
else:
    print("user not found")
