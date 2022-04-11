def merge_sort(arr): 
    n = len(arr)
    if(n<2):
        return

    mid = n//2
    left_half = arr[:mid]
    right_half = arr[mid:]
    merge_sort(left_half)
    merge_sort(right_half)

    i, j, k = 0, 0, 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1 
        k += 1

arr = [9, 5, -2, 6]
merge_sort(arr)
print(arr)