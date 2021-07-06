def find_max_num(data):
    if data == []:
        return 'None'
    if len(data) == 1:
        return data[0]
    elif data[0] > data[-1]:
        data.pop(-1)
        find_max_num(data)
        return data[0]
    else:
        data.pop(0)
        find_max_num(data)
        return data[0]


data = [[1, 3, 10, 9], [1], [1, 2], []]
for i in range(len(data)):
    print('================================')
    print('Test ', i + 1)
    print('================================')
    print('List:', data[i])
    print('Max =', find_max_num(data[i]))
