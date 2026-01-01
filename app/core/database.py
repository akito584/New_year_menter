from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# PostgreSQL接続エンジン
engine = create_engine(settings.DATABASE_URL)

# セッションローカルクラス
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ベースモデルクラス
Base = declarative_base()

# 依存性注入用関数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
