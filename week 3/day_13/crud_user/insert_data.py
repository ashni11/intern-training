from database import SessionLocal
from model import User

db = SessionLocal()

new_user = User(
    name="Ashni",
    email="ashni_new@gmail.com"
)

db.add(new_user)
db.commit()
print("User Added Successfully!")