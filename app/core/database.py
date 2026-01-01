import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 【修正ポイント】環境変数 DATABASE_URL を読み込む
# 第2引数の "postgresql://..." はローカル開発用のフォールバックです
# プロジェクトの既存設定に合わせてDB名を resolution_mate にしています
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/resolution_mate")

# Neon/Renderを使う場合、URLの先頭が "postgres://" だとSQLAlchemyが嫌がることがあるため修正
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# エンジン作成
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
