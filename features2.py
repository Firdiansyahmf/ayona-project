# Pustaka Rich
from rich.console import Console # Menyorot Teks
from rich.panel import Panel # Menyorot Teks
from rich.prompt import Prompt # Input interaktif
from rich import print # Warna Teks

# Impor fungsi progressBar
from utils import progressBar

# Buat objek Console dari pustaka Rich
console = Console()

"""
Fungsi fitur 2
(main)
"""
def fiturDua():
    console.print(Panel("Perhitungan Tabungan", style="bold bright_cyan", width=24))

    # Kembali ke Halaman Utama
    kembali = Prompt.ask("[bold bright_blue]Ketik 'Q/q' untuk kembali ke menu utama[/bold bright_blue]", choices=["Q", "q"])
    if kembali.lower() == "q":
        progressBar()
        return True
    return False