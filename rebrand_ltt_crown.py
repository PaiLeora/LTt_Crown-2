#!/usr/bin/env python3
"""
rebrand_ltt_crown_v3.py — Rebrand Total → Ltt Crown (Leonore Tech Team)
Author  : Pai Leora
Company : Leonore Tech Team
Usage   : python3 rebrand_ltt_crown_v3.py

FITUR:
  ✅ Rename file: Danxy_Dick.sh → LttCrown.sh
  ✅ Rename file: Database_Danxy_dick.sh → Database_LttCrown.sh
  ✅ Rebrand semua string: Danxy/Fluxy/Byexe/Daemon → Leonore Tech Team
  ✅ Rebrand Makefile: YouTube link & referensi file
  ✅ Skip data.json (murni data geografis)
"""

import os
import re
import shutil

REPO_DIR = os.path.dirname(os.path.abspath(__file__))

# ========== 1. RENAME FILE ==========
FILE_RENAMES = [
    ('Danxy_Dick.sh', 'LttCrown.sh'),
    ('Database_Danxy_dick.sh', 'Database_LttCrown.sh'),
]

# ========== 2. REBRAND STRING ==========
REPLACEMENTS = [
    # ── PRODUK / FOLDER ──
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

    # ── CASE VARIANTS ──
    (r'fluxycrown',       'lttcrown'),
    (r'fluxytools',       'ltttools'),
    (r'fluxy',            'ltt'),

    # ── OLD BRANDING → LEONORE TECH TEAM ──
    (r'DANXY TOOLS',      'LTT CROWN'),
    (r'TOOLS BY DANXY OFFICIAL', 'TOOLS BY LEONORE TECH TEAM'),
    (r'TOOLS V8\.4',      'LTT CROWN V1.0'),
    (r'MENU LOGIN TOOLS V8\.4', 'MENU LOGIN LTT CROWN'),
    (r'REGRISTRASI & LOGAIN TOOLS DANXY', 'REGISTRASI & LOGIN LTT CROWN'),
    (r'WELCOME TO REGRISTRASI & LOGAIN TOOLS DANXY', 'WELCOME TO REGISTRASI & LOGIN LTT CROWN'),
    (r'KASI KE DANXY',    'KASI KE LEONORE TECH TEAM'),
    (r'Danxy_Dick\.sh',   'LttCrown.sh'),
    (r'Database_Danxy_dick\.sh', 'Database_LttCrown.sh'),
    (r'DanxyBot',         'LttCrownBot'),
    (r'danxy',            'lttcrown'),
    (r'Danxy',            'LttCrown'),

    # ── BYEXE / DAEMON → LEONORE TECH TEAM ──
    (r'DAEMONTECHX',      'LEONORE TECH TEAM'),
    (r'DaemonTechX',      'LeonoreTechTeam'),
    (r'ByexeOfficial999', 'LeonoreTechTeam'),
    (r'ByexeOfficial',    'LeonoreTechTeam'),
    (r'Byexe',            'LeonoreTechTeam'),
    (r'Qwela\.38',        'LeonoreTechTeam'),

    # ── YOUTUBE CHANNEL ──
    (r'www\.youtube\.com/@ByexeOfficial', 'www.youtube.com/@LeonoreTechTeam'),
    (r'youtube\.com/@ByexeOfficial',      'youtube.com/@LeonoreTechTeam'),

    # ── TEKS DI BANNER ──
    (r'YT: LttCrownBot',  'YT: LeonoreTechTeam'),
    (r'===== FluxyTools =====', '===== Ltt Tools ====='),

    # ── GITHUB RAW LINK (11404d/1) ──
    (r'raw\.githubusercontent\.com/11404d/1/refs/heads/main/LttCrownAja\.sh',
     'raw.githubusercontent.com/LeonoreTechTeam/LttCrown/main/LttCrownAja.sh'),

    # ── REFERENSI FILE DI MAKEFILE ──
    (r'bash Danxy_Dick\.sh', 'bash LttCrown.sh'),
]

# File yang di-skip total
SKIP_FILES = {'.git', '.gitignore', os.path.basename(__file__), 'data.json'}


# =============================================================
# 3. HELPER FUNCTIONS
# =============================================================

def is_text_file(filepath: str) -> bool:
    ext = os.path.splitext(filepath)[1].lower()
    text_exts = {'.sh', '.md', '.txt', '.py', '.cfg', '.conf', '.yml', '.yaml',
                 '.ini', '.xml', '.json', '.csv', '.env', '.gitignore',
                 '.gitattributes', 'Makefile'}
    # Makefile gak punya ekstensi, cek basename
    basename = os.path.basename(filepath)
    if basename == 'Makefile':
        return True
    if ext in text_exts:
        return True
    try:
        with open(filepath, 'rb') as f:
            return b'\0' not in f.read(8192)
    except Exception:
        return False


def rebrand_content(content: str) -> str:
    for pattern, replacement in REPLACEMENTS:
        content = re.sub(pattern, replacement, content)
    return content


def rebrand_file(filepath: str) -> bool:
    relpath = os.path.relpath(filepath, REPO_DIR)
    # Skip files
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
                print(f"  ~ {new_name} sudah ada, hapus dulu {old_name}?")
        else:
            print(f"  - {old_name} tidak ditemukan, skip")
    if count == 0:
        print("  (tidak ada rename yang dilakukan)")


def main():
    banner = r"""
╔════════════════════════════════════════════════╗
║   LTT CROWN — REBRAND TOOL V3                 ║
║   Fluxy / Danxy / Byexe → Leonore Tech Team   ║
║   Include: Makefile rebrand + file rename      ║
╚════════════════════════════════════════════════╝
    """
    print(banner)
    print(f"Target repo : {REPO_DIR}\n")

    # Step 1: Rename file
    rename_files()

    # Step 2: Rebrand konten
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
            if is_text_file(fpath) and rebrand_file(fpath):
                count += 1

    print(f"\n>>> Selesai! {count} file berhasil di-rebrand.")
    print("""
╔════════════════════════════════════════════════╗
║  ⚠️  CEK MANUAL SETELAH INI:                  ║
║                                                ║
║  1. BOT_TOKEN Telegram — ganti dengan punya   ║
║     Leonore Tech Team                          ║
║                                                ║
║  2. CHAT_ID Telegram — ganti dgn chat ID lo   ║
║                                                ║
║  3. Email SMTP (spam laporan WA) — ganti      ║
║     email & app password LTT                   ║
║                                                ║
║  4. git add .                                  ║
║     git commit -m "Rebrand total Ltt Crown"   ║
║     git push origin main                       ║
╚════════════════════════════════════════════════╝
    """)


if __name__ == '__main__':
    main()
