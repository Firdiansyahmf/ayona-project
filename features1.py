# Pustaka Rich
from rich.console import Console  # Menyorot teks
from rich.panel import Panel  # Menyorot teks
from rich.prompt import Prompt  # Input interaktif
from rich import print  # Warna teks

# Library Lainnya
from fpdf import FPDF  # Impor PDF
from matplotlib import pyplot as plt
from matplotlib import style
from rich.table import Table #Membuat Tabel
from matplotlib.ticker import FuncFormatter
import os #Supaya file ekspor PDF terunduh di direktori downloads

# Standar Pustaka Python (datetime)
from datetime import datetime

# Impor fungsi progressBar, formatRupiah, inputTanggal, hitungJumlahPengeluaran
from utils import progressBar, formatRupiah, inputTanggal, hitungJumlahPengeluaran, quickSort, quickSortDesc

# Buat objek Console dari pustaka Rich
console = Console()

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
    table.add_column ("Tipe Waktu Pemasukan", justify = "center", style = "cyan", no_wrap = True)
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
        str(tipeWaktuPengeluaran), 
        str(tanggalPengeluaran),
        str(jumlahPengeluaranRp),
        str(jumlahPemasukanBersihRp)
    )
    print(table)
    
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
    for i, val in enumerate(y):
        # Menggunakan fungsi formatRupiah untuk memformat angka
        formattedValue = formatRupiah(val)
        plt.text(i, val, f'{formattedValue}', ha='center', va='bottom', color='black', fontsize=10)

    ax.set_title('Yo-Managements Graphsite by Ayona')
    ax.set_ylabel('JUMLAH / QTY')
    ax.set_xlabel('GRAFIK KAS')

    # Set Teks Label pada Garis X yang horizontal
    a = "Pemasukan pada \n" + tanggalPemasukan
    b = "Pengeluaran pada \n" + tanggalPengeluaran
    c = "Pemasukan Bersih"
    ax.set_xticks(x)
    ax.set_xticklabels((a, b, c))

    # Format label pada sumbu Y
    def rupiah_formatter(x, pos):
        return formatRupiah(x)
    ax.yaxis.set_major_formatter(FuncFormatter(rupiah_formatter))

    # Menampilkan Grafik
    plt.show()

#Fungsi untuk mengekspor catatan rekomendasi keuangan ke PDF
def eksporPDF(
    tipeWaktuPemasukan, 
    tanggalPemasukan, 
    jumlahPemasukanRp, 
    tipeWaktuPengeluaran, 
    tanggalPengeluaran, 
    jumlahPengeluaranRp, 
    jumlahPemasukanBersihRp
):
    jumlahPemasukan = float(jumlahPemasukanRp.replace(".", "").replace("Rp", "").replace(",", ".").strip())
    jumlahPengeluaran = float(jumlahPengeluaranRp.replace(".", "").replace("Rp", "").replace(",", ".").strip())
    jumlahPemasukanBersih = float(jumlahPemasukanBersihRp.replace(".", "").replace("Rp", "").replace(",", ".").strip())

    #Menentukan persentase tabungan sesuai tipe waktu pemasukan
    if tipeWaktuPemasukan == "hari":
        persentaseTabungan = 0.05  # 5% untuk pemasukan harian
    elif tipeWaktuPemasukan == "minggu":
        persentaseTabungan = 0.10  # 10% untuk pemasukan mingguan
    elif tipeWaktuPemasukan == "bulan":
        persentaseTabungan = 0.20  # 20% untuk pemasukan bulanan
    elif tipeWaktuPemasukan == "tahun":
        persentaseTabungan = 0.20  # 20% untuk pemasukan tahunan
    else:
        persentaseTabungan = 0.20  # Default 20% jika tipe tidak dikenal

    tabunganDisarankan = jumlahPemasukan * persentaseTabungan
    sisaPemasukan = jumlahPemasukanBersih - tabunganDisarankan
    pdf = FPDF()
    pdf.add_page()
    
    #Header
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, txt="Catatan Rekomendasi Keuangan", ln=True, align='C')
    pdf.ln(10) 

    #Detail Ekspor
    pdf.set_font("Arial", size=12) 
    pdf.cell(0, 10, txt=f"Tipe waktu pemasukan : {tipeWaktuPemasukan}", ln=True, align='L')
    pdf.cell(0, 10, txt=f"Tanggal pemasukan : {tanggalPemasukan}", ln=True, align='L')
    pdf.cell(0, 10, txt=f"Jumlah pemasukan Anda : {jumlahPemasukanRp}", ln=True, align='L')
    pdf.cell(0, 10, txt=f"Tipe waktu pengeluaran : {tipeWaktuPengeluaran}", ln=True, align='L')
    pdf.cell(0, 10, txt=f"Tanggal pengeluaran : {tanggalPengeluaran}", ln=True, align='L')
    pdf.cell(0, 10, txt=f"Jumlah pengeluaran Anda : {jumlahPengeluaranRp}", ln=True, align='L')
    pdf.cell(0, 10, txt=f"Pemasukan bersih Anda : {jumlahPemasukanBersihRp}", ln=True, align='L')
    pdf.cell(0, 10, txt=f"Saran tabungan: Sisihkan {persentaseTabungan*100}% dari pemasukan Anda untuk tabungan investasi/pengeluaran darurat.", ln=True, align='L')
    pdf.cell(0, 10, txt=f"Tabungan yang disarankan: {formatRupiah(tabunganDisarankan)}", ln=True, align='L')
    pdf.cell(0, 10, txt=f"Sisa uang setelah ditabung: {formatRupiah(sisaPemasukan)}", ln=True, align='L')

    #Simpan PDF
    unduhPath = os.path.join(os.path.expanduser("~"), "Downloads")
    namaFileAwal = "Catatan_Rekomendasi_Keuangan"
    angkaUrut = 1
    while True:
        namaFile = f"{namaFileAwal} ({angkaUrut}).pdf"
        lokasiFile = os.path.join(unduhPath, namaFile)
        if not os.path.exists(lokasiFile):
            break
        angkaUrut += 1

    pdf.output(lokasiFile)
    print(f"Hasil berhasil diekspor ke [bold green]'Catatan Rekomendasi Keuangan.pdf'[/bold green]")

# Fungsi untuk membuat saran keuangan
def saranKeuangan(jumlahPemasukan, jumlahPengeluaran, jumlahPemasukanBersih, tipeWaktuPemasukan):
    if tipeWaktuPemasukan == "hari":
        persentaseTabungan = 0.05  # 5% untuk pemasukan harian
    elif tipeWaktuPemasukan == "minggu":
        persentaseTabungan = 0.10  # 10% untuk pemasukan mingguan
    elif tipeWaktuPemasukan == "bulan":
        persentaseTabungan = 0.20  # 20% untuk pemasukan bulanan
    elif tipeWaktuPemasukan == "tahun":
        persentaseTabungan = 0.20  # 20% untuk pemasukan tahunan
    else:
        persentaseTabungan = 0.20  # Default 20% jika tipe tidak dikenal
    tabunganDisarankan = jumlahPemasukan * persentaseTabungan
    sisaPemasukan = jumlahPemasukanBersih - tabunganDisarankan

    # Menampilkan saran keuangan
    print(f"\n[bold bright_white]Saran Tabungan:[/bold bright_white] Sisihkan [bold bright_cyan] {persentaseTabungan*100}% [/bold bright_cyan] dari pemasukan untuk tabungan.")
    print(f"[bold bright_white]Tabungan yang disarankan:[/bold bright_white] [bold bright_cyan] {formatRupiah(tabunganDisarankan)} [/bold bright_cyan]")
    print(f"[bold bright_white]Sisa uang setelah ditabung:[/bold bright_white] [bold bright_cyan] {formatRupiah(sisaPemasukan)} [/bold bright_cyan]")
    if sisaPemasukan > 0:
        print(f"[bold bright_cyan]Rekomendasi:[/bold bright_cyan] Gunakan sisa tabungan ini untuk kebutuhan lain seperti investasi atau pengeluaran darurat.")
    else:
        print(f"[bold bright_red]Peringatan:[/bold bright_red] Anda mungkin perlu menyesuaikan pengeluaran untuk memastikan keuangan tetap ideal.")

#Inisialisasi variable global
jumlahPemasukanBersih = None

"""
Fitur 1
(main)
"""
def fiturSatu():
    # Panel
    print(Panel("Yo-Managements", style="bold bright_cyan", width=18))

    # Input tipe dan tanggal pemasukan
    tipeWaktuPemasukan = Prompt.ask("[bold bright_cyan]Masukkan tipe waktu untuk pemasukan[/bold bright_cyan]", 
                                    choices=["hari", "minggu", "bulan", "tahun"])
    tanggalPemasukan = inputTanggal("pemasukan")

    # Input jumlah pemasukan
    while True:
        jumlahPemasukan = Prompt.ask("[bold bright_cyan]Masukkan jumlah pemasukan[/bold bright_cyan]")
        if jumlahPemasukan.isdigit():
            jumlahPemasukan = float(jumlahPemasukan)
            break
        else:
            print("[bold bright_red]Input tidak valid. Harap masukkan angka positif.[/bold bright_red]")

    # Input tipe dan tanggal pengeluaran
    tipeWaktuPengeluaran = Prompt.ask("[bold bright_cyan]Masukkan tipe waktu untuk pengeluaran[/bold bright_cyan]", 
                                    choices=["hari", "minggu", "bulan", "tahun"])
    tanggalPengeluaran = inputTanggal("pengeluaran")

    # Input jumlah pengeluaran
    jumlahPengeluaran = hitungJumlahPengeluaran()

    # Hitung pemasukan bersih
    global jumlahPemasukanBersih
    jumlahPemasukanBersih = jumlahPemasukan - jumlahPengeluaran

    # Tampilkan catatan rekomendasi keuangan
    progressBar()
    print(Panel("Catatan Rekomendasi Keuangan", style="bold bright_cyan", width=15))
    print(f"[bold bright_white]Tipe waktu pemasukan\t: {tipeWaktuPemasukan}[/bold bright_white]")
    print(f"[bold bright_white]Tanggal pemasukan \t: {tanggalPemasukan}[/bold bright_white]")
    print(f"[bold bright_white]Jumlah pemasukan Anda\t: {formatRupiah(jumlahPemasukan)}[/bold bright_white]")
    print(f"[bold bright_white]Tipe waktu pengeluaran\t: {tipeWaktuPengeluaran}[/bold bright_white]")
    print(f"[bold bright_white]Tanggal pengeluaran\t: {tanggalPengeluaran}[/bold bright_white]")
    print(f"[bold bright_white]Jumlah pengeluaran Anda\t: {formatRupiah(jumlahPengeluaran)}[/bold bright_white]")
    print(f"[bold bright_white]Pemasukan bersih Anda\t: {formatRupiah(jumlahPemasukanBersih)}[/bold bright_white]")
    
    # Impor variabel global
    from utils import untukCatatan, arrPengeluaran

    # Rincian Pengeluaran (Konsisi 2/2)
    if untukCatatan == True:
        print(f"[bold bright_yellow]\nRincian Pengeluaran:[/bold bright_yellow]")
        while True:
            # Tampilkan Default
            for record in arrPengeluaran:
                print(f"[bold bright_yellow]{formatRupiah(record)}[/bold bright_yellow]")
            # Sorting
            sorting = Prompt.ask(f"[bold bright_cyan]Sorting rincian pengeluaran?\n[bold bright_dark]Ketik '1' untuk sorting dari terkecil dan '2' dari terbesar atau ketik 'n' jika tidak[/bold bright_dark][/bold bright_cyan]", choices=["1","2","n"])
            if sorting == "1":
                print(f"[bold bright_yellow]\nRincian Pengeluaran dari Terkecil:[/bold bright_yellow]")
                arrPengeluaran = quickSort(arrPengeluaran)
            elif sorting == "2":
                print(f"[bold bright_yellow]\nRincian Pengeluaran dari Terbesar:[/bold bright_yellow]")
                arrPengeluaran = quickSortDesc(arrPengeluaran)
            elif sorting.lower() == "n":
                break

    # Saran Keuangan
    saranKeuangan(jumlahPemasukan, jumlahPengeluaran, jumlahPemasukanBersih, tipeWaktuPemasukan)
    
    # Pilihan Catatan Rekomendasi Keuangan dalam Bentuk Tabel
    tabel = Prompt.ask(f"[bold bright_cyan]Lihat dalam bentuk tabel?[/bold bright_cyan]", 
                    choices =["y","n"])
    if tabel.lower() == "y":
        tabelKeuangan(
            tipeWaktuPemasukan, 
            tanggalPemasukan, 
            formatRupiah(jumlahPemasukan), 
            tipeWaktuPengeluaran, 
            tanggalPengeluaran, 
            formatRupiah(jumlahPengeluaran), 
            formatRupiah(jumlahPemasukanBersih)
        )

    # Pilihan untuk menampilkan Grafik
    tampilGrafik = Prompt.ask("[bold bright_cyan]Lihat dalam bentuk grafik?[/bold bright_cyan]", choices=["y","n"])
    if tampilGrafik.lower() == "y":
        console.print("[bold bright_yellow]Silakan Tutup jendela grafik untuk melanjutkan program.[/bold bright_yellow]")
        grafikLine(
            tipeWaktuPemasukan, 
            tanggalPemasukan, 
            jumlahPemasukan, 
            tipeWaktuPengeluaran, 
            tanggalPengeluaran, 
            jumlahPengeluaran, 
            jumlahPemasukanBersih
        )
        console.print("[bold bright_white]Jendela grafik ditutup.[/bold bright_white]")


    # Pilihan ekspor ke PDF
    eksporKePDF = Prompt.ask("[bold bright_cyan]Ingin ekspor hasil ke PDF?[/bold bright_cyan]", 
                        choices=["y", "n"])
    if eksporKePDF.lower() == "y":
        eksporPDF(
        tipeWaktuPemasukan, 
            tanggalPemasukan, 
            formatRupiah(jumlahPemasukan), 
            tipeWaktuPengeluaran, 
            tanggalPengeluaran, 
            formatRupiah(jumlahPengeluaran), 
            formatRupiah(jumlahPemasukanBersih)
        )

    # Kembali ke Halaman Utama
    kembali = Prompt.ask("[bold bright_yellow]\nKetik 'Q/q' untuk kembali ke menu utama[/bold bright_yellow]", choices=["Q", "q"])
    if kembali.lower() == "q":
        progressBar()
        return True
    return False, jumlahPemasukanBersih