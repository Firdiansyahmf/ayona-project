def garis_keren():
    garis_keren = print("--------------------------------------------")
    return garis_keren


print("Selamat Datang di Ayona")
print("Pilih Opsi Berikut:")
print("1. Yo-Managements")
print("2. Perhitungan Tabungan")
print("3. Bantuan Pengguna")

input_fitur = int(input("Masukkan (1/2/3) Fitur yang ingin anda pilih: "))

if input_fitur == 1:
    garis_keren()
    print("Pilihan Bagus! Ini adalah Fitur 1. Yo-Managements")
    garis_keren()
elif input_fitur == 2:
    garis_keren()
    print("Pilihan Keren! Ini adalah Fitur 2. Perhitungan Tabungan, yang memuat 2 Fitur yakni Yo-Savers & Yo-Goals")
    garis_keren()
elif input_fitur == 3:
    garis_keren()
    print("Nice one! Ini adalah Fitur 3. Bantuan Pengguna")
    garis_keren()


