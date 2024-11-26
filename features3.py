# Pustaka Rich
from rich.console import Console  # Menyorot teks
from rich.panel import Panel  # Menyorot teks
from rich.prompt import Prompt  # Input interaktif
from rich import print  # Warna teks

# Impor fungsi progressBar
from utils import progressBar

# Buat objek Console dari pustaka Rich
console = Console()

"""
Fitur 3
(main)
"""
def fiturTiga():
    # Panel
    console.print(Panel("Bantuan Pengguna", style="bold bright_cyan", width=20))

    # Input Pilihan Menu
    console.print("[bold bright_cyan]1. Panduan Fitur Yo-Managements\n2. Panduang Fitur Perhitungan Tabungan\n3. Panduan Mengunduh Catatan Rekomendasi Keuangan/Catatan Menabung\n[bold bright_yellow]4. Kembali[/bold bright_yellow][/bold bright_cyan]")  
    pilihanMenu = Prompt.ask("[bold bright_green]Pilih menu yang ingin Anda akses (1-3), atau pilih 4 untuk kembali[/bold bright_green]",
                             choices=["1","2","3","4"]) 

    progressBar() 

    # Tampilkan Panduan Fitur Yo-Managements
    if pilihanMenu == "1":
        console.print(Panel("Panduan Yo-Managements", style="bold bright_white", width=26))
       
        # Taruh panduan disini
        

    elif pilihanMenu == "2":
        console.print(Panel("Panduan Perhitungan Tabungan", style="bold bright_white", width=30))
        
        # Taruh panduan disini


    elif pilihanMenu == "3":
        console.print(Panel("Panduan Mengunduh Catatan Rekomendasi Keuangan/Catatan Menabung", style="bold bright_white", width=38))
        
        # Taruh panduan disini


    elif pilihanMenu == "4":
        return True

    # Kembali ke Halaman Utama
    kembali = Prompt.ask("[bold bright_blue]Ketik 'Q/q' untuk kembali ke menu utama[/bold bright_blue]", choices=["Q", "q"])
    if kembali.lower() == "q":
        progressBar()
        return True
    return False