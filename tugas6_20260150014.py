import modul_konversi

print('========================================')
print('KALKULATOR KONSUMSI DAYA PERANGKAT EDGE')
print('========================================')

# Input dari pengguna
nama = input('Masukkan Nama Perangkat : ')
volt = float(input('Masukkan Voltase (Volt) : '))
ampere = float(input('Masukkan Arus (Ampere) : '))

# Panggil fungsi dari modul
daya = modul_konversi.hitung_daya_watt(volt, ampere)
kategori = modul_konversi.kategori_konsumsi(daya)

# Output
print('========================================')
print('HASIL ANALISIS DAYA AI')
print('========================================')
print('Nama Perangkat :', nama)
print(f'Daya Terhitung : {daya:.2f} Watt')
print('Kategori Daya  :', kategori)