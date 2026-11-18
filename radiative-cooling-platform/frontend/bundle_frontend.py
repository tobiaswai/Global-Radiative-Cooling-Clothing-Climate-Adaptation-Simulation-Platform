import os
from pathlib import Path

OUT = "frontend_full.md"

# 固定的設定與根檔案
INCLUDE_FILES = [
    "package.json", "tsconfig.json", "next.config.ts", "eslint.config.mjs",
    "AGENTS.md", "CLAUDE.md", "README.md"
]

# 檢查選用的環境變數範例檔
for f in [".env.example", ".env.local.example"]:
    if os.path.isfile(f):
        INCLUDE_FILES.append(f)

# ========== 1. 排除規則 ==========
EXCLUDE_DIRS = {
    'node_modules', '.next', '.git',
    '__tests__', 'tests', 'test', '__mocks__', 'mocks',
    'stories', '.storybook', 'fixtures', 'coverage',
    'generated',
}

EXCLUDE_EXTS = {
    '.snap', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico',
    '.woff', '.woff2', '.ttf', '.eot',
    # 新增
    '.map',
    # '.d.ts',   # 若需要型別宣告檔可把這行註解掉
    '.log',
}

EXCLUDE_FILE_PATTERNS = (
    '.test.', '.spec.', '.stories.',
    'mock', 'fixture', 'dummy',
)

# ========== 2. 單一檔案大小限制 ==========
MAX_FILE_SIZE = 120 * 1024  # 120 KB，不想限制可改成 None

def should_exclude_file(filename: str) -> bool:
    """根據副檔名與檔名 pattern 判斷是否排除"""
    ext = os.path.splitext(filename)[1].lower()
    if ext in EXCLUDE_EXTS:
        return True
    lower_name = filename.lower()
    return any(p in lower_name for p in EXCLUDE_FILE_PATTERNS)

src_files = []

if os.path.isdir("src"):
    for root, dirs, files in os.walk("src"):
        # 原地過濾目錄，避免進入不需要的資料夾
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith('.')]

        # 額外保險：如果路徑中已包含排除目錄就跳過
        if any(ex in root.split(os.sep) for ex in EXCLUDE_DIRS):
            continue

        for file in files:
            if should_exclude_file(file):
                continue

            full_path = Path(root) / file

            # 檔案大小限制
            if MAX_FILE_SIZE is not None:
                try:
                    if full_path.stat().st_size > MAX_FILE_SIZE:
                        print(f"  ⏭ 跳過過大檔案: {full_path.as_posix()} "
                              f"({full_path.stat().st_size / 1024:.1f} KB)")
                        continue
                except OSError:
                    continue

            rel_path = full_path.as_posix()
            src_files.append(rel_path)

    src_files.sort()

def lang_for(filename: str) -> str:
    if filename.endswith('.ts'):
        return 'typescript'
    elif filename.endswith('.tsx'):
        return 'tsx'
    elif filename.endswith(('.js', '.mjs', '.cjs')):
        return 'javascript'
    elif filename.endswith('.json'):
        return 'json'
    elif filename.endswith('.md'):
        return 'markdown'
    elif filename.endswith('.css'):
        return 'css'
    else:
        return 'text'

# 收集 public/ 底下的檔案名稱（只列名稱，不寫內容）
public_files = []
if os.path.isdir("public"):
    for root, dirs, files in os.walk("public"):
        for file in files:
            public_files.append(Path(root, file).as_posix())
    public_files.sort()

# 開始寫入輸出檔
total_files_count = 0

with open(OUT, 'w', encoding='utf-8') as out:
    out.write("# Frontend Source Bundle (`frontend/` - excluding node_modules, .next, tests, stories, public assets)\n\n")
    out.write("## Directory Structure\n")
    out.write("```text\n")

    # 寫入 INCLUDE_FILES 與 src_files
    for f in INCLUDE_FILES + src_files:
        out.write(f"frontend/{f}\n")

    # 寫入 public/ 檔案（僅名稱）
    out.write("\n# public/ (names only)\n")
    for f in public_files:
        out.write(f"frontend/{f}\n")

    out.write("```\n\n---\n\n## Source Code Files\n\n")

    # 寫入各個程式碼檔案內容
    all_source_targets = [f for f in INCLUDE_FILES + src_files if os.path.isfile(f)]
    total_files_count = len(all_source_targets)

    for f in all_source_targets:
        out.write(f"### File: `frontend/{f}`\n")
        out.write(f"```{lang_for(f)}\n")
        try:
            with open(f, 'r', encoding='utf-8', errors='ignore') as infile:
                out.write(infile.read())
        except Exception as e:
            out.write(f"// Unable to read file: {e}\n")
        out.write("\n```\n\n")

    # 檢查並引入上層目錄的 OpenAPI 契約快照
    contract_paths = [
        "../../.stage-3-api-contract-before.json",
        "../../.stage-3-api-contract-after.json",
        "../.stage-3-api-contract-before.json",
        "../.stage-3-api-contract-after.json"
    ]

    handled_contracts = set()
    for c in contract_paths:
        if os.path.isfile(c) and c not in handled_contracts:
            # 也套用大小限制
            if MAX_FILE_SIZE is not None and os.path.getsize(c) > MAX_FILE_SIZE:
                print(f"  ⏭ 跳過過大契約檔: {c}")
                continue

            handled_contracts.add(c)
            base_name = os.path.basename(c)
            out.write(f"### File: `{base_name}`\n")
            out.write("```json\n")
            try:
                with open(c, 'r', encoding='utf-8', errors='ignore') as infile:
                    out.write(infile.read())
            except Exception as e:
                out.write(f"// Unable to read contract: {e}\n")
            out.write("\n```\n\n")
            total_files_count += 1

# 計算檔案大小與統計
file_size = os.path.getsize(OUT)
print(f"wrote {OUT} ({file_size} bytes, {total_files_count} files)")