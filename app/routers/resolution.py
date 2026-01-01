from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.resolution import ResolutionCreate, ResolutionResponse
from app.services.resolution_service import ResolutionService

# ルーターの定義
router = APIRouter(
    prefix="/save",
    tags=["Resolution"]
)

# 依存性注入(DI)のための関数
# これが「Serviceを提供する係」です。
# 将来的にServiceの初期化が複雑になっても、ここを修正するだけで済みます。
def get_resolution_service() -> ResolutionService:
    return ResolutionService()

@router.post("/", response_model=ResolutionResponse)
def save_resolution(
    request: ResolutionCreate, 
    db: Session = Depends(get_db),
    # ★ ここが修正ポイント ★
    # FastAPIのDIシステム(Depends)を使います。
    # 「この関数を実行する前に get_resolution_service を呼んで、その結果を service に入れてね」という意味です。
    service: ResolutionService = Depends(get_resolution_service)
):
    """
    確定した抱負とNext Actionをデータベースに保存します。
    """
    # グローバルなインスタンスではなく、注入された service インスタンスを使います
    return service.create_resolution(db, request)
