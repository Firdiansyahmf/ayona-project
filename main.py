from rich.console import Console
from rich.text import Text

# Halaman Utama 
def garis():
    garis = print("--------------------------------------------")
    return garis

console = Console()
console.print("Selamat Datang di Ayona", style="bright_green")
print("Pilih Opsi Berikut:")
print("1. Yo-Managements")
print("2. Perhitungan Tabungan")
print("3. Bantuan Pengguna")

input_fitur = int(input("Masukkan (1/2/3) Fitur yang ingin anda pilih: "))

if input_fitur == 1:
    garis()
    print("Pilihan Bagus! Ini adalah Fitur 1. Yo-Managements")
    garis()
elif input_fitur == 2:
    garis()
    print("Pilihan Keren! Ini adalah Fitur 2. Perhitungan Tabungan, yang memuat 2 Fitur yakni Yo-Savers & Yo-Goals")
    garis()
elif input_fitur == 3:
    garis()
    print("Nice one! Ini adalah Fitur 3. Bantuan Pengguna")
    garis()