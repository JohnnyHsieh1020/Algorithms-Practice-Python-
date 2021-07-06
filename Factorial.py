def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


data = [1, 3, 6, 9]
for i in range(len(data)):
    print('================================')
    print('Test ', i + 1)
    print('================================')
    print(data[i], '!=', factorial(data[i]))
