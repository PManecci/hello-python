def insertion_sort(arr):
    for i in range(1, len(arr)):
        cur_num = arr[i]
        while i > 0 and arr [i-1] > cur_num:
            print("Swapping " + str(cur_num) + " and " + str(arr[i-1]))
            arr[i] = arr[i-1]
            i -= 1
        arr[i] = cur_num

arr = [9, 5, -2, 6]
insertion_sort(arr)
print(arr)