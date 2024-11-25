# Pustaka Rich
from rich.console import Console  # Menyorot teks
from rich.panel import Panel  # Menyorot teks
from rich.prompt import Prompt  # Input interaktif
from rich import print  # Warna teks

# Library
from fpdf import FPDF  # Impor PDF
from matplotlib import pyplot as plt
from matplotlib import style
from rich.table import Table #Membuat Tabel

# Standar Pustaka Python (datetime)
from datetime import datetime

# Impor fungsi progressBar, formatRupiah, hitungJumlahPengeluaran
from utils import progressBar, formatRupiah, hitungJumlahPengeluaran

# Buat objek Console dari pustaka Rich
console = Console()

#Fungsi membuat Tabel
def tabelYo_Savers(
        tanggalPerhitungan,
        hariMenabung,
        targetBesaranMenabung,
        jumlahPemasukanBersih,
        yoSaversHari,
        yoSaversMinggu,
        yoSaversBulan
):
    table = Table(title = "Tabel Yo-Savers")

    table.add_column ("Tanggal Perhitungan",justify = "center", style = "cyan", no_wrap = True)
    table.add_column ("Lama Waktu Menabung", justify = "center", style = "magenta")
    table.add_column ("Target Besaran Menabung", justify = "center", style = "green")
    table.add_column ("Pemasukan Bersih Anda", justify = "center", style = "cyan")   
    table.add_column ("Menabung per Hari", justify = "center", style = "magenta") 
    table.add_column ("Menabung per Minggu", justify = "center", style = "red")    
    table.add_column ("Menabung per Bulan", justify = "center", style = "green")

    table.add_row (
        str(tanggalPerhitungan),
        str(hariMenabung),
        str(targetBesaranMenabung), 
        str (jumlahPemasukanBersih), 
        str (yoSaversHari),
        str (yoSaversMinggu),
        str (yoSaversBulan)
    )

    print(table)

# Fungsi untuk mengecek apakah tahun adalah kabisat
def tahunKabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    return False

# Fungsi untuk mengecek jumlah hari di setiap bulan dalam satu tahun
def hariDalamBulan(tahun):
    if tahunKabisat(tahun):
        return [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Fungsi untuk mengonversi waktu ke dalam hari
def konversiKeHari(
        jenisLamaWaktuMenabung, 
        lamaWaktuMenabung, 
        tahun
):
    hariBulan = hariDalamBulan(tahun)

    if jenisLamaWaktuMenabung == "hari":
        hariMenabung = lamaWaktuMenabung
    elif jenisLamaWaktuMenabung == "minggu":
        hariMenabung = lamaWaktuMenabung * 7
    elif jenisLamaWaktuMenabung == "bulan":
        bulanPenuh = int(lamaWaktuMenabung)  # Bulan penuh
        sisaBulan = lamaWaktuMenabung - bulanPenuh  # Pecahan bulan
        hariMenabung = sum(hariBulan[:bulanPenuh])  # Total hari dari bulan penuh
        if sisaBulan > 0:
            hariMenabung += sisaBulan * hariBulan[bulanPenuh]  # Hari dari pecahan bulan
    elif jenisLamaWaktuMenabung == "tahun":
        hariMenabung = lamaWaktuMenabung * (366 if tahunKabisat(tahun) else 365)
    else:
        console.print("[bold bright_red]Input tidak valid. Harap masukkan angka atau ketik 'hitung' atau 'ya'.[/bold bright_red]")

    return hariMenabung

"""
Fitur 2
(main)
"""
def fiturDua():
    # Impor variabel global jumlahPemasukanBersih
    from features1 import jumlahPemasukanBersih

    # Panel
    console.print(Panel("Perhitungan Tabungan", style="bold bright_cyan", width=24))

    # Input tipe dan tanggal pemasukan
    console.print("[bold bright_cyan]1. Yo-Savers\n2. Yo-Goals\n[bold bright_yellow]3. Kembali[/bold bright_yellow][/bold bright_cyan]")
    pilihanPerhitungan = Prompt.ask("[bold bright_green]Pilih menu yang ingin Anda akses (1-2), atau pilih 3 untuk kembali[/bold bright_green]", 
                        choices=["1", "2", "3"])
    progressBar()
    
    # Masuk ke Yo-Savers
    if pilihanPerhitungan == "1":
        console.print(Panel("Yo-Savers", style="bold bright_white", width=13))

        # Tanggal saat Perhitungan
        tanggalPerhitungan = datetime.now()

        # Input jenis lama waktu menabung
        jenisLamaWaktuMenabung = Prompt.ask("[bold bright_green]Masukkan jenis untuk lama waktu menabung Anda[/bold bright_green]", 
                                            choices=["hari", "minggu", "bulan", "tahun"])
        
        # Input lama waktu menabung
        while True:
            lamaWaktuMenabung = Prompt.ask("[bold bright_green]Masukkan lama waktu menabung (Masukkan angka berdasarkan jenis sebelumnya)[/bold bright_green]")
            if lamaWaktuMenabung.isdigit():
                lamaWaktuMenabung = float(lamaWaktuMenabung)
                break
            elif lamaWaktuMenabung == 0:
                console.print("[bold bright_red]Input tidak valid. Harap masukkan angka positif.[/bold bright_red]")
            else:
                console.print("[bold bright_red]Input tidak valid. Harap masukkan angka positif.[/bold bright_red]")
        
        # Konversi lama waktu menabung ke Hari
        hariMenabung = konversiKeHari(
            jenisLamaWaktuMenabung,
            lamaWaktuMenabung,
            datetime.now().year
        )

        # Input target besaran menabung
        while True:
            targetBesaranMenabung = Prompt.ask("[bold bright_green]Masukkan target besaran menabung Anda[/bold bright_green]")
            if targetBesaranMenabung.isdigit():
                targetBesaranMenabung = int(targetBesaranMenabung)
                break
            else:
                console.print("[bold bright_red]Input tidak valid. Harap masukkan angka positif.[/bold bright_red]")

        # Input jumlah pemasukan bersih
        while True:
            tanyaMetodeInputJumlahPemasukanBersih = Prompt.ask("[bold bright_green]Masukkan jumlah pemasukan bersih, [bold bright_black]atau ketik 'hitung' untuk menghitung jumlah pemasukan bersih dan ketik 'ya' apabila ingin menggunakan data catatan keuangan Yo-Managements yang sudah anda isi[/bold bright_black][/bold bright_green]")
            if tanyaMetodeInputJumlahPemasukanBersih.isdigit():
                jumlahPemasukanBersih = float(tanyaMetodeInputJumlahPemasukanBersih)
            elif tanyaMetodeInputJumlahPemasukanBersih.lower() == "hitung":
                # Input jumlah pemasukan
                while True:
                    jumlahPemasukan = Prompt.ask("[bold bright_green]Masukkan jumlah pemasukan[/bold bright_green]")
                    if jumlahPemasukan.isdigit():
                        jumlahPemasukan = float(jumlahPemasukan)
                        break
                    else:
                        console.print("[bold bright_red]Input tidak valid. Harap masukkan angka positif.[/bold bright_red]")

                # Input jumlah pengeluaran
                jumlahPengeluaran = hitungJumlahPengeluaran()

                # Hitung pemasukan bersih 
                jumlahPemasukanBersih = jumlahPemasukan - jumlahPengeluaran

            elif tanyaMetodeInputJumlahPemasukanBersih.lower() == "ya":
                # Validasi
                if jumlahPemasukanBersih is not None:
                    jumlahPemasukanBersih = jumlahPemasukanBersih
                else:
                    console.print("[bold bright_red]Anda belum mengisi data catatan keuangan Yo-Managements. Gunakan cara lain.[/bold bright_red]")
                    continue
            else:
                console.print("[bold bright_red]Input tidak valid. Harap masukkan angka atau ketik 'hitung' atau 'ya'.[/bold bright_red]")

            # Perhitungan Yo-Savers
            yoSaversHari = targetBesaranMenabung / konversiKeHari(jenisLamaWaktuMenabung, lamaWaktuMenabung, datetime.now().year)
            yoSaversMinggu = yoSaversHari * 7
            yoSaversBulan = targetBesaranMenabung / lamaWaktuMenabung

            # Tampilkan catatan menabung Yo-Savers
            progressBar()
            console.print(Panel("Catatan Menabung Yo-Savers", style="bold bright_white", width=15))
            console.print(f"[bold bright_white]Tanggal Perhitungan\t: {tanggalPerhitungan}[/bold bright_white]")
            console.print(f"[bold bright_white]Lama Waktu Menabung\t: {hariMenabung} hari[/bold bright_white]")
            console.print(f"[bold bright_white]Target besaran menabung\t: {formatRupiah(targetBesaranMenabung)}[/bold bright_white]")
            console.print(f"[bold bright_white]Pemasukan bersih Anda\t: {formatRupiah(jumlahPemasukanBersih)}[/bold bright_white]")
            console.print(f"[bold bright_black]Jumlah uang yang harus anda sisihkan[/bold bright_black]")
            console.print(f"[bold bright_white]Dalam per hari\t\t: {formatRupiah(yoSaversHari)}/Hari[/bold bright_white]")
            console.print(f"[bold bright_white]Dalam per minggu\t: {formatRupiah(yoSaversMinggu)}/Minggu[/bold bright_white]")
            console.print(f"[bold bright_white]Dalam per bulan\t\t: {formatRupiah(yoSaversBulan)}/Bulan[/bold bright_white]")
            break

    #Pilihan Yo-Savers dalam bentuk Tabel
        tabel = Prompt.ask(f"\n [bold bright_blue]Lihat dalam bentuk tabel?[/bold bright_blue]", 
                    choices =["y","n"])
        if tabel.lower() == "y":
                tabelYo_Savers(
                tanggalPerhitungan, 
                hariMenabung, 
                formatRupiah(targetBesaranMenabung),
                formatRupiah(jumlahPemasukanBersih), 
                formatRupiah(yoSaversHari),  
                formatRupiah(yoSaversMinggu), 
                formatRupiah(yoSaversBulan)
        )
    # Masuk ke Yo-Goals
    elif pilihanPerhitungan == "2":
            console.print(Panel("Yo-Goals", style="bold bright_white", width=12))
    
    # Kembali ke Halaman Utama
    elif pilihanPerhitungan == "3":
        return True

    # Kembali ke Halaman Utama
    kembali = Prompt.ask("[bold bright_blue]Ketik 'Q/q' untuk kembali ke menu utama[/bold bright_blue]", choices=["Q", "q"])
    if kembali.lower() == "q":
        progressBar()
        return True
    return False