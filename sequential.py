list = [4, 6, 7, 9, 5, 3]
dicari = 5  # ! elemen yang dicari
index = -1 # ! posisi elemen yang dicari

# ? perulanangan untuk memeriksa tiap elemnt pada list
for i in range(len(list)):
    if list[i]== dicari:  # ? jika ditemukan
        index = i # ! index diisi dengan nilai i (nilai saat ini)
        break # ! dihentikan

if index == -1: # ! jika index masih terisi dengan nilai -1 maka tidak ditemukan
    print (f"nilai {dicari} tidak ditemukan")
else:  # ! sebaliknya berarti nilai yang dicari ditemukan pada indeks yang sama dengan nilai index
    print(f"nilai {dicari} ditemukan pada indeks ke-{index}")