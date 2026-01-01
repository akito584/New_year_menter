from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import chat, resolution
from app.core.database import Base, engine

# DBテーブルの作成
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Resolution Mate API")

# CORS設定 (フロントエンドからのアクセスを許可)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # 【重要】本番URLが決まるまでは "*" (すべて許可) にしておくのが一番ハマらない
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ルーターの登録
app.include_router(chat.router, prefix="/api")
app.include_router(resolution.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Resolution Mate APIへようこそ。/docs にアクセスしてAPIドキュメントを確認してください。"}

