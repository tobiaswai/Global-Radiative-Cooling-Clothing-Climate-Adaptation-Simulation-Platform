import os

# 要打包的目標目錄（可同時打多個）
TARGET_DIRS = [
    "backend/tests",
    "backend/docs",
]

# 1. 忽略的子目錄名稱
IGNORE_DIRS = {
    '__pycache__', '.pytest_cache', '.mypy_cache', '.numba_cache',
    '.venv', 'venv', 'dist', 'build', 'htmlcov',
    'node_modules', '_build', 'site',
}

# 2. 忽略的大型檔案、二進位檔與編譯檔
IGNORE_EXTS = {
    '.png', '.jpg', '.jpeg', '.gif', '.ico', '.pdf',
    '.pyc', '.pyo', '.pyd', '.zip', '.tar', '.gz',
    '.db', '.sqlite', '.sqlite3', '.so', '.dll', '.exe', '.csv',
    '.dat', '.dir', '.bak', '.log', '.tmp', '.cache',
    '.pkl', '.pickle', '.jsonl', '.parquet',
}

# 3. 忽略敏感與雜項檔案
IGNORE_FILES = {
    '.env', '.env.local',
    '.coverage', 'coverage.xml',
}

OUTPUT_FILE = "tests_docs_full.md"

# 單一檔案大小上限；設為 None 可關閉
MAX_FILE_SIZE = 300 * 1024  # 300 KB


def collect_files():
    files_to_pack = []
    missing = []

    for target in TARGET_DIRS:
        if not os.path.exists(target):
            missing.append(target)
            continue

        print(f"🔍 掃描 `{target}` ...")

        for root, dirs, files in os.walk(target):
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS and not d.startswith('.')]

            for file in files:
                if file in IGNORE_FILES or file.startswith('.'):
                    continue

                _, ext = os.path.splitext(file)
                if ext.lower() in IGNORE_EXTS:
                    continue

                full_path = os.path.join(root, file)

                if MAX_FILE_SIZE is not None:
                    try:
                        size = os.path.getsize(full_path)
                        if size > MAX_FILE_SIZE:
                            print(f"  ⏭ 跳過過大檔案: {full_path} ({size / 1024:.1f} KB)")
                            continue
                    except OSError:
                        continue

                rel_path = os.path.relpath(full_path, '.').replace('\\', '/')
                files_to_pack.append(rel_path)

    if missing:
        print(f"⚠️ 找不到目錄：{', '.join(missing)}")

    return sorted(files_to_pack)


def detect_lang(ext: str) -> str:
    mapping = {
        '.py': 'python',
        '.json': 'json',
        '.yml': 'yaml',
        '.yaml': 'yaml',
        '.toml': 'toml',
        '.md': 'markdown',
        '.txt': 'text',
        '.rst': 'rst',
        '.ini': 'ini',
        '.cfg': 'ini',
        '.sh': 'bash',
        '.html': 'html',
        '.css': 'css',
    }
    return mapping.get(ext.lower(), '')


def main():
    matched_files = collect_files()

    if not matched_files:
        print("⚠️ 未找到可打包的檔案。")
        return

    print(f"📦 找到 {len(matched_files)} 個檔案，開始打包成 Markdown...")

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as out_f:
        targets = ", ".join(f"`{t}/`" for t in TARGET_DIRS)
        out_f.write(f"# Tests & Docs Source ({targets})\n\n")

        out_f.write("## Directory Structure\n```text\n")
        for file_path in matched_files:
            out_f.write(f"{file_path}\n")
        out_f.write("```\n\n---\n\n## Source Code Files\n\n")

        for file_path in matched_files:
            out_f.write(f"### File: `{file_path}`\n")
            ext = os.path.splitext(file_path)[1]
            lang = detect_lang(ext)

            out_f.write(f"```{lang}\n")
            try:
                with open(file_path, 'r', encoding='utf-8') as in_f:
                    out_f.write(in_f.read())
            except Exception as e:
                out_f.write(f"// Unable to read file: {e}\n")
            out_f.write("\n```\n\n")

    print(f"✅ 打包成功！內容已寫入：{OUTPUT_FILE}")
    print(f"   共打包 {len(matched_files)} 個檔案")


if __name__ == '__main__':
    main()