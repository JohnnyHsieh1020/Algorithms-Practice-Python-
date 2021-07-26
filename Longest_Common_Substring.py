def lcs(word_a, word_b):
    rows, cols = len(word_a), len(word_b)
    table = [[0]*(cols+1) for z in range(rows+1)]
    sub_string_size = sub_string_addr = 0
    sub_string = ''

    for i in range(rows):
        for j in range(cols):

            if word_a[i] == word_b[j]:
                table[i+1][j+1] = table[i][j] + 1
                if sub_string_size < table[i+1][j+1]:
                    sub_string_size = table[i+1][j+1]
                    sub_string_addr = i + 1
            else:
                table[i+1][j+1] = 0

    begin = sub_string_addr - sub_string_size
    sub_string = word_a[begin:sub_string_addr]
    result = {'Sub String': sub_string, 'Sub String Size': sub_string_size}
    return result


word_a = str(input("Type the first word:"))
word_b = str(input("Type the second word:"))
print('Longest Common Substring:', lcs(word_a, word_b))
