# Pustaka Rich
from rich import print  # Warna Teks
from rich.progress import track  # Progress Bar
import time  # Time Progress Bar
from rich.panel import Panel  # Menyorot Teks
from rich.console import Console  # Menyorot Teks
from rich.prompt import Prompt # Input interaktif

# Fungsi
def progressBar():
    for _ in track(range(2), description="[bold green]Memuat..."):
        time.sleep(0.25)
    print("")

def menuUtama():
    console.print(Panel("Menu Utama", style="bold bright_white", width=14))
    console.print("[bold bright_white]1. Yo-Managements[/bold bright_white]")
    print("[bold bright_white]2. Perhitungan Tabungan[/bold bright_white]")
    print("[bold bright_white]3. Bantuan Pengguna[/bold bright_white]")
    print("[bold bright_yellow]4. Keluar dari aplikasi[/bold bright_yellow]")
    pilihan = Prompt.ask("[bold bright_green]Pilih menu yang ingin Anda akses (1-3), atau pilih 4 untuk keluar[/bold bright_green]", choices=["1", "2", "3", "4"])
    return pilihan

def fiturSatu():
    console.print(Panel("Yo-Managements", style="bold bright_cyan", width=18))
    kembali = Prompt.ask("[bold bright_blue]Ketik 'kembali' untuk kembali ke menu utama[/bold bright_blue]", choices=["kembali"])
    if kembali.lower() == "kembali":
        progressBar()
        return True
    return False

def fiturDua():
    console.print(Panel("Perhitungan Tabungan", style="bold bright_cyan", width=24))
    kembali = Prompt.ask("[bold bright_blue]Ketik 'kembali' untuk kembali ke menu utama[/bold bright_blue]", choices=["kembali"])
    if kembali.lower() == "kembali":
        progressBar()
        return True
    return False

def fiturTiga():
    console.print(Panel("Bantuan Pengguna", style="bold bright_cyan", width=20))
    kembali = Prompt.ask("[bold bright_blue]Ketik 'kembali' untuk kembali ke menu utama[/bold bright_blue]", choices=["kembali"])
    if kembali.lower() == "kembali":
        progressBar()
        return True
    return False

# Inisialisasi objek Console dari pustaka Rich
console = Console()

""" 
Halaman Utama | Ayona 
Versi 0.1
"""""
greeting = "Selamat datang di aplikasi Ayona!"
console.print(Panel(f"\n\t\t{greeting}\t\t\n", title="Sistem Ayona", title_align="right", style="bold bright_blue", width=64))
progressBar()

# Program utama
def main():
    while True:
        pilihan = menuUtama()

        if pilihan == "1":
            progressBar()
            while True:
                if fiturSatu():
                    break # Kembali ke menu utama      
        elif pilihan == "2":
            progressBar()
            while True:
                if fiturDua():
                    break # Kembali ke menu utama 
        elif pilihan == "3":
            progressBar()
            while True:
                if fiturTiga():
                    break # Kembali ke menu utama
        elif pilihan == "4":
            progressBar()  
            console.print("[bold bright_red](Keluar dari aplikasi)[/bold bright_red]")
            return False

"""
if __name__ == "__main__":
Memeriksa apakah skrip sedang dijalankan langsung (bukan diimpor).
Jika benar, Python akan memanggil fungsi main().
Jika salah, Python tidak akan memanggil fungsi main().
"""
if __name__ == "__main__":
    main()