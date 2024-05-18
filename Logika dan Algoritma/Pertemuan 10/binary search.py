def binary_search(arr, low, high, x):
    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val == x:
            return mid
        elif mid_val < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1

arr = [3, 6, 9, 13, 16, 26, 38, 58]

search_values = [13, 16, 10]

for val in search_values:
    result = binary_search(arr, 0, len(arr) - 1, val)
    if result != -1:
        print(val, " ditemukan pada urutan ke ", result)
    else:
        print(val, "tidak ditemukan dalam deretan angka")
        
"""
Nama Kelompok
1. Dio Herlambang (17230526)
2. Fajar Ramadhan (17230511)
3. Ambrusius Paska Dipta (17230562)
4. Haykal Ryan Andre (17230519)
5. Muhammad Nasal Ekaputra (17230564)
"""