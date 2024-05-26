def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [ 7, 8, 2, 4, 9, 3, 5]
print(f"Array yang di insetion sort: {arr}")
insertion_sort(arr)
print(f"Hasil insertion sort: {arr}")