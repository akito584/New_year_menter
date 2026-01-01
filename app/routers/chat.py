from fastapi import APIRouter, HTTPException, Depends
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import ChatService

# ルーターの定義
router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

# 依存性注入(DI)のための関数
def get_chat_service() -> ChatService:
    return ChatService()

@router.post("/", response_model=ChatResponse)
async def chat_with_ai(
    request: ChatRequest,
    # ServiceをDIで注入。これでテスト時にモックに差し替え可能になります。
    service: ChatService = Depends(get_chat_service)
):
    """
    ユーザーのメッセージを受け取り、指定された人格（Strength Level）でGeminiからの応答を返します。
    """
    try:
        response_text, emotion = await service.generate_response(
            message=request.message,
            history=request.history,
            level=request.strength_level
        )
        return ChatResponse(response=response_text, emotion=emotion)
    except Exception as e:
        # 本番環境では詳細なエラーメッセージを隠蔽すべきだが、学習用のため表示
        raise HTTPException(status_code=500, detail=f"AIエラーが発生しました: {str(e)}")
