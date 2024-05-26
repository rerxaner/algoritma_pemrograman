arr = [1, 2, 4, 5, 7, 8, 9, 10, 12, 14, 19, 20]
dicari = 7

print(f"Mencari nilai {dicari} pada array {arr}")
ditemukan = False
batas_awal = 0
batas_akhir = len(arr) -1

while not ditemukan and batas_awal <= batas_akhir:
    pos_cari = batas_awal + (batas_akhir - batas_awal) // 2
    print(f"Posisi pencarian pada indeks {pos_cari} dengan nilai {arr[pos_cari]}")
    if arr[pos_cari] == dicari:
        ditemukan = True
    elif arr[pos_cari] > dicari:
        batas_akhir = pos_cari - 1
    else:
        batas_awal = pos_cari + 1

if ditemukan:
    print(f"Nilai {dicari} ditemukan pada indeks {pos_cari}")
else:
    print(f"Nilai {dicari} not found")