# バックエンド用 Dockerfile
FROM python:3.11-slim

WORKDIR /app

# 依存関係のインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ソースコードのコピー
# 現在のディレクトリ構造上、appディレクトリをコンテナ内の /app/app に配置する
COPY app ./app
COPY .env .

# 実行コマンド
# --host 0.0.0.0 はコンテナ外からアクセスするために必須
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
