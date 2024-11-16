# Pustaka Rich
import time # Time Progress Bar
from rich.progress import track # Progress Bar
from rich import print # Warna Teks

# Fungsi
def progressBar():
    for _ in track(range(2), description="[bold green]Memuat..."):
        time.sleep(0.25)
    print("")