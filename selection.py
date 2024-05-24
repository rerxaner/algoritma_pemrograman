def selection_sort(list):
    iterasi = 0
    for i in range(len(list) - 1):
        minimal = i
        for j in range(i + 1, len(list)):
            if list[j] < list[minimal]:
                minimal = j
        iterasi += 1
        list[i], list[minimal] = list[minimal], list[i]
        print(iterasi, list)

list = [2, 3, 4, 1, 5]
print(f"Data yang di Selection sort: {list}")
print('Proses pengerjaan:')
selection_sort(list)
print(f"Hasil Selection sort: {list}")