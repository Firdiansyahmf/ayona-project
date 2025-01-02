# Pustaka Rich
from rich.console import Console  # Menyorot teks
from rich.panel import Panel  # Menyorot teks
from rich.prompt import Prompt  # Input interaktif
from rich import print  # Warna teks

# Library Lainnya
from fpdf import FPDF  # Impor PDF
from matplotlib import pyplot as plt
from matplotlib import style
from rich.table import Table # Membuat Tabel
from math import ceil  # Impor ceil
from matplotlib.ticker import FuncFormatter
import os, math, calendar

# Standar Pustaka Python (datetime)
from datetime import datetime

# Impor fungsi progressBar, formatRupiah, hitungJumlahPengeluaran
from utils import progressBar, formatRupiah, hitungJumlahPengeluaran, linearSearch

# Buat objek Console dari pustaka Rich
console = Console()

# Fungsi tampilan tabel Yo-Savers
def tabelYoSavers(
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
    table.add_column ("Lama Waktu Menabung", justify = "center", style = "blue")
    table.add_column ("Target Besaran Menabung", justify = "center", style = "#FFD700")
    table.add_column ("Pemasukan Bersih Anda", justify = "center", style = "green")   
    table.add_column ("Menabung per Hari", justify = "center", style = "magenta") 
    table.add_column ("Menabung per Minggu", justify = "center", style = "magenta")    
    table.add_column ("Menabung per Bulan", justify = "center", style = "magenta")
    hari = int(hariMenabung)
    lamaWaktuMenabung = str(hari) + " hari"
    table.add_row (
        str(tanggalPerhitungan),
        str(lamaWaktuMenabung),
        str(targetBesaranMenabung), 
        str(jumlahPemasukanBersih), 
        str(yoSaversHari),
        str(yoSaversMinggu),
        str(yoSaversBulan)
    )
    print(table)

#Fungsi tampilan tabel Yo-Goals
def tabelYoGoals(besaranMenabungHari, targetBesaranMenabung, yoGoals):
    table = Table(title = "Tabel Yo-Goal")
    table.add_column("Jumlah Besaran Menabung/hari",justify = "center", style = "cyan", no_wrap = True)
    table.add_column("Target Besaran Menabung", justify = "center", style = "magenta")
    table.add_column("Lama Waktu Menabung", justify = "center", style = "green")
    table.add_row (
        str(besaranMenabungHari),
        str(targetBesaranMenabung),
        str(yoGoals)
    )
    print(table)

# Grafik untuk Yo-Savers
def grafikLineYoSavers(
    tanggalPerhitungan,
    hariMenabung,
    targetBesaranMenabung,
    jumlahPemasukanBersih,
    yoSaversHari,
    yoSaversMinggu,
    yoSaversBulan
):
    # style.use('ggplot')
    # x = Garis X horizontal, y = Garis Y veritikal
    x = [0, 1, 2]
    # pemasukanBersih = int(jumlahPemasukanBersih)
    if yoSaversHari != None and yoSaversMinggu != None and yoSaversBulan != None:
        perHari = math.trunc(float(yoSaversHari))
        perBulan = math.trunc(float(yoSaversBulan))
        perMinggu = math.trunc(float(yoSaversMinggu))
    elif yoSaversHari != None and yoSaversMinggu != None and yoSaversBulan == None:
        perHari = math.trunc(float(yoSaversHari))
        perBulan = math.trunc(float(yoSaversBulan))
        perMinggu = float(0)
    elif yoSaversHari != None and yoSaversMinggu == None and yoSaversBulan == None:
        perHari = math.trunc(float(yoSaversHari))
        perBulan = float(0)
        perMinggu = float(0)
    elif yoSaversHari == None and yoSaversMinggu == None and yoSaversBulan == None:
        perHari = float(0)
        perBulan = float(0)
        perMinggu = float(0)

    y = [perHari, perMinggu, perBulan]
    fig, ax = plt.subplots()

    # Definisikan Grafik apa disini Grafiknya == Bar(Batang)
    ax.bar(x, y, align='center',  color=['purple', 'purple', 'purple'])

    # Menampilkan Teks di dalam Grafiknya sesuai nilai Y
    for i, val in enumerate(y):
        # Menggunakan fungsi formatRupiah untuk memformat angka
        formattedValue = formatRupiah(val)
        plt.text(i, val, f'{formattedValue}', ha='center', va='bottom', color='black', fontsize=10)

    hari = int(hariMenabung)
    lamaWaktuMenabung = str(hari)
    ax.set_title(f'Yo-Savers Graphsite by Ayona\nTarget Menabung {formatRupiah(targetBesaranMenabung)}. Dalam waktu {lamaWaktuMenabung} hari. Dengan pemasukan {formatRupiah(jumlahPemasukanBersih)}')
    ax.set_ylabel('Perlu Disisihkan')
    ax.set_xlabel('Rentang Waktu')

    # Set Teks Label pada Garis X yang horizontal
    ax.set_xticks(x)
    # a = "Pemasukan Bersih"
    a = "Per Hari"
    b = "Per Minggu"
    c = "Per Bulan"
    ax.set_xticklabels((a, b, c))

    def rupiah_formatter(x, pos):
        return formatRupiah(x)
    ax.yaxis.set_major_formatter(FuncFormatter(rupiah_formatter))

    # Menampilkan Grafik
    plt.show()

# Format rupiah untuk Yo-Goals
def formatRupiahYg(x, pos):
    return f'Rp{int(x):,}'.replace(',', '.')

# Grafik untuk Yo-Goals
def grafikLineYoGoals(besaranMenabungHari, targetBesaranMenabung, yoGoals):  
    x = []
    y = []
    kenaikanTabungan = 0

    # kenaikan tabungan setiap hari
    for hari in range(yoGoals):
        kenaikanTabungan += besaranMenabungHari
        y.append(kenaikanTabungan)
        x.append(f'H-{hari + 1}')

    # interval
    interval = max(yoGoals // 5, 1)

    # Menampilkan grafik garis progres menabung
    plt.plot(x, y, marker='o', label='Progres Menabung', color='blue')

    # Menampilkan nilai tabungan di titik-titik tertentu
    for i in range(0, yoGoals, interval):
        plt.text(
            i, y[i],  # posisi teks di setiap titik
            f"Rp{math.trunc(y[i]):,}".replace(',', '.'),  # format Rupiah
            fontsize=9, color='green', ha='center', va='bottom'  # gaya teks
        )

    # Pastikan H terakhir tetap ditampilkan jika ada
    if yoGoals % interval != 0:  
        plt.text(
            yoGoals - 1, y[yoGoals - 1],  # Posisi teks untuk hari terakhir
            f"Rp{math.trunc(y[yoGoals - 1]):,}".replace(',', '.'),  # format Rupiah
            fontsize=9, color='green', ha='center', va='bottom'
        )

    # Menambahkan garis horizontal untuk menunjukkan target menabung
    plt.axhline(y=targetBesaranMenabung, color='red', linestyle='--', label='Target Menabung')
    
    # Label dan judul grafik
    plt.xlabel('Progress Hari')
    plt.ylabel('Kenaikan Tabungan')  # Menambahkan label sumbu Y
    plt.title(f'Yo-Goals Graphsite by Ayona \nTarget menabung Rp{targetBesaranMenabung:,.0f} dalam {yoGoals} Hari, Uang yang disisihkan sebesar Rp{besaranMenabungHari:,.0f}')
    
    # Menambahkan grid dan legenda pada grafik
    plt.grid(True)
    plt.legend()
    
    # Atur label pada sumbu X agar hanya menampilkan setiap interval tertentu
    plt.xticks(range(0, yoGoals, interval), [f'H-{i+1}' for i in range(0, yoGoals, interval)])  
    plt.xticks(rotation=45)
    
    # Menggunakan FuncFormatter untuk memformat angka di sumbu Y
    plt.gca().yaxis.set_major_formatter(FuncFormatter(formatRupiahYg))

    # Penyesuaian tata letak grafik agar tidak terpotong
    plt.tight_layout()  

    # Menampilkan grafik
    plt.show()

# Ekspor PDF untuk Yo-Savers
def eksporPDFYoSavers(
    tanggalPerhitungan, 
    hariMenabung, 
    targetBesaranMenabung, 
    jumlahPemasukanBersih, 
    yoSaversHari, 
    yoSaversMinggu, 
    yoSaversBulan,
    minPemasukanBersih
):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, txt="Catatan Menabung Yo-Savers", ln=True, align="C")
    pdf.set_font("Arial", size=12)
    pdf.ln(10)  # Jarak baris
    hariMenabung = int(hariMenabung)
    pdf.cell(200, 10, txt=f"Tanggal Perhitungan: {tanggalPerhitungan}", ln=True)
    pdf.cell(200, 10, txt=f"Lama Waktu Menabung: {hariMenabung} hari", ln=True)
    pdf.cell(200, 10, txt=f"Target Besaran Menabung: {targetBesaranMenabung}", ln=True)
    pdf.cell(200, 10, txt=f"Jumlah Pemasukan Bersih: {jumlahPemasukanBersih}", ln=True)
    pdf.cell(200, 10, txt=f"Jumlah uang yang harus anda sisihkan:   ", ln=True)
    pdf.cell(200, 10, txt=f"Dalam per Hari: {yoSaversHari}", ln=True)
    pdf.cell(200, 10, txt=f"Dalam per Minggu: {yoSaversMinggu}", ln=True)
    pdf.cell(200, 10, txt=f"Dalam per Bulan: {yoSaversBulan}", ln=True)
    pdf.cell(200, 10, txt=f"Pemasukan bersih tidak mencukupi untuk menabung dengan lama waktu yang ditentukan", ln=True)
    pdf.cell(200, 10, txt=f"Minimal pemasukan bersih per hari yang dibutuhkan: {formatRupiah(minPemasukanBersih)}", ln=True)
    
    #Simpan PDF
    unduhPath = os.path.join(os.path.expanduser("~"), "Downloads")
    namaFileAwal = "Catatan_Menabung_Yo-Savers"
    angkaUrut = 1
    while True:
        namaFile = f"{namaFileAwal} ({angkaUrut}).pdf"
        lokasiFile = os.path.join(unduhPath, namaFile)
        if not os.path.exists(lokasiFile):
            break
        angkaUrut += 1
    pdf.output(lokasiFile)
    print(f"Hasil berhasil diekspor ke [bold green]'Catatan_Menabung_Yo-Savers.pdf'[/bold green]")
    
# Ekspor PDF untuk Yo-Goals
def eksporPDFYoGoals(namaTargetMenabung, besaranMenabungHari, targetBesaranMenabung, yoGoals):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, txt="Catatan Menabung Yo-Goals", ln=True, align="C")
    pdf.set_font("Arial", size=12)
    pdf.ln(10)  # Jarak baris
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, f"Nama target Menabung  : {namaTargetMenabung}", ln=True)
    pdf.cell(200, 10, txt=f"Besaran Menabung Setiap Hari: {besaranMenabungHari}", ln=True)
    pdf.cell(200, 10, txt=f"Target Besaran Menabung: {targetBesaranMenabung}", ln=True)
    pdf.cell(200, 10, txt=f"Lama Anda Perlu Menabung: {yoGoals} hari", ln=True)

    #Simpan PDF
    unduhPath = os.path.join(os.path.expanduser("~"), "Downloads")
    namaFileAwal = "Catatan_Menabung_Yo-Goals"
    angkaUrut = 1
    while True:
        namaFile = f"{namaFileAwal} ({angkaUrut}).pdf"
        lokasiFile = os.path.join(unduhPath, namaFile)
        if not os.path.exists(lokasiFile):
            break
        angkaUrut += 1
    pdf.output(lokasiFile)
    print(f"Hasil berhasil diekspor ke [bold green]'Catatan_Menabung_Yo-Goals.pdf'[/bold green]")

# Fungsi untuk mengecek apakah tahun adalah kabisat dengan library calendar
def tahunKabisat(tahun):
    return calendar.isleap(tahun)

# Fungsi untuk mengecek jumlah hari di setiap bulan dalam satu tahun
def hariDalamBulan(tahun):
    # monthrange -> jumlah hari dlm satu bulan berdasarkan tahun dan bulan tertentu
    return [calendar.monthrange(tahun, bulan)[1] for bulan in range(1,13)]

# Fungsi untuk mengonversi waktu ke dalam hari
def konversiKeHari(jenisLamaWaktuMenabung, lamaWaktuMenabung, tahun):
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

    # Input Pilihan Menu
    console.print("[bold bright_white]1. Yo-Savers\n2. Yo-Goals\n[bold bright_yellow]3. Kembali[/bold bright_yellow][/bold bright_white]")
    pilihanPerhitungan = Prompt.ask("[bold bright_cyan]Pilih menu yang ingin Anda akses (1-2), atau pilih 3 untuk kembali[/bold bright_cyan]", 
                        choices=["1", "2", "3"])
    progressBar()
    
    # Masuk ke Yo-Savers
    if pilihanPerhitungan == "1":
        console.print(Panel("Yo-Savers", style="bold bright_cyan", width=13))

        # Tanggal saat Perhitungan
        datetimeNow = datetime.now()
        waktuStr = str(datetimeNow)
        waktuPerhitungan = datetime.strptime(waktuStr, "%Y-%m-%d %H:%M:%S.%f")
        tanggalPerhitungan = waktuPerhitungan.strftime("%d-%m-%Y")

        # Input jenis lama waktu menabung
        jenisLamaWaktuMenabung = Prompt.ask("[bold bright_cyan]Masukkan jenis untuk lama waktu menabung Anda[/bold bright_cyan]", choices=["hari", "minggu", "bulan", "tahun"])
        
        # Input lama waktu menabung
        while True:
            lamaWaktuMenabung = Prompt.ask("[bold bright_cyan]Masukkan lama waktu menabung [bold bright_black](Masukkan angka berdasarkan jenis sebelumnya)[/bold bright_black][/bold bright_cyan]")
            if lamaWaktuMenabung.isdigit():
                lamaWaktuMenabung = float(lamaWaktuMenabung)
                break
            elif lamaWaktuMenabung == 0:
                console.print("[bold bright_red]Input tidak valid. Harap masukkan angka tidak sama dengan 0.[/bold bright_red]")
            else:
                console.print("[bold bright_red]Input tidak valid. Harap masukkan angka positif.[/bold bright_red]")
        
        # Konversi lama waktu menabung ke Hari
        hariMenabung = konversiKeHari(jenisLamaWaktuMenabung,lamaWaktuMenabung,datetime.now().year)

        # Input target besaran menabung
        while True:
            targetBesaranMenabung = Prompt.ask("[bold bright_cyan]Masukkan target besaran menabung Anda[/bold bright_cyan]")
            if targetBesaranMenabung.isdigit():
                targetBesaranMenabung = int(targetBesaranMenabung)
                break
            else:
                console.print("[bold bright_red]Input tidak valid. Harap masukkan angka positif.[/bold bright_red]")

        # Input jumlah pemasukan bersih
        while True:
            tanyaMetodeInputJumlahPemasukanBersih = Prompt.ask("[bold bright_cyan]Masukkan jumlah pemasukan bersih, [bold bright_black]atau ketik 'hitung' untuk menghitung jumlah pemasukan bersih dan ketik 'ya' apabila ingin menggunakan data catatan keuangan Yo-Managements yang sudah anda isi[/bold bright_black][/bold bright_cyan]")
            if tanyaMetodeInputJumlahPemasukanBersih.isdigit():
                jumlahPemasukanBersih = float(tanyaMetodeInputJumlahPemasukanBersih)
            elif tanyaMetodeInputJumlahPemasukanBersih.lower() == "hitung":
                # Input jumlah pemasukan
                while True:
                    jumlahPemasukan = Prompt.ask("[bold bright_yellow]Masukkan jumlah pemasukan[/bold bright_yellow]")
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
            yoSaversMinggu = yoSaversHari * 7 if (targetBesaranMenabung / (yoSaversHari*7)) >= 1 else None
            yoSaversBulan = yoSaversHari * sum(hariDalamBulan(datetime.now().year)) / 12 if (targetBesaranMenabung / (yoSaversHari * sum(hariDalamBulan(datetime.now().year)) / 12)) >= 1 else None
            
            # Minimal pemasukan bersih
            minPemasukanBersih = yoSaversHari

            # Tampilkan catatan menabung Yo-Savers
            progressBar()
            console.print(Panel("Catatan Menabung Yo-Savers", style="bold bright_cyan", width=15))
            console.print(f"[bold bright_white]Tanggal Perhitungan\t: {tanggalPerhitungan}[/bold bright_white]")
            console.print(f"[bold bright_white]Lama Waktu Menabung\t: {int(hariMenabung)} hari[/bold bright_white]")
            console.print(f"[bold bright_white]Target besaran menabung\t: {formatRupiah(targetBesaranMenabung)}[/bold bright_white]")
            console.print(f"[bold bright_white]Pemasukan bersih Anda\t: {formatRupiah(jumlahPemasukanBersih)}[/bold bright_white]")
            console.print(f"[bold bright_black]Jumlah uang yang harus anda sisihkan[/bold bright_black]")
            if yoSaversHari <= jumlahPemasukanBersih:
                console.print(f"[bold bright_white]Dalam per hari\t\t: {formatRupiah(yoSaversHari)}/Hari[/bold bright_white]")
                if yoSaversMinggu is not None:
                    console.print(f"[bold bright_white]Dalam per minggu\t: {formatRupiah(yoSaversMinggu)}/Minggu[/bold bright_white]")
                if yoSaversBulan is not None:
                    console.print(f"[bold bright_white]Dalam per bulan\t\t: {formatRupiah(yoSaversBulan)}/Bulan[/bold bright_white]")
            else:
                console.print("[bold bright_red]Pemasukan bersih tidak mencukupi untuk menabung dengan lama waktu yang ditentukan[/bold bright_red]")
                console.print(f"[bold bright_dark]Minimal pemasukan bersih per hari yang dibutuhkan: {formatRupiah(minPemasukanBersih)}[/bold bright_dark]")
                yoSaversHari = None

            #Pilihan Yo-Savers dalam bentuk Tabel
            tabelys = Prompt.ask(f"[bold bright_cyan]Lihat dalam bentuk tabel?[/bold bright_cyan]", choices =["y","n"])
            if tabelys.lower() == "y":
                if yoSaversHari != None and yoSaversMinggu != None and yoSaversBulan != None:
                    tabelYoSavers(
                        tanggalPerhitungan, hariMenabung, formatRupiah(targetBesaranMenabung),
                        formatRupiah(jumlahPemasukanBersih), formatRupiah(yoSaversHari),  
                        formatRupiah(yoSaversMinggu), formatRupiah(yoSaversBulan)
                    )
                elif yoSaversHari != None and yoSaversMinggu != None and yoSaversBulan == None:
                    tabelYoSavers(
                        tanggalPerhitungan, hariMenabung, formatRupiah(targetBesaranMenabung), 
                        formatRupiah(jumlahPemasukanBersih), formatRupiah(yoSaversHari),  
                        formatRupiah(yoSaversMinggu), yoSaversBulan
                    )
                elif yoSaversHari != None and yoSaversMinggu == None and yoSaversBulan == None:
                    tabelYoSavers(
                        tanggalPerhitungan, hariMenabung, formatRupiah(targetBesaranMenabung), 
                        formatRupiah(jumlahPemasukanBersih), formatRupiah(yoSaversHari),  
                        yoSaversMinggu, yoSaversBulan
                    )
                elif yoSaversHari == None and yoSaversMinggu == None and yoSaversBulan == None:
                    tabelYoSavers(
                        tanggalPerhitungan, hariMenabung, formatRupiah(targetBesaranMenabung), 
                        formatRupiah(jumlahPemasukanBersih), yoSaversHari,  
                        yoSaversMinggu, yoSaversBulan
                    )

            # Pilihan Yo-Savers dalam bentuk Grafik
            grafikYs = Prompt.ask(f"[bold bright_cyan]Lihat data dalam bentuk Grafik?[/bold bright_cyan]", choices =["y","n"])
            if grafikYs.lower() == "y":
                console.print("[bold bright_yellow]Silakan Tutup jendela grafik untuk melanjutkan program.[/bold bright_yellow]")
                grafikLineYoSavers(
                    tanggalPerhitungan,
                    hariMenabung,
                    targetBesaranMenabung,
                    jumlahPemasukanBersih,
                    yoSaversHari,
                    yoSaversMinggu,
                    yoSaversBulan
                )
                console.print("[bold bright_white]Jendela Grafik ditutup.[/bold bright_white]")
                    
            # Ekspor PDF untuk Yo-Savers
            eksporys = Prompt.ask("[bold bright_cyan]Ingin ekspor hasil ke PDF?[/bold bright_cyan]", choices=["y", "n"])
            if eksporys.lower() == "y":
                if yoSaversHari != None and yoSaversMinggu != None and yoSaversBulan != None:
                    eksporPDFYoSavers(
                        tanggalPerhitungan, 
                        hariMenabung, 
                        formatRupiah(targetBesaranMenabung), 
                        formatRupiah(jumlahPemasukanBersih), 
                        formatRupiah(yoSaversHari), 
                        formatRupiah(yoSaversMinggu), 
                        formatRupiah(yoSaversBulan),
                        minPemasukanBersih
                    )
                elif yoSaversHari != None and yoSaversMinggu != None and yoSaversBulan == None:
                    eksporPDFYoSavers(
                        tanggalPerhitungan, 
                        hariMenabung, 
                        formatRupiah(targetBesaranMenabung), 
                        formatRupiah(jumlahPemasukanBersih), 
                        formatRupiah(yoSaversHari), 
                        formatRupiah(yoSaversMinggu), 
                        yoSaversBulan,
                        minPemasukanBersih
                    )
                elif yoSaversHari != None and yoSaversMinggu == None and yoSaversBulan == None:
                    eksporPDFYoSavers(
                        tanggalPerhitungan, 
                        hariMenabung, 
                        formatRupiah(targetBesaranMenabung), 
                        formatRupiah(jumlahPemasukanBersih), 
                        formatRupiah(yoSaversHari), 
                        yoSaversMinggu, yoSaversBulan,
                        minPemasukanBersih
                    )     
                elif yoSaversHari == None and yoSaversMinggu == None and yoSaversBulan == None:
                    eksporPDFYoSavers(
                        tanggalPerhitungan, 
                        hariMenabung, 
                        formatRupiah(targetBesaranMenabung), 
                        formatRupiah(jumlahPemasukanBersih), 
                        yoSaversHari, yoSaversMinggu, yoSaversBulan,
                        minPemasukanBersih
                    )
            break
    
    # Masuk ke Yo-Goals
    elif pilihanPerhitungan == "2":
        console.print(Panel("Yo-Goals", style="bold bright_cyan", width=12))

        # Import Variabel Global
        from database_yogoals import yoGoalsDict

        # Input nama target menabung
        namaTargetMenabung = Prompt.ask("[bold bright_cyan]Masukkan nama target menabung Anda[/bold bright_cyan]")
            
        # Input jumlah besaran Menabung di tiap harinya
        while True:
            besaranMenabungHari = Prompt.ask("[bold bright_cyan]Masukkan jumlah besaran menabung 'di setiap harinya' [bold bright_dark](Masukkan Nominal)[/bold bright_dark][/bold bright_cyan]")
            if besaranMenabungHari == "0":
                console.print("[bold bright_red]Input tidak valid. Harap masukkan angka tidak sama dengan 0.[/bold bright_red]")
            elif besaranMenabungHari.isdigit():
                besaranMenabungHari = float(besaranMenabungHari)
                break
            else:
                console.print("[bold bright_red]Input tidak valid. Harap masukkan angka positif.[/bold bright_red]")

        # Input target besaran menabung
        while True:
            targetBesaranMenabung = Prompt.ask("[bold bright_cyan]Masukkan target besaran menabung Anda [bold bright_dark](Masukkan Nominal)[/bold bright_dark][/bold bright_cyan]")
            if targetBesaranMenabung.isdigit():
                targetBesaranMenabung = int(targetBesaranMenabung)
                break
            else:
                console.print("[bold bright_red]Input tidak valid. Harap masukkan angka positif.[/bold bright_red]")

        # Perhitungan Yo-Goals (Lama waktu pengguna perlu menabung)
        yoGoals = ceil(targetBesaranMenabung / besaranMenabungHari) # ceil membulatkan ke atas

        # Tampilkan catatan menabung Yo-Goals
        progressBar()
        console.print(Panel("Catatan Menabung Yo-Goals", style="bold bright_cyan", width=15))
        console.print(f"[bold bright_white]Nama target Menabung\t\t\t  : {namaTargetMenabung}[/bold bright_white]")
        console.print(f"[bold bright_white]Jumlah besaran menabung di setiap harinya : {formatRupiah(besaranMenabungHari)}[/bold bright_white]")
        console.print(f"[bold bright_white]Jumlah target besaran menabung\t\t  : {formatRupiah(targetBesaranMenabung)}[/bold bright_white]")
        console.print(f"[bold bright_white]Lama Anda perlu menabung\t\t  : {yoGoals} hari[/bold bright_white]")

        # Memasukkan Data Yo-Goals ke Dictionary (DATABASE YO-GOALS)
        yoGoalsDict[namaTargetMenabung] = {
            'yoGoals': yoGoals
        }
        while True:
            targetSearch = Prompt.ask("[bold bright_cyan]\nApakah Anda ingin mencari Nama Target Menabung yang sudah dimasukkan?[/bold bright_cyan]", choices=["y", "n"])
            if targetSearch == "y":
                target = Prompt.ask("[bold bright_yellow]Masukkan Nama Target Menabung yang dicari[/bold bright_yellow]")
                namaList = list(yoGoalsDict.keys())
                result = linearSearch(namaList, target)
                if result != -1:
                    yoGoalsResult = yoGoalsDict[namaList[result]]['yoGoals']
                    console.print(f"[bold bright_green]Pencarian ditemukan[/bold bright_green]")
                    console.print(f"[bold bright_yellow]Nama target Menabung\t : {target}[/bold bright_yellow]")
                    console.print(f"[bold bright_yellow]Lama Anda perlu menabung : {yoGoalsResult} hari[/bold bright_yellow]")
                else:
                    console.print("[bold bright_red]Pencarian tidak ditemukan[/bold bright_red]")
                
                closeSearch = Prompt.ask("[bold bright_cyan]Tutup pencarian?[/bold bright_cyan]", choices=["y","n"])
                if closeSearch == "y":
                    break
                elif closeSearch == "n":
                    continue
            elif targetSearch == "n":
                break

        #Pilihan Yo-Goals dalam bentuk Tabel
        tabelyg = Prompt.ask(f"[bold bright_blue]\nLihat dalam bentuk tabel?[/bold bright_blue]", choices =["y","n"])
        
        if tabelyg.lower() == "y":
            tabelYoGoals(formatRupiah(besaranMenabungHari), formatRupiah(targetBesaranMenabung), f"{yoGoals} hari")

        # Pilihan Yo-Goals dalam bentuk Grafik
        grafikYg = Prompt.ask(f"[bold bright_blue]Lihat data dalam bentuk Grafik?[/bold bright_blue]", choices =["y","n"])
        if grafikYg.lower() == "y":
            console.print("[bold bright_yellow]Silakan Tutup jendela grafik untuk melanjutkan program.[/bold bright_yellow]")
            grafikLineYoGoals(besaranMenabungHari, targetBesaranMenabung, yoGoals)
            console.print("[bold bright_white]Jendela Grafik ditutup.[/bold bright_white]")     

        # Ekspor PDF untuk Yo-Goals
        eksporyg = Prompt.ask("[bold bright_blue]Ingin ekspor hasil ke PDF?[/bold bright_blue]", choices=["y", "n"])
        if eksporyg.lower() == "y":
            eksporPDFYoGoals(namaTargetMenabung, formatRupiah(besaranMenabungHari), formatRupiah(targetBesaranMenabung), yoGoals)

    # Kembali ke Halaman Utama
    elif pilihanPerhitungan == "3":
        return True

    # Kembali ke Halaman Utama
    kembali = Prompt.ask("[bold bright_yellow]\nKetik 'Q/q' untuk kembali ke menu utama[/bold bright_yellow]", choices=["Q", "q"])
    if kembali.lower() == "q":
        progressBar()
        return True
    return False