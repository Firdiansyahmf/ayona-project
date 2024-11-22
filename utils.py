# Pustaka Rich
import time # Time Progress Bar
from rich.progress import track # Progress Bar
from rich import print # Warna Teks

# Grafik
import matplotlib.pyplot as plt

# Fungsi Progress Bar
def progressBar():
    for _ in track(range(2), description="[bold green]Memuat..."):
        time.sleep(0.25)
    print("")

# Fungsi format ke Rupiah
def formatRupiah(nilai):
    # Membagi angka menjadi bagian int dan desimal
    strNilai = str(nilai)
    if '.' in strNilai:
        bagianInt, bagianDecimal = strNilai.split('.')
    else:
        bagianInt, bagianDecimal = strNilai, '00'
    
    # Menambah pemisah ribuan untuk bagianInt
    bagianInt = bagianInt[::-1]
    formatBagianInt = ""
    for i in range (0, len(bagianInt), 3):
        formatBagianInt += bagianInt[i:i+3] + "."
    
    # Menghapus titik terakhir jika ada
    if formatBagianInt[-1] == ".":
        formatBagianInt = formatBagianInt[:-1]

    # Membalikan str nilai setelah pemisah ribuah ditambahkan
    formatBagianInt = formatBagianInt[::-1]

    # Menjaga hanya 2 angka di belakang koma untuk bagian desimal
    bagianDecimal = bagianDecimal + '00' 
    bagianDecimal = bagianDecimal[:2] 

    # Menggabung int dan desimal kembali
    return f"Rp{formatBagianInt},{bagianDecimal}"