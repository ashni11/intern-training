from database import SessionLocal
from model import User

db = SessionLocal()
user = db.query(User).filter(User.id==6).first ()
user.name = "trishala"
db.commit()
print("updated successfull")
