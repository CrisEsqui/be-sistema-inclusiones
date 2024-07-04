from pydantic import BaseModel, Field
from typing import Optional
from uuid import uuid4, UUID

class CampusSchema(BaseModel):

    campus_id: Optional[str] = Field(default_factory=lambda: str(uuid4()))
    name: str
    code: str