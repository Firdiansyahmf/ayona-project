# Pustaka Rich
import time # Time Progress Bar
from rich.progress import track # Progress Bar
from rich import print # Warna Teks
from rich.console import Console  # Menyorot teks
from rich.panel import Panel  # Menyorot teks
from rich.prompt import Prompt  # Input interaktif

# Buat objek Console dari pustaka Rich
console = Console()

# Fungsi Progress Bar
def progressBar():
    for _ in track(range(2), description="[bold green]Memuat..."):
        time.sleep(0.25)
    print("")

# Fungsi format ke Rupiah
def formatRupiah(nilai):
    # int nilai negatif?
    nilaiNegatif = nilai < 0
    nilai = abs(nilai)  # Ubah menjadi positif untuk pemrosesan

    # Konversi int nilai ke string
    strNilai = f"{nilai:.2f}"
    bagianInt, bagianDecimal = strNilai.split('.')

    # Format bagian integer dengan pemisah ribuan
    formatBagianInt = "{:,}".format(int(bagianInt)).replace(",", ".")

    # Gabungkan kembali bagian integer dan desimal
    hasil = f"Rp{formatBagianInt},{bagianDecimal}"

    # Tambahkan tanda negatif jika nilai awalnya negatif
    if nilaiNegatif:
        hasil = f"-{hasil}"

    return hasil

# Fungsi input tanggal 
def inputTanggal(tipeTanggal):
    while True:
        inputTanggal = Prompt.ask(f"[bold bright_green]Masukan tanggal {tipeTanggal} (dd-mm-yyyy)[/bold bright_green]")

        # Memeriksa format tanggal dan validasi manual
        if len(inputTanggal) == 10 and inputTanggal[2] == '-' and inputTanggal[5] == '-':
            day, month, year = inputTanggal.split('-')
            
            # Memastikan nilai adalah angka
            if day.isdigit() and month.isdigit() and year.isdigit():
                day = int(day)
                month = int(month)
                year = int(year)
                
                # Memastikan bahwa tanggal valid (bulan tidak lebih dari 12, hari sesuai bulan)
                if 1 <= month <= 12:
                    if 1 <= day <= 31:
                        if month in [4, 6, 9, 11] and day > 30:
                            console.print("[bold bright_red]Tanggal tidak valid. Bulan ini hanya memiliki 30 hari.[/bold bright_red]")
                        elif month == 2:
                            # Cek tahun kabisat
                            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                                if day > 29:
                                    console.print("[bold bright_red]Tanggal tidak valid. Februari pada tahun kabisat hanya memiliki 29 hari.[/bold bright_red]")
                                    continue
                            elif day > 28:
                                console.print("[bold bright_red]Tanggal tidak valid. Februari hanya memiliki 28 hari pada tahun non-kabisat.[/bold bright_red]")
                                continue
                        
                        return inputTanggal  # Jika tanggal valid, ambil nilai tanggal
                    else:
                        console.print("[bold bright_red]Tanggal tidak valid. Hari harus antara 1 hingga 31.[/bold bright_red]")
                else:
                    console.print("[bold bright_red]Tanggal tidak valid. Bulan harus antara 1 hingga 12.[/bold bright_red]")
            else:
                console.print("[bold bright_red]Tanggal tidak valid. Pastikan semua bagian tanggal berupa angka.[/bold bright_red]")
        else:
            console.print("[bold bright_red]Tanggal tidak valid. Harap masukkan tanggal dengan format yang benar (dd-mm-yyyy).[/bold bright_red]")

# Fungsi untuk hitung jumlah pengeluaran
def hitungJumlahPengeluaran():
    jumlahPengeluaran = 0
    while True:
        tanyaMetodeInputPengeluaran = Prompt.ask("[bold bright_green]Masukkan jumlah pengeluaran, [bold bright_black]atau ketik 'hitung' untuk menghitung total dari item[/bold bright_black][/bold bright_green]")
        if tanyaMetodeInputPengeluaran.isdigit():
            jumlahPengeluaran = float(tanyaMetodeInputPengeluaran)
            break
        elif tanyaMetodeInputPengeluaran.lower() == "hitung":
            listPengeluaran = []
            console.print("[bold bright_yellow]Masukkan pengeluaran satu per satu. [bold bright_black]Ketik 'selesai' jika sudah.[/bold bright_black][/bold bright_yellow]")
            while True:
                inputPengeluaran = Prompt.ask("[bold bright_yellow]Masukkan pengeluaran[/bold bright_yellow]")
                if inputPengeluaran.isdigit():
                    listPengeluaran.append(float(inputPengeluaran))
                elif inputPengeluaran.lower() == "selesai":
                    break
                else:
                    console.print("[bold bright_red]Input tidak valid. Harap masukkan angka.[/bold bright_red]")
            jumlahPengeluaran = sum(listPengeluaran)
            break
        else:
            console.print("[bold bright_red]Input tidak valid. Harap masukkan angka atau ketik 'hitung'.[/bold bright_red]")
    return jumlahPengeluaran