def kembalian_koin(koin, jumlah):
    koin.sort(reverse=True)
    hasil = []
    for k in koin:
        while jumlah >= k:
            jumlah -= k
            hasil.append(k)
    if jumlah != 0:
        return None
    return hasil

koin = [100, 200, 500, 1000]
jumlah = 2100
output = kembalian_koin(koin, jumlah)
print(output)

# if output is not None:
#     output_str = ' + '.join(f'{x}' for x in output)
#     total_str = f'{sum(output)}'
#     print(f'{output_str} = {total_str}')
# else:
#     print('Tidak dapat memberikan kembalian dengan jumlah tersebut menggunakan koin yang tersedia.')