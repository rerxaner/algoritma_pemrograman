import datetime
import os

total = []
daftar_makanan = []

print('\n----------------------------------')
print('\t  WARUNG WARMINDO')
print('----------------------------------')

def daftar_barang():
    print(' No |  Nama Makanan  |  Harga')
    print('----------------------------------')
    print(' 1. |  Mie Ayam      |  15.000')
    print(' 2. |  Mie Rebus     |  10.000')
    print(' 3. |  Mie Jumbo     |  12.000')
    print(' 4. |  Mie Goreng    |  10.000')
    print(' 5. |  Ayam Bakar    |  14.000')
    print(' 6. |  Ikan Bakar    |  13.000')
    print('----------------------------------')

    nomor_makanan = int(input('Masukkan nomor makanan  : '))
    harga_makanan = 0
    nama_makanan = ""

    if nomor_makanan == 1:
        harga_makanan = 15000
        nama_makanan = "Mie Ayam"
    elif nomor_makanan == 2:
        harga_makanan = 10000
        nama_makanan = "Mie Rebus"
    elif nomor_makanan == 3:
        harga_makanan = 12000
        nama_makanan = "Mie Jumbo"
    elif nomor_makanan == 4:
        harga_makanan = 10000
        nama_makanan = "Mie Goreng"
    elif nomor_makanan == 5:
        harga_makanan = 14000
        nama_makanan = "Ayam Bakar"
    elif nomor_makanan == 6:
        harga_makanan = 13000
        nama_makanan = "Ikan Bakar"
    else:
        print('Nomor makanan tidak valid ulangi!')
        return daftar_barang()

    jumlah_makanan = int(input('Masukkan jumlah makanan : '))
    total_harga = harga_makanan * jumlah_makanan
    total.append(total_harga)
    daftar_makanan.append((nama_makanan, jumlah_makanan, total_harga))
    tambah_makanan()

def tambah_makanan():
    print('\n----------------------------------')
    tambah_lagi = input('Tambah lagi? [Y/N] \t: ').upper()

    if tambah_lagi == 'Y':
        daftar_barang()
    elif tambah_lagi == 'N':
        subtotal_makanan()
    else:
        print('Pilihan yang dimasukkan salah!')
        tambah_makanan()

def subtotal_makanan():
    print('\n----------------------------------')
    subtotal = sum(total)
    print('\tSubtotal \t: {:>8}'.format(subtotal))

    diskon = 0
    if subtotal > 300000:
        diskon = subtotal * 0.08
    elif subtotal > 200000:
        diskon = subtotal * 0.03
    elif subtotal > 150000:
        diskon = subtotal * 0.01
    else:
        diskon = 0

    bayar = int(input("Masukkan jumlah pembayar: "))
    print('\tPotongan harga \t: {:>8}'.format(diskon))

    total_akhir = subtotal - diskon
    print('\tTOTAL \t\t: {:>8}'.format(total_akhir))
    print('----------------------------------')

    print('\t\tTUNAI \t: {:>8}'.format(bayar))
    kembalian = bayar - total_akhir
    print('\tKEMBALIAN \t: {:>8}'.format(kembalian))

    cetak_rincian_pembelian(diskon, total_akhir, bayar, kembalian)

def waktu_pembelian():
    waktu = datetime.datetime.now()
    print('%02d/%02d/%04d' % (waktu.day, waktu.month, waktu.year), end='\t\t')
    print('  %02d:%02d:%02d' % (waktu.hour, waktu.minute, waktu.second))
    return waktu_pembelian

def cetak_rincian_pembelian(diskon, total_akhir, bayar, kembalian):
    os.system('cls')
    print('\n----------------------------------')
    print('\t WARUNG WARMINDO')
    print(' KOTA BENGKULU JL. KAMPUNG BALI')
    print('----------------------------------')
    waktu_pembelian()
    print('----------------------------------')

    for nama, jumlah, total_harga in daftar_makanan:
        print(f"{nama}  x{jumlah}   {total_harga // jumlah}\t: {total_harga:>8}")
    print('----------------------------------')
    print('\tPotongan harga \t: {:>8}'.format(round(diskon)))
    print('\tTUNAI \t\t: {:>8}'.format(bayar))
    print('\tTOTAL \t\t: {:>8}'.format(round(total_akhir)))
    print('\t\t\t----------')
    print('\tKEMBALIAN \t: {:>8}'.format(round(kembalian)))

    print('\n----------------------------------')
    print('\t   TERIMA KASIH')
    print('----------------------------------')

daftar_barang()

