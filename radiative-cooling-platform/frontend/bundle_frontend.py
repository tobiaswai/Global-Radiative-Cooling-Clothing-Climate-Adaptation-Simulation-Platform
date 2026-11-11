import os
import glob
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

# 遞迴搜尋 src 目錄下的原始碼檔案，排除不需要的副檔名與 artifacts
EXCLUDE_EXTS = {'.snap', '.png', '.jpg', '.svg', '.ico', '.woff', '.woff2'}
src_files = []

if os.path.isdir("src"):
    for root, dirs, files in os.walk("src"):
        # 排除 node_modules 或 .next
        if 'node_modules' in root.split(os.sep) or '.next' in root.split(os.sep):
            continue
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext not in EXCLUDE_EXTS:
                full_path = Path(root) / file
                # 以相對 src/ 的格式紀錄，或保持與 find 一致
                rel_path = full_path.as_posix()
                src_files.append(rel_path)
    src_files.sort()

def lang_for(filename):
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

# 收集 public/ 底下的檔案名稱
public_files = []
if os.path.isdir("public"):
    for root, dirs, files in os.walk("public"):
        for file in files:
            public_files.append(Path(root, file).as_posix())
    public_files.sort()

# 開始寫入輸出檔
total_files_count = 0

with open(OUT, 'w', encoding='utf-8') as out:
    out.write("# Frontend Source Bundle (`frontend/` - excluding node_modules, .next, public assets)\n\n")
    out.write("## Directory Structure\n")
    out.write("```text\n")
    
    # 寫入 INCLUDE_FILES 與 src_files 加上 frontend/ 前綴
    for f in INCLUDE_FILES + src_files:
        out.write(f"frontend/{f}\n")
    
    # 寫入 public/ 檔案
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
        # 預防路徑層級不同，也支援從根目錄直接抓取
        "../.stage-3-api-contract-before.json",
        "../.stage-3-api-contract-after.json"
    ]
    
    handled_contracts = set()
    for c in contract_paths:
        if os.path.isfile(c) and c not in handled_contracts:
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