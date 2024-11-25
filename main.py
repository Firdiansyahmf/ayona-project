import random

# Pustaka Rich
from rich.console import Console # Menyorot Teks
from rich.panel import Panel # Menyorot Teks
from rich.prompt import Prompt # Input interaktif
from rich import print # Warna Teks

# Impor fungsi fiturSatu-fiturTiga
from features1 import fiturSatu
from features2 import fiturDua
from features3 import fiturTiga

# Impor fungsi progressBar
from utils import progressBar

# Buat objek Console dari pustaka Rich
console = Console()

# Fungsi menu utama 
laci_emoji = ["ヾ(˃ᴗ˂)◞", "(ღゝ◡╹)ノ", "(⌒ ▽⌒)ﾉ", "ヾ(˃ᴗ˂)◞✨"]

def emoji():
    emoji = random.choice(laci_emoji)
    return emoji

def menuUtama():
    console.print(Panel("Menu Utama", style="bold bright_white", width=14))
    console.print("[bold bright_white]1. Yo-Managements[/bold bright_white]")
    print("[bold bright_white]2. Perhitungan Tabungan[/bold bright_white]")
    print("[bold bright_white]3. Bantuan Pengguna[/bold bright_white]")
    print("[bold bright_yellow]4. Keluar dari aplikasi[/bold bright_yellow]")
    pilihan = Prompt.ask("[bold bright_green]Pilih menu yang ingin Anda akses (1-3), atau pilih 4 untuk keluar[/bold bright_green]", choices=["1", "2", "3", "4"])
    return pilihan

"""
Fungsi main (main)
"""
def main():
    greeting = "Selamat datang di aplikasi Ayona!" + emoji()
    console.print(Panel(f"\n\t{greeting}\t\n", title="Sistem Ayona", title_align="right", style="bold bright_cyan", width=64))
    progressBar()

    while True:
        pilihan = menuUtama()

        if pilihan == "1":
            progressBar()
            while True:
                if fiturSatu():
                    break # Kembali ke menuUtama()     
        elif pilihan == "2":
            progressBar()
            while True:
                if fiturDua():
                    break # Kembali ke menuUtama()
        elif pilihan == "3":
            progressBar()
            while True:
                if fiturTiga():
                    break # Kembali ke menuUtama()
        elif pilihan == "4":
            progressBar()  
            console.print("[bold bright_red](Keluar dari aplikasi)[/bold bright_red]")
            return False

"""
Memeriksa apakah skrip sedang dijalankan langsung (bukan diimpor).
Jika benar, Python akan memanggil fungsi main().
Jika salah, Python tidak akan memanggil fungsi main().
"""
if __name__ == "__main__":
    main()