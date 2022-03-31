from numpy import min_scalar_type


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range (i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        print("Swapping " + str(arr[min_index]) + " and " + str(arr[i]))
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [9, 5, -2, 6]
selection_sort(arr)
print(arr)