from sqlalchemy.orm import Session
from app.models.resolution import Resolution
from app.schemas.resolution import ResolutionCreate

class ResolutionService:
    """
    抱負（Resolution）に関するビジネスロジックとDB操作を担うサービスクラス。
    （Repositoryパターンの簡易版として機能）
    """
    def create_resolution(self, db: Session, resolution: ResolutionCreate):
        # SQLAlchemyモデルのインスタンス化
        db_res = Resolution(
            content=resolution.content, 
            next_action=resolution.next_action
        )
        # DBへの追加とコミット
        db.add(db_res)
        db.commit()
        # IDなどの生成された値を反映させるためにリフレッシュ
        db.refresh(db_res)
        return db_res
