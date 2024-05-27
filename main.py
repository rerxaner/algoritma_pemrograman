def kelola_keuangan(anggaran_harian, pengeluaran):
    sisa_anggaran = anggaran_harian
    pengeluaran_dikelola = {}

    for kategori, jumlah in pengeluaran.items():
        if jumlah <= sisa_anggaran:
            pengeluaran_dikelola[kategori] = jumlah
            sisa_anggaran -= jumlah
        else:
            pengeluaran_dikelola[kategori] = sisa_anggaran
            sisa_anggaran = 0
            break

    if sisa_anggaran > 0:
        pengeluaran_dikelola['sisa'] = sisa_anggaran

    return pengeluaran_dikelola

# Contoh penggunaan:
anggaran_harian = 50000
pengeluaran = {
    'makanan': 20000,
    'transportasi': 15000,
    'minuman': 10000,
}

pengeluaran_dikelola = kelola_keuangan(anggaran_harian, pengeluaran)
print("Pengeluaran Harian yang Dikelola: ", pengeluaran_dikelola)
