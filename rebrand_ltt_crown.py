#!/usr/bin/env python3
"""
rebrand_ltt_crown.py — Rebrand FluxyCrownTools → Ltt Crown (Leonore Tech Team)
Author  : Pai Leora
Company : Leonore Tech Team
Usage   : python3 rebrand_ltt_crown.py

Deskripsi:
  - Mengganti semua string "FluxyCrownTools", "Fluxy", "Danxy", "Byexe", dll
    menjadi "LttCrown", "Ltt", "Leonore Tech Team", dll.
  - Tidak ada fungsionalitas yang dihapus/diblokir — semua fitur tetap utuh.
  - data.json tetap karena murni data geografis.
"""

import os
import re

# =============================================================
# 1.  KONFIGURASI
# =============================================================
REPO_DIR = os.path.dirname(os.path.abspath(__file__))

# Mapping rebrand — urut dari spesifik ke umum
REPLACEMENTS = [
    # Produk / folder references
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
    # Case variants
    (r'fluxycrown',       'lttcrown'),
    (r'fluxytools',       'ltttools'),
    (r'fluxy',            'ltt'),
    # Old author branding → Leonore Tech Team
    (r'DANXY TOOLS',      'LTT CROWN'),
    (r'TOOLS BY DANXY OFFICIAL', 'TOOLS BY LEONORE TECH TEAM'),
    (r'TOOLS V8\.4',      'LTT CROWN V1.0'),
    (r'MENU LOGIN TOOLS V8\.4', 'MENU LOGIN LTT CROWN'),
    (r'REGRISTRASI & LOGAIN TOOLS DANXY', 'REGISTRASI & LOGIN LTT CROWN'),
    (r'WELCOME TO REGRISTRASI & LOGAIN TOOLS DANXY', 'WELCOME TO REGISTRASI & LOGIN LTT CROWN'),
    (r'Danxy',            'LttCrown'),
    (r'danxy',            'lttcrown'),
    (r'DanxyBot',         'LttCrownBot'),
    (r'Qwela\.38',        'LeonoreTechTeam'),
    # Author references
    (r'DAEMONTECHX',      'LEONORE TECH TEAM'),
    (r'DaemonTechX',      'LeonoreTechTeam'),
    (r'ByexeOfficial999', 'LeonoreTechTeam'),
    (r'ByexeOfficial',    'LeonoreTechTeam'),
    (r'Byexe',            'LeonoreTechTeam'),
    # YouTube channel
    (r'www\.youtube\.com/@ByexeOfficial', 'www.youtube.com/@LeonoreTechTeam'),
    (r'youtube\.com/@ByexeOfficial',      'youtube.com/@LeonoreTechTeam'),
    # Teks di main script
    (r'===== FluxyTools =====', '===== Ltt Tools ====='),
]

SKIP_FILES = {'.git', '.gitignore', os.path.basename(__file__)}

# =============================================================
# 2.  HELPER FUNCTIONS
# =============================================================

def is_text_file(filepath: str) -> bool:
    ext = os.path.splitext(filepath)[1].lower()
    text_exts = {'.sh', '.md', '.json', '.txt', '.py', '.cfg', '.conf', '.yml', '.yaml', '.ini', '.xml'}
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
    # Lewati file yang di-skip
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


def main():
    print("""
╔═══════════════════════════════════════════╗
║   LTT CROWN — REBRAND TOOL               ║
║   FluxyCrownTools → Ltt Crown            ║
║   Leonore Tech Team                      ║
╚═══════════════════════════════════════════╝
    """)
    print(f"Target repo : {REPO_DIR}\n")

    print(">>> MEREBRAND STRING DI SELURUH FILE...")
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
    ╔═══════════════════════════════════════════╗
    ║  LANGKAH SELANJUTNYA:                     ║
    ║                                           ║
    ║  1. git init (folder baru)                ║
    ║  2. git add .                             ║
    ║  3. git commit -m "Initial Ltt Crown"     ║
    ║  4. Buat repo di GitHub > LttCrown        ║
    ║  5. git remote add origin <url-baru>      ║
    ║  6. git push -u origin main               ║
    ╚═══════════════════════════════════════════╝
    """)


if __name__ == '__main__':
    main()
