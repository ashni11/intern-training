from database import SessionLocal
from model import Post

db = SessionLocal()

post1 = Post(
    title="Advanced SQL",
    content="Learning SQL",
    user_id=6
)

post2 = Post(
    title="FastAPI CRUD",
    content="Building APIs",
    user_id=6
)

db.add_all([post1, post2])
db.commit()

print("Posts Added!")