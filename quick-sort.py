def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr) - 1)

def quick_sort_helper(arr, start, end):
    if (start >= end):
        return
    pivot = partition(arr, start, end)
    quick_sort_helper(arr, start, pivot - 1)
    quick_sort_helper(arr, pivot + 1, end)

def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <=pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1 

arr = [9, 5, -2, 6]
quick_sort(arr)
print(arr)