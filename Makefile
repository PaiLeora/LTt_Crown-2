
👑 KONTRIBUTOR
Ltt Crown — Developer & Maintainer
📌 About
Tools All-In-One dengan berbagai fitur canggih untuk Termux. """ try: with open(readme_path, 'w', encoding='utf-8') as f: f.write(new_readme) print(f" ✓ REBRAND README.md") except Exception as e: print(f" ✗ GAGAL tulis README.md: {e}")

def write_new_makefile(): """Tulis ulang Makefile dengan branding Ltt Crown.""" makefile_path = os.path.join(REPO_DIR, 'Makefile') new_makefile = """help: @clear @echo "██╗░░░░░████████╗████████╗" @echo "██║░░░░░╚══██╔══╝╚══██╔══╝" @echo "██║░░░░░░░░██║░░░░░░██║░░░" @echo "██║░░░░░░░░██║░░░░░░██║░░░" @echo "███████╗░░░██║░░░░░░██║░░░" @echo "╚══════╝░░░╚═╝░░░░░░╚═╝░░░" @echo @echo "┌─[ Bantuan Perintah ]" @echo "│" @echo "├─ make install" @echo "├─ make tutor" @echo "└─ make run"

install: @clear @echo "██╗░░░░░████████╗████████╗" @echo "██║░░░░░╚══██╔══╝╚══██╔══╝" @echo "██║░░░░░░░░██║░░░░░░██║░░░" @echo "██║░░░░░░░░██║░░░░░░██║░░░" @echo "███████╗░░░██║░░░░░░██║░░░" @echo "╚══════╝░░░╚═╝░░░░░░╚═╝░░░" @echo @echo "[ ! ] Memulai instalasi semua dependensi..." @pkg update -y && pkg upgrade -y @pkg install python python3 nala git -y @pkg install coreutils ncurses-utils which python-pip nodejs bc ruby -y @pkg install termux-api @pkg install sox @pkg install cloudflared -y @pkg install openssl-tool xz-utils bzip2 boxes jq cowsay toilet -y @pkg install php -y @gem install lolcat @npm install -g bash-obfuscate @gem install lolcat @pip install rich @pip install rich-cli @pip install yt-dlp @echo "[ ✔ ] Semua paket berhasil diinstal!"

tutor: @clear @echo "██╗░░░░░████████╗████████╗" @echo "██║░░░░░╚══██╔══╝╚══██╔══╝" @echo "██║░░░░░░░░██║░░░░░░██║░░░" @echo "██║░░░░░░░░██║░░░░░░██║░░░" @echo "███████╗░░░██║░░░░░░██║░░░" @echo "╚══════╝░░░╚═╝░░░░░░╚═╝░░░" @echo @echo "[ INFO ] Tutorial: https://youtube.com/@LttCrown"

run: @clear @echo "██╗░░░░░████████╗████████╗" @echo "██║░░░░░╚══██╔══╝╚══██╔══╝" @echo "██║░░░░░░░░██║░░░░░░██║░░░" @echo "██║░░░░░░░░██║░░░░░░██║░░░" @echo "███████╗░░░██║░░░░░░██║░░░" @echo "╚══════╝░░░╚═╝░░░░░░╚═╝░░░" @echo @echo "[ ! ] RUNNING LTT CROWN TOOLS..." @bash 
		bash LttCrown_Dick.sh
