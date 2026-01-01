from pydantic import BaseModel, Field
from typing import List

class ChatMessage(BaseModel):
    role: str = Field(..., description="ロール ('user' または 'model')")
    content: str = Field(..., description="メッセージ本文")

class ChatRequest(BaseModel):
    message: str = Field(..., description="ユーザーからのメッセージ")
    history: List[ChatMessage] = Field(default=[], description="会話履歴")
    strength_level: int = Field(default=1, description="壁打ち強度 (1: 受容・共感, 2: 論理・分析, 3: 鬼軍曹)")

class ChatResponse(BaseModel):
    response: str = Field(..., description="AIからの応答")
    emotion: str = Field(default="neutral", description="AIの感情ステータス (neutral, happy, thinking, serious, warm)")
