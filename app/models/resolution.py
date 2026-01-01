from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Resolution(Base):
    __tablename__ = "resolutions"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)  # 抱負、目標
    next_action = Column(Text, nullable=False)  # 具体的な行動アクション
    created_at = Column(DateTime(timezone=True), server_default=func.now())
