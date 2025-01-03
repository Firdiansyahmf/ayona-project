# Pustaka Rich
import time # Time Progress Bar
from rich.progress import track # Progress Bar
from rich import print # Warna Teks
from rich.console import Console  # Menyorot teks
from rich.panel import Panel  # Menyorot teks
from rich.prompt import Prompt  # Input interaktif

# Buat objek Console dari pustaka Rich
console = Console()

#Inisialisasi variable global
untukCatatan = None
arrPengeluaran = None

# Fungsi Progress Bar
def progressBar():
    for _ in track(range(2), description="[bold green]Memuat..."):
        time.sleep(0.25)
    console.print("")

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

    # Untuk Bagian Desimal
    if int(bagianDecimal) == 0:
        hasil = hasil = f"Rp{formatBagianInt}"
    else:
        hasil = f"Rp{formatBagianInt},{bagianDecimal}"

    # Tambahkan tanda negatif jika nilai awalnya negatif
    if nilaiNegatif:
        hasil = f"-{hasil}"

    return hasil

# Fungsi input tanggal 
def inputTanggal(tipeTanggal):
    while True:
        inputTanggal = Prompt.ask(f"[bold bright_cyan]Masukan tanggal {tipeTanggal} (dd-mm-yyyy)[/bold bright_cyan]")

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
    global untukCatatan
    while True:
        tanyaMetodeInputPengeluaran = Prompt.ask("[bold bright_yellow]Masukkan jumlah pengeluaran, [bold bright_black]atau ketik 'hitung' untuk menghitung total dari item[/bold bright_black][/bold bright_yellow]")
        if tanyaMetodeInputPengeluaran.isdigit():
            jumlahPengeluaran = float(tanyaMetodeInputPengeluaran)
            untukCatatan = False
            break
        elif tanyaMetodeInputPengeluaran.lower() == "hitung":
            global arrPengeluaran
            arrPengeluaran = []
            console.print("[bold bright_yellow]Masukkan pengeluaran satu per satu. [bold bright_black]Ketik 'selesai' jika sudah.[/bold bright_black][/bold bright_yellow]")
            while True:
                inputPengeluaran = Prompt.ask("[bold bright_yellow]Masukkan pengeluaran[/bold bright_yellow]")
                if inputPengeluaran.isdigit():
                    arrPengeluaran.append(float(inputPengeluaran))
                elif inputPengeluaran.lower() == "selesai":
                    break
                else:
                    console.print("[bold bright_red]Input tidak valid. Harap masukkan angka Positif.[/bold bright_red]")
            jumlahPengeluaran = sum(arrPengeluaran)
            untukCatatan = True
            break
        else:
            console.print("[bold bright_red]Input tidak valid. Harap masukkan angka atau ketik 'hitung'.[/bold bright_red]")
    return jumlahPengeluaran

# Fungsi untuk Sorting data Kecil-Besar
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        return quickSort(left) + [pivot] + quickSort(right)
    
# Fungsi untuk Sorting data Besar-Kecil
def quickSortDesc(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x > pivot]
        right = [x for x in arr[1:] if x <= pivot]
        return quickSortDesc(left) + [pivot] + quickSortDesc(right)
    
# Fungsi untuk Searching data
def linearSearch(arr, target):
    # Ubag target menjadi lower
    targetLower = target.lower()

    for i in range(len(arr)):
        # Bandinglan elemen arr setelah diubah menjadi lower
        if arr[i].lower() == targetLower:
            return i
    return -1

"""
arr = [10, 15, 30, 70, 80, 60, 20, 90, 40]
target = 20
hasil = linearSearch(arr, target)
if hasil != -1:
    console.print(f"Linear Search: Elemen ditemukan di index {hasil}")
else:
    console.print("Linear Search: Elemen tidak ditemukan")
"""