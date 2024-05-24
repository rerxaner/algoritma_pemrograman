def bubble_sort(list):
    for j in range(len(list) - 1):
        for i in range(len(list) - 1 - j):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
            print(list)

list = [4, 2, 5, 3, 9]
print(f"Data yang di Buuble sort: {list}")
print("Proses pengerjaan:")
bubble_sort(list)
print(f"Hasil Bubble sort: {list}")