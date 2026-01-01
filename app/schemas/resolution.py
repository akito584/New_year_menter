from pydantic import BaseModel, Field
from datetime import datetime

class ResolutionCreate(BaseModel):
    content: str = Field(..., description="抱負・目標の内容")
    next_action: str = Field(..., description="具体的なNext Action")

class ResolutionResponse(ResolutionCreate):
    id: int = Field(..., description="登録ID")
    created_at: datetime = Field(..., description="作成日時")

    class Config:
        from_attributes = True
