def quick_sort(data):
    if len(data) < 2:
        return data
    else:
        pivot = data[0]
        right = [i for i in data[1:] if i > pivot]
        left = [i for i in data[1:] if i < pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


data = [[10, 5, 2, 3], [1], [2, 1], []]
for i in range(len(data)):
    print('================================')
    print('Test ', i + 1)
    print('================================')
    print('Before:', data[i])
    print('After:', quick_sort(data[i]), '\n')
