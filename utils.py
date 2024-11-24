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