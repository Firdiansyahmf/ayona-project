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
    bantuanPage = 1
    while bantuanPage == 1:
        # Panel
        console.print(Panel("Bantuan Pengguna", style="bold bright_cyan", width=20))
        
        # Input Pilihan Menu
        console.print("[bold bright_cyan]1. Panduan Fitur Yo-Managements\n2. Panduan Fitur Perhitungan Tabungan\n3. Panduan Mengunduh Catatan Rekomendasi Keuangan/Catatan Menabung\n[bold bright_yellow]4. Kembali[/bold bright_yellow][/bold bright_cyan]")  
        pilihanMenu = Prompt.ask("[bold bright_green]Pilih menu yang ingin Anda akses (1-3), atau pilih 4 untuk kembali[/bold bright_green]",
                                choices=["1","2","3","4"]) 
        progressBar()
        
        if pilihanMenu == "1":
            console.print(Panel("Panduan Yo-Managements", style="bold bright_white", width=26))
        
            # Panduan Yo-Management
            console.print("1. Pilih fitur Yo-Management di Menu Utama", style="bright_white")
            console.print("2. Isi Form Data Keuangan Yo-Management",  style="bright_white")
            console.print("3. Setelah semua data dimasukkan, sistem akan menghitung dan menampilkan catatan rekomendasi keuangan", style="bright_white")
            console.print("4. Anda bisa melihat catatan rekomendasi keuangan dalam bentuk tabel dengan mengetik 'y' atau 'n'", style="bright_white")
            console.print("5. Anda bisa melihat catatan rekomendasi keuangan dalam bentuk grafik dengan mengetik 'y' atau 'n'", style="bright_white")
            console.print("6. Anda bisa mengekspor catatan rekomendasi keuangan dalam bentuk PDF dengan mengetik 'y' atau 'n'", style="bright_white")

        elif pilihanMenu == "2":
            console.print(Panel("Panduan Perhitungan Tabungan", style="bold bright_white", width=32))
            
            # Tampilan Panduan Yo-Savers dan Yo-Goals
            console.print("1. Pilih fitur Perhitungan Tabungan di Menu Utama", style= "bright_white")
            console.print("2. Terdapat dua pilihan, yaitu 'Yo-Savers' dan 'Yo-Goals',\nYo-Savers' digunakan untuk menghitung jumlah uang yang perlu ditabung per hari, minggu, dan bulan, sesuai dengan pilihan Anda. Sedangkan, 'Yo-Goals' digunakan untuk menentukan durasi menabung.", style= "bright_white")
            console.print("3. Jika Anda memilih Yo-Savers, maka Anda akan mengisi formulir keuangan Yo-Savers. Hal yang sama berlaku jika Anda memilih Yo-Goals.", style="bright_white")
            console.print("4. Anda bisa melihat Catatan Menabung dalam bentuk tabel dengan mengetik 'y' atau 'n'", style="bright_white")
            console.print("5. Anda bisa melihat Catatan Menabung dalam bentuk grafik dengan mengetik 'y' atau 'n'", style="bright_white")
            console.print("6. Anda bisa mengekspor Catatan Menabung dalam bentuk PDF dengan mengetik 'y' atau 'n'", style="bright_white")

        elif pilihanMenu == "3":
            console.print(Panel("Panduan Mengunduh Catatan Rekomendasi Keuangan/Menabung", style="bold bright_white", width=33))
            
            # Panduan mengunduh catatan rekomendasi keuangan atau menabung ke pdf
            console.print("1. Saat catatan rekomendai keuangan/menabung ditampilkan, akan ada pertanyaan untuk export ke PDF", style="bright_white")
            console.print("2. Anda bisa mengekspor Catatan Rekomendasi Keuangan/Menabung ke PDF dengan mengetik 'y' atau 'n'", style="bright_white")

        elif pilihanMenu == "4":
            return True
        
        bantuanPage = Prompt.ask("[bold bright_blue]Ketik 'Q/q' untuk kembali ke bantuan pengguna[/bold bright_blue]", choices=["Q", "q"])
        if bantuanPage.lower() == "q":
            bantuanPage = 1
            progressBar()

    # Kembali ke Halaman Utama
    kembali = Prompt.ask("[bold bright_blue]Ketik 'Q/q' untuk kembali ke menu utama[/bold bright_blue]", choices=["Q", "q"])
    if kembali.lower() == "q":
        progressBar()
        return True
    return False