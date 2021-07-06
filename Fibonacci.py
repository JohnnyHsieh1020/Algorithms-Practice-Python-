def fibonacci(n):
    f = []
    next_num = 0
    for i in range(n):
        if i == 0 or i == 1:
            f.append(1)

        else:
            next_num = f[i - 2] + f[i - 1]
            f.append(next_num)
    return f


n = int(input('Please type a number to print a Fibonacci Sequence: '))
print(fibonacci(n))
