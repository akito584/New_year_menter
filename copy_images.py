import shutil
import os

# 生成された画像の元パス (ユーザーの環境に合わせて推測)
# エージェントが生成した際のパスログを元に記述
source_dir = r"C:\Users\akkki\.gemini\antigravity\brain\a1bddcea-6712-4bd0-a353-732b8aa68476"
dest_dir = r"c:\Users\akkki\programing_outcome\Newyear_menter\frontend\public\characters"

# ファイル名のマッピング (元ファイル名: コピー先ファイル名リスト)
# ※ エージェントが生成した際のタイムスタンプ付きファイル名を指定します
mapping = {
    "mofu_smile_1767239721798.png": ["warm_smile.png", "warm_base.png"],
    "mofu_thinking_1767239740196.png": ["thinking.png", "logical_base.png", "logical_explain.png"],
    "mofu_angry_1767239761026.png": ["strict_anger.png", "strict_base.png", "error.png"]
}

def copy_images():
    if not os.path.exists(dest_dir):
        print(f"Creating directory: {dest_dir}")
        os.makedirs(dest_dir)

    print(f"Searching for images in: {source_dir}")
    
    # 元フォルダ内のファイルをリストアップして、最も近いファイルを探す
    # (ファイル名が完全に一致しない場合に備えて、プレフィックスでマッチング)
    available_files = os.listdir(source_dir)
    
    for prefix, tasks in mapping.items():
        # mofu_smile などのプレフィックス部分を取得
        base_prefix = prefix.rsplit('_', 1)[0]
        
        # 実際にフォルダにあるファイルを探す
        found_file = None
        for f in available_files:
            if f.startswith(base_prefix) and f.endswith(".png"):
                found_file = f
                break # 最初に見つかったものを採用
        
        if found_file:
            src_path = os.path.join(source_dir, found_file)
            for target_name in tasks:
                dest_path = os.path.join(dest_dir, target_name)
                try:
                    shutil.copy2(src_path, dest_path)
                    print(f"SUCCESS: Copied {found_file} to {target_name}")
                except Exception as e:
                    print(f"ERROR: Failed to copy to {target_name}. Reason: {e}")
        else:
            print(f"WARNING: Source image starting with '{base_prefix}' not found in {source_dir}")

if __name__ == "__main__":
    copy_images()
