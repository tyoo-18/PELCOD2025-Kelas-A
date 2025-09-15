# Input data
jarak = float(input("Masukkan total jarak perjalanan (km): "))
konsumsi = float(input("Masukkan konsumsi BBM (km per liter): "))
kapasitas_tangki = float(input("Masukkan kapasitas tangki (liter): "))
harga_per_liter = float(input("Masukkan harga bensin per liter (Rp): "))

# Hitung total bensin yang dibutuhkan
bensin_dibutuhkan = jarak / konsumsi

# Cek apakah dapat diskon
if bensin_dibutuhkan > 3:
    harga_per_liter = harga_per_liter - 500

# Hitung total biaya bensin
total_biaya = bensin_dibutuhkan * harga_per_liter

# Hitung berapa kali isi bensin
jumlah_isi = bensin_dibutuhkan / kapasitas_tangki
# Dibulatkan ke atas secara manual
if bensin_dibutuhkan % kapasitas_tangki != 0:
    jumlah_isi = int(jumlah_isi) + 1

# Output hasil
print("Total bensin yang dibutuhkan:", bensin_dibutuhkan, "liter")
print("Harga bensin per liter setelah diskon:", harga_per_liter)
print("Total biaya bensin: Rp", total_biaya)
print("Perkiraan jumlah kali isi bensin:", jumlah_isi, "kali")