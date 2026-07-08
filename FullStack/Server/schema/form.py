from pydantic import BaseModel
class UserCreateSchema(BaseModel):
    username: str
    dob: str
    phoneNumber: str