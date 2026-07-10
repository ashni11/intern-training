import os
from dotenv import load_dotenv
load_dotenv()
class Settings:
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:ASHNI@localhost:5432/FullStack_db"
    )
    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "my_super_secret_jwt_key"
    )

    ALGORITHM = os.getenv(
        "ALGORITHM",
        "HS256"
    )

    ACCESS_TOKEN_EXPIRE_MINUTES = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)
    )
    
settings = Settings()