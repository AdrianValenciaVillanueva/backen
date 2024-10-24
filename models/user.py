from pydantic import BaseModel, Field, validator
from typing import Optional

class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=8)
    is_admin: bool = False
    id_team: Optional[str]

    @validator('username')
    def username_must_be_alphanumeric(cls, v):
        assert v.isalnum(), 'Username must be alphanumeric'
        return v
    
    @validator('password')
    def password_strength(cls, v):
        assert any(char.isdigit() for char in v), 'Password must contain at least one digit'
        assert any(char.isalpha() for char in v), 'Password must contain at least one letter'
        return v


class UserResponse(BaseModel):
    id: Optional[str]
    username: str
    is_admin: bool
    id_team: Optional[str]

    class Config:
        from_mode = True