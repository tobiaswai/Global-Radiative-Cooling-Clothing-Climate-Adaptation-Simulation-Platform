import os

# 指定要打包的目標目錄
TARGET_DIR = "backend"

# 1. 忽略的子目錄名稱（包含 data 目錄、快取、虛擬環境等）
IGNORE_DIRS = {
    'data', '__pycache__', '.pytest_cache', '.venv', 'venv', 
    'dist', 'build', '.mypy_cache', '.coverage', 'htmlcov'
}

# 2. 忽略的大型檔案、二進位檔與編譯檔
IGNORE_EXTS = {
    '.png', '.jpg', '.jpeg', '.gif', '.ico', '.pdf', 
    '.pyc', '.pyo', '.pyd', '.zip', '.tar', '.gz', 
    '.db', '.sqlite', '.sqlite3', '.so', '.dll', '.exe', '.csv'
}

# 3. 忽略敏感與大型 Lock 檔案
IGNORE_FILES = {
    '.env', '.env.local', 'poetry.lock', 'Pipfile.lock', 'requirements.txt.lock'
}

OUTPUT_FILE = "backend_full.md"

def collect_backend_files():
    files_to_pack = []
    
    if not os.path.exists(TARGET_DIR):
        print(f"⚠️ 錯誤：找不到 '{TARGET_DIR}' 資料夾！請確認腳本是否放置於專案根目錄。")
        return []

    print(f"🔍 開始掃描 `{TARGET_DIR}` 目錄（已排除 `data/` 目錄）...")
    
    for root, dirs, files in os.walk(TARGET_DIR):
        # 原地過濾掉需要忽略的資料夾（如 data, __pycache__ 等，避免 os.walk 進入）
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS and not d.startswith('.')]
        
        for file in files:
            if file in IGNORE_FILES or file.startswith('.'):
                continue
                
            _, ext = os.path.splitext(file)
            if ext.lower() in IGNORE_EXTS:
                continue
                
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, '.').replace('\\', '/')
            files_to_pack.append(rel_path)
            
    return sorted(files_to_pack)

def main():
    matched_files = collect_backend_files()
    
    if not matched_files:
        print("⚠️ 未找到可打包的檔案。")
        return

    print(f"📦 找到 {len(matched_files)} 個後端檔案，開始打包成 Markdown...")
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as out_f:
        out_f.write(f"# Complete Backend Source Code (`{TARGET_DIR}/` - Excluding `data/`)\n\n")
        
        # 寫入 Backend 樹狀目錄架構
        out_f.write("## Directory Structure\n```text\n")
        for file_path in matched_files:
            out_f.write(f"{file_path}\n")
        out_f.write("```\n\n---\n\n## Source Code Files\n\n")
        
        # 逐一寫入檔案內容
        for file_path in matched_files:
            out_f.write(f"### File: `{file_path}`\n")
            
            ext = os.path.splitext(file_path)[1].lower()
            lang = "python" if ext == ".py" else (
                "json" if ext == ".json" else (
                    "yaml" if ext in ['.yml', '.yaml'] else (
                        "toml" if ext == ".toml" else ""
                    )
                )
            )
            
            out_f.write(f"```{lang}\n")
            try:
                with open(file_path, 'r', encoding='utf-8') as in_f:
                    out_f.write(in_f.read())
            except Exception as e:
                out_f.write(f"// Unable to read file: {e}\n")
            out_f.write("\n```\n\n")

    print(f"✅ 打包成功！後端完整程式碼已寫入：{OUTPUT_FILE}")

if __name__ == '__main__':
    main()