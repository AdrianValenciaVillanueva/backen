from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime


class Task(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1, max_length=500)
    user_id: Optional[str]
    team_id: str = Field(..., min_length=1)  # Nuevo campo para el código del equipo
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    deadline: Optional[datetime]
    status: str = Field(default="pending", pattern="^(pending|in_progress|completed)$")

    @validator('title')
    def title_must_not_be_empty(cls, v):
        assert v.strip(), 'Title must not be empty'
        return v

    @validator('description')
    def description_must_not_be_empty(cls, v):
        assert v.strip(), 'Description must not be empty'
        return v

    @validator('deadline')
    def deadline_must_be_future(cls, v, values):
        if v and 'created_at' in values and v < values['created_at']:
            raise ValueError('Deadline must be in the future')
        return v
    