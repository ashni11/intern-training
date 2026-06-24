from database import Base, engine
from model import User, Post

Base.metadata.create_all(bind=engine)

print("Tables Created Successfully!")