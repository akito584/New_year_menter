# フロントエンド用 Dockerfile
FROM node:20-alpine

WORKDIR /app

# 依存関係のインストール
COPY package*.json ./
RUN npm install

# ソースコードのコピー
COPY . .

# Next.jsの開発サーバー起動
# ホストからのアクセスを許可するためにホスト指定が必要な場合があるが、
# npm run dev自体がデフォルトで外部アクセスを受け付けない場合があるのでコマンドで指定
CMD ["npm", "run", "dev", "--", "-H", "0.0.0.0"]
