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

# Impor fungsi progressBar, formatRupiah
from utils import progressBar, formatRupiah

# Buat objek Console dari pustaka RiQ
# ch
console = Console()

# Fungsi input tanggal berdasarkan tipe (pemasukan/pengeluaran)
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

#Fungsi untuk membuat tabel
def tabelKeuangan (
        tipeWaktuPemasukan, 
        tanggalPemasukan, 
        jumlahPemasukanRp, 
        tipeWaktuPengeluaran, 
        tanggalPengeluaran, 
        jumlahPengeluaranRp, 
        jumlahPemasukanBersihRp
):

    table = Table(title = "Catatan Rekomendasi Keuangan")

    table.add_column ("Tipe Waktu Pemasukan",justify = "center", style = "cyan", no_wrap = True)
    table.add_column ("Tanggal Pemasukan", justify = "center", style = "magenta")
    table.add_column ("Jumlah Pemasukan", justify = "center", style = "green")
    table.add_column ("Tipe Waktu Pengeluaran", justify = "center", style = "cyan")   
    table.add_column ("Tanggal Pengeluaran", justify = "center", style = "magenta") 
    table.add_column ("Jumlah Pengeluaran", justify = "center", style = "red")    
    table.add_column ("Jumlah Pemasukan Bersih", justify = "center", style = "green")

    table.add_row (
        str(tipeWaktuPemasukan),
        str(tanggalPemasukan),
        str(jumlahPemasukanRp), 
        str (tipeWaktuPengeluaran), 
        str (tanggalPengeluaran),
        str (jumlahPengeluaranRp),
        str (jumlahPemasukanBersihRp)
    )

    console.print(table)

# Fungsi untuk membuat grafik
def grafikLine(
    tipeWaktuPemasukan, 
    tanggalPemasukan, 
    jumlahPemasukan, 
    tipeWaktuPengeluaran, 
    tanggalPengeluaran, 
    jumlahPengeluaran, 
    jumlahPemasukanBersih
):
    
    # style.use('ggplot')
    # x = Garis X horizontal, y = Garis Y veritikal
    x = [0, 1, 2]
    pemasukan = int(jumlahPemasukan)
    pengeluaran = int(jumlahPengeluaran)
    bersih = int(jumlahPemasukanBersih)
    y = [pemasukan, pengeluaran, bersih]
    fig, ax = plt.subplots()

    # Definisikan Grafik apa disini Grafiknya == Bar(Batang)
    ax.bar(x, y, align='center',  color=['blue', 'red', 'green'])

    # Menampilkan Teks di dalam Grafiknya sesuai nilai Y
    for i, y in enumerate(y):
        plt.text(i, y-10000, f'{y:,}', ha='center', va='bottom', color='black', fontsize=10)

    ax.set_title('Yo-Managements Graphsite by Ayona')
    ax.set_ylabel('JUMLAH / QTY')
    ax.set_xlabel('GRAFIK KAS')

    # Set Teks Label pada Garis X yang horizontal
    ax.set_xticks(x)
    a = "Pemasukan pada \n" + tanggalPemasukan
    b = "Pengerluaran pada \n" + tanggalPengeluaran
    c = "Pemasukan Bersih"
    ax.set_xticklabels((a, b, c))

    # Menampilkan Grafik
    # plt.grid(True)
    plt.show()

# Fungsi untuk mengekspor catatan rekomendasi keuangan ke PDF
def eksporPDF(
        tipeWaktuPemasukan, 
        tanggalPemasukan, 
        jumlahPemasukanRp, 
        tipeWaktuPengeluaran, 
        tanggalPengeluaran, 
        jumlahPengeluaranRp, 
        jumlahPemasukanBersihRp
):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12) 
    
    # Header
    pdf.cell(200, 10, txt="Catatan Rekomendasi Keuangan", ln=True, align='C')
    pdf.ln(10) 

    # Detail Ekspor
    pdf.cell(0, 10, txt=f"Tipe waktu pemasukan : {tipeWaktuPemasukan}", ln=True, align='L')
    pdf.cell(0, 10, txt=f"Tanggal pemasukan : {tanggalPemasukan}", ln=True, align='L')
    pdf.cell(0, 10, txt=f"Jumlah pemasukan Anda : {jumlahPemasukanRp}", ln=True, align='L')
    pdf.cell(0, 10, txt=f"Tipe waktu pengeluaran : {tipeWaktuPengeluaran}", ln=True, align='L')
    pdf.cell(0, 10, txt=f"Tanggal pengeluaran : {tanggalPengeluaran}", ln=True, align='L')
    pdf.cell(0, 10, txt=f"Jumlah pengeluaran Anda : {jumlahPengeluaranRp}", ln=True, align='L')
    pdf.cell(0, 10, txt=f"Pemasukan bersih Anda : {jumlahPemasukanBersihRp}", ln=True, align='L')
    
    # Simpan file PDF
    pdf.output("Catatan Rekomendasi Keuangan.pdf")
    console.print("Hasil berhasil diekspor ke [bold green]'Catatan Rekomendasi Keuangan.pdf'[/bold green]")

"""
Fitur 1
(main)
"""
def fiturSatu():
    console.print(Panel("Yo-Managements", style="bold bright_cyan", width=18))

    # Input tipe dan tanggal pemasukan
    tipeWaktuPemasukan = Prompt.ask("[bold bright_green]Masukkan tipe waktu untuk pemasukan[/bold bright_green]", 
                                    choices=["hari", "minggu", "bulan", "tahun"])
    tanggalPemasukan = inputTanggal("pemasukan")

    # Input jumlah pemasukan
    while True:
        jumlahPemasukan = Prompt.ask("[bold bright_green]Masukkan jumlah pemasukan[/bold bright_green]")
        if jumlahPemasukan.isdigit():
            jumlahPemasukan = float(jumlahPemasukan)
            break
        else:
            console.print("[bold bright_red]Input tidak valid. Harap masukkan angka positif.[/bold bright_red]")

    # Input tipe dan tanggal pengeluaran
    tipeWaktuPengeluaran = Prompt.ask("[bold bright_green]Masukkan tipe waktu untuk pengeluaran[/bold bright_green]", 
                                      choices=["hari", "minggu", "bulan", "tahun"])
    tanggalPengeluaran = inputTanggal("pengeluaran")

    # Input jumlah pengeluaran
    jumlahPengeluaran = 0
    while True:
        tanyaPengeluaran = Prompt.ask("[bold bright_green]Masukkan jumlah pengeluaran, [bold bright_black]atau ketik 'hitung' untuk menghitung total dari item[/bold bright_black][/bold bright_green]")
        if tanyaPengeluaran.isdigit():
            jumlahPengeluaran = float(tanyaPengeluaran)
            break
        elif tanyaPengeluaran.lower() == "hitung":
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

    # Hitung pemasukan bersih dan format ke rupiah
    jumlahPemasukanBersih = jumlahPemasukan - jumlahPengeluaran
    jumlahPemasukanRp = formatRupiah(jumlahPemasukan)
    jumlahPengeluaranRp = formatRupiah(jumlahPengeluaran)
    jumlahPemasukanBersihRp = formatRupiah(jumlahPemasukanBersih)

    # Tampilkan rekomendasi keuangan
    progressBar()
    console.print(Panel("Catatan Rekomendasi Keuangan", style="bold bright_cyan", width=15))
    console.print(f"[bold bright_cyan]Tipe waktu pemasukan\t: {tipeWaktuPemasukan}[/bold bright_cyan]")
    console.print(f"[bold bright_cyan]Tanggal pemasukan \t: {tanggalPemasukan}[/bold bright_cyan]")
    console.print(f"[bold bright_cyan]Jumlah pemasukan Anda\t: {jumlahPemasukanRp}[/bold bright_cyan]")
    console.print(f"[bold bright_cyan]Tipe waktu pengeluaran\t: {tipeWaktuPengeluaran}[/bold bright_cyan]")
    console.print(f"[bold bright_cyan]Tanggal pengeluaran\t: {tanggalPengeluaran}[/bold bright_cyan]")
    console.print(f"[bold bright_cyan]Jumlah pengeluaran Anda\t: {jumlahPengeluaranRp}[/bold bright_cyan]")
    console.print(f"[bold bright_cyan]Pemasukan bersih Anda\t: {jumlahPemasukanBersihRp}[/bold bright_cyan]")
    
    # Pilihan Catatan Rekomendasi Keuangan dalam Bentuk Tabel
    tabel = Prompt.ask("[bold bright_blue]Lihat dalam bentuk tabel?[/bold bright_blue]", 
                       choices =["y","n"])
    if tabel.lower() == "y":
        tabelKeuangan(
            tipeWaktuPemasukan, 
            tanggalPemasukan, 
            jumlahPemasukanRp, 
            tipeWaktuPengeluaran, 
            tanggalPengeluaran, 
            jumlahPengeluaranRp, 
            jumlahPemasukanBersihRp
        )

    # Pilihan untuk menampilkan Grafik
    tampilGrafik = Prompt.ask("[bold bright_blue]Lihat dalam bentuk grafik?[/bold bright_blue]", choices=["y","n"])
    if tampilGrafik.lower() == "y":
        grafikLine(
            tipeWaktuPemasukan, 
            tanggalPemasukan, 
            jumlahPemasukan, 
            tipeWaktuPengeluaran, 
            tanggalPengeluaran, 
            jumlahPengeluaran, 
            jumlahPemasukanBersih
        )

    # Pilihan ekspor ke PDF
    eksporKePDF = Prompt.ask("[bold bright_blue]Ekspor ke PDF?[/bold bright_blue]", 
                           choices=["y", "n"])
    if eksporKePDF.lower() == "y":
        eksporPDF(
        tipeWaktuPemasukan, 
            tanggalPemasukan, 
            jumlahPemasukanRp, 
            tipeWaktuPengeluaran, 
            tanggalPengeluaran, 
            jumlahPengeluaranRp, 
            jumlahPemasukanBersihRp
        )

    # Kembali ke Halaman Utama
    kembali = Prompt.ask("[bold bright_blue]Ketik 'Q/q' untuk kembali ke menu utama[/bold bright_blue]", choices=["Q", "q"])
    if kembali.lower() == "q":
        progressBar()
        return True
    return False