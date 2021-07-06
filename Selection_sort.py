# 找出陣列中最小值的位置
def find_smallest(arr):
    smallest_index = 0
    smallest = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest_index = i
            smallest = arr[i]

    return smallest_index


# 呼叫 'find_smallest'將舊的陣列中最小值放入新的陣列中
def selection_sort(arr):
    sorted_arr = []

    for i in range(len(arr)):
        smallest = find_smallest(arr)
        sorted_arr.append(arr.pop(smallest))

    return sorted_arr


data = [[4, 2, 5, 3, 1], [5, 3, 6, 2, 10]]
for i in range(len(data)):
    print('================================')
    print('Test ', i+1)
    print('================================')
    print('Before:', data[i])
    print('After:', selection_sort(data[i]))
