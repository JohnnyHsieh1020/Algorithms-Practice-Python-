def binary_search(data, target):
    bottom = 0
    top = len(data) - 1
    sorted_data = sorted(data) # 做搜尋前需要將資料排序
    print('Sorted Data: ', sorted_data)
    print('Search: ', target)

    while top >= bottom:
        search = (bottom + top) // 2  # 整除無條件捨去法

        if sorted_data[search] == target:
            return 'index: ' + str(search)
        elif sorted_data[search] > target:
            top = search - 1
        else:
            bottom = search + 1

    return 'Not Found!'


data = [4, 2, 5, 3, 1]
target = [3, -1, 6]
for i in range(len(target)):
    print('================================')
    print('Test ', i+1)
    print('================================')
    print(binary_search(data, target[i]))
