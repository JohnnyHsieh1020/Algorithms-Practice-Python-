def sum(data):
    if data == []:
        return 0
    return data[0] + sum(data[1:])


data = [[1, 3, 6, 9], [1]]
for i in range(len(data)):
    print('================================')
    print('Test ', i + 1)
    print('================================')
    print('Sum =', sum(data[i]))
