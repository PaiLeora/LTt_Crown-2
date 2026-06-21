#!/usr/bin/env python3
"""
rebrand_final.py — Rebrand TOTAL ke Leonore Tech Team
Author  : Pai Leora
Company : Leonore Tech Team
Usage   : python3 rebrand_ltt_crown.py

FITUR:
  ✅ Rename file
  ✅ Rebrand semua string
  ✅ Ganti token & email (isi manual di LTT_CONFIG)
  ✅ Rebrand Makefile
"""

import os
import re
import shutil

REPO_DIR = os.path.dirname(os.path.abspath(__file__))

# =============================================================
# 🔧 ISI TOKEN & EMAIL LTT KAMU DI SINI
# =============================================================
LTT_CONFIG = {
    "BOT_TOKEN": "8471359519:AAFhGmhK0qzAC-lQa_WozLKfaUKyuuryDCU",  # ← GANTI INI
    "CHAT_ID": "7380101464",                                        # ← GANTI INI
    "SMTP_EMAIL": "leonoerenexus@gmail.com",                        # ← GANTI INI
    "SMTP_PASS": "BANDUNG889",                               # ← GANTI INI
}

# =============================================================
# 1. DAFTAR FILE YANG DI-RENAME
# =============================================================
FILE_RENAMES = [
    ('Danxy_Dick.sh', 'LttCrown.sh'),
    ('Database_Danxy_dick.sh', 'Database_LttCrown.sh'),
]

# =============================================================
# 2. REBRAND STRING — SEMUA YANG MASIH DANXY/FLUXY/BYEXE
# =============================================================
REPLACEMENTS = [
    # ── NAMA FILE ──
    (r'Danxy_Dick\.sh',               'LttCrown.sh'),
    (r'Database_Danxy_dick\.sh',       'Database_LttCrown.sh'),

    # ── PRODUK ──
    (r'FluxyCrownTools',  'LttCrown'),
    (r'FluxyCrown',       'LttCrown'),
    (r'FluxyTools',       'LttTools'),
    (r'FluxyTracker',     'LttTracker'),
    (r'FluxyIG',          'LttIG'),
    (r'FluxyFF',          'LttFF'),
    (r'FluxyTT',          'LttTT'),
    (r'FluxySpin',        'LttSpin'),
    (r'FluxyTTSuntik',    'LttTTSuntik'),
    (r'FluxyPro',         'LttPro'),
    (r'FluxyInject',      'LttInject'),
    (r'Fluxy',            'Ltt'),
    (r'fluxycrown',       'lttcrown'),
    (r'fluxytools',       'ltttools'),
    (r'fluxy',            'ltt'),

    # ── DANXY → LTT / LEONORE ──
    (r'DANXY TOOLS',                   'LTT CROWN'),
    (r'TOOLS BY DANXY OFFICIAL',       'TOOLS BY LEONORE TECH TEAM'),
    (r'TOOLS V8\.4',                   'LTT CROWN V1.0'),
    (r'MENU LOGIN TOOLS V8\.4',        'MENU LOGIN LTT CROWN'),
    (r'REGRISTRASI & LOGAIN TOOLS DANXY', 'REGISTRASI & LOGIN LTT CROWN'),
    (r'WELCOME TO REGRISTRASI & LOGAIN TOOLS DANXY', 'WELCOME TO REGISTRASI & LOGIN LTT CROWN'),
    (r'KASI KE DANXY[!.]*',            'KASI KE LEONORE TECH TEAM'),
    (r'DANXY[!.]*',                    'LEONORE TECH TEAM'),
    (r'DanxyBot',                      'LttCrownBot'),
    (r'Danxy',                         'LttCrown'),
    (r'danxy',                         'lttcrown'),

    # ── BYEXE → LEONORE ──
    (r'DAEMONTECHX',                   'LEONORE TECH TEAM'),
    (r'DaemonTechX',                   'LeonoreTechTeam'),
    (r'ByexeOfficial999',              'LeonoreTechTeam'),
    (r'ByexeOfficial',                 'LeonoreTechTeam'),
    (r'Byexe',                         'LeonoreTechTeam'),
    (r'Qwela\.38',                     'LeonoreTechTeam'),

    # ── YOUTUBE ──
    (r'www\.youtube\.com/@ByexeOfficial', 'www.youtube.com/@LeonoreTechTeam'),
    (r'youtube\.com/@ByexeOfficial',      'youtube.com/@LeonoreTechTeam'),

    # ── TEKS LAIN ──
    (r'YT: LttCrownBot',                'YT: LeonoreTechTeam'),
    (r'===== FluxyTools =====',         '===== Ltt Tools ====='),

    # ── GITHUB RAW ──
    (r'raw\.githubusercontent\.com/11404d/1/refs/heads/main/LttCrownAja\.sh',
     'raw.githubusercontent.com/LeonoreTechTeam/LttCrown/main/LttCrownAja.sh'),

    # ── MAKEFILE ──
    (r'bash Danxy_Dick\.sh',            'bash LttCrown.sh'),
]

# =============================================================
# 3. TOKEN & EMAIL — REBRAND KE PUNYA LTT
# =============================================================
# Ini pattern spesifik buat ganti token & kredensial
TOKEN_REPLACEMENTS = [
    (r'BOT_TOKEN="[^"]*"', f'BOT_TOKEN="{LTT_CONFIG["BOT_TOKEN"]}"'),
    (r'CHAT_ID="[^"]*"',   f'CHAT_ID="{LTT_CONFIG["CHAT_ID"]}"'),
    (r'sender = "[^"]*"',  f'sender = "{LTT_CONFIG["SMTP_EMAIL"]}"'),
    (r'passwd = "[^"]*"',  f'passwd = "{LTT_CONFIG["SMTP_PASS"]}"'),
]

SKIP_FILES = {'.git', '.gitignore', os.path.basename(__file__), 'data.json'}
FILE_RENAME_BASENAMES = {new for _, new in FILE_RENAMES}


def is_text_file(filepath: str) -> bool:
    ext = os.path.splitext(filepath)[1].lower()
    basename = os.path.basename(filepath)
    text_exts = {'.sh', '.md', '.txt', '.py', '.cfg', '.conf', '.yml', '.yaml',
                 '.ini', '.xml', '.json', '.csv', '.env', '.gitignore'}
    if basename == 'Makefile' or ext in text_exts:
        return True
    try:
        with open(filepath, 'rb') as f:
            return b'\0' not in f.read(8192)
    except Exception:
        return False


def rebrand_content(content: str) -> str:
    # Step A: Replace branding strings
    for pattern, replacement in REPLACEMENTS:
        content = re.sub(pattern, replacement, content)
    # Step B: Replace token & credentials
    for pattern, replacement in TOKEN_REPLACEMENTS:
        content = re.sub(pattern, replacement, content)
    return content


def rebrand_file(filepath: str) -> bool:
    relpath = os.path.relpath(filepath, REPO_DIR)
    for skip in SKIP_FILES:
        if skip in relpath:
            return False
    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            original = f.read()
    except Exception as e:
        print(f"  ✗ GAGAL baca {relpath}: {e}")
        return False
    modified = rebrand_content(original)
    if modified == original:
        return False
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(modified)
        print(f"  ✓ {relpath}")
        return True
    except Exception as e:
        print(f"  ✗ GAGAL tulis {relpath}: {e}")
        return False


def rename_files():
    print("\n>>> RENAME FILE...")
    count = 0
    for old_name, new_name in FILE_RENAMES:
        old_path = os.path.join(REPO_DIR, old_name)
        new_path = os.path.join(REPO_DIR, new_name)
        if os.path.exists(old_path):
            if not os.path.exists(new_path):
                shutil.move(old_path, new_path)
                print(f"  ✓ {old_name} → {new_name}")
                count += 1
            else:
                print(f"  ~ {new_name} sudah ada, skip rename {old_name}")
        else:
            print(f"  - {old_name} tidak ditemukan, skip")
    if count == 0:
        print("  (tidak ada rename)")


def main():
    print(r"""
╔═══════════════════════════════════════════════════╗
║   REBRAND FINAL — LTT CROWN                      ║
║   Semua Danxy / Fluxy / Byexe → Leonore Tech Team║
╚═══════════════════════════════════════════════════╝
    """)
    print(f"Target repo : {REPO_DIR}\n")

    # 1. Rename file
    rename_files()

    # 2. Rebrand konten
    print("\n>>> REBRAND STRING DI SELURUH FILE...")
    count = 0
    for root, dirs, files in os.walk(REPO_DIR):
        if '.git' in dirs:
            dirs.remove('.git')
        if '.git' in root:
            continue
        for fname in files:
            fpath = os.path.join(root, fname)
            if os.path.basename(fpath) in SKIP_FILES:
                continue
            # Lewati file yang sudah di-rename (file baru belum diproses)
            if os.path.basename(fpath) in FILE_RENAME_BASENAMES:
                continue
            if is_text_file(fpath) and rebrand_file(fpath):
                count += 1

    # 3. Proses juga file yang sudah di-rename
    print("\n>>> REBRAND FILE YANG SUDAH DI-RENAME...")
    for _, new_name in FILE_RENAMES:
        new_path = os.path.join(REPO_DIR, new_name)
        if os.path.exists(new_path) and is_text_file(new_path):
            if rebrand_file(new_path):
                count += 1

    print(f"\n>>> Selesai! {count} file berhasil di-rebrand.")
    print("""
╔═══════════════════════════════════════════════════╗
║  ✅ SEMUA SUDAH LEONORE TECH TEAM               ║
║                                                  ║
║  ⚠️ PASTIKAN lo udah isi LTT_CONFIG di atas      ║
║     dengan token & email LTT punya lo sendiri!   ║
║                                                  ║
║  🚀 git add .                                    ║
║     git commit -m "Rebrand total Leonore Tech"   ║
║     git push origin main                         ║
╚═══════════════════════════════════════════════════╝
    """)


if __name__ == '__main__':
    main()
