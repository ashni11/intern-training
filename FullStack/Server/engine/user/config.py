import os
from dotenv import load_dotenv
load_dotenv()
class Settings:
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:ASHNI@localhost:5432/FullStack_db"
    )
settings = Settings()