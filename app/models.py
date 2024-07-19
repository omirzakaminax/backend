from bson import ObjectId
from pydantic import BaseModel, Field, EmailStr


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v, values, **kwargs):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, field_schema):
        field_schema.update(type="string")


class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    email: EmailStr
    password: str
    full_name: str
    is_active: bool = True

    class Config:
        populate_by_name = True
        json_encoders = {ObjectId: str}


class Article(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str
    content: str
    author: str

    class Config:
        orm_mode = True
        json_encoders = {ObjectId: str}
