def get_col(lst_arg, index):
    return [ el[index] for el in lst_arg ]

def set_col(matrix, col, j):
    i = 0
    for line in matrix:
        line[j] = col[i]
        i = i + 1
    return matrix 