def lcs(word_a, word_b):
    rows, cols = len(word_a), len(word_b)
    table = [[0]*(cols+1) for z in range(rows+1)]
    sub_sequence = []
    sub_sequence_size = 0
    
    for i in range(rows):
        for j in range(cols):
            
            if word_a[i] == word_b[j]:
                table[i+1][j+1] = table[i][j] + 1
                
                if table[i+1][j+1] > sub_sequence_size:
                    sub_sequence_size = table[i+1][j+1]
                    sub_sequence.append(word_a[i])
            else:
                table[i+1][j+1] = max(table[i][j+1], table[i+1][j])

    result = {'Sub Sequence':sub_sequence, 'Sub Sequence Size':sub_sequence_size}
    return result


word_a = str(input("Type the first word:"))
word_b = str(input("Type the second word:"))
print('Longest Common Subsequence:', lcs(word_a, word_b))
