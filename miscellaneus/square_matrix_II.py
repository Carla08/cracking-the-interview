"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
"""

def square_spiral_matrix(matrix, n, current_fill, rotation_iter, row_to_fill):
    if current_fill == n**2:
        for _ in range(4 - (rotation_iter % 4)):
            # to leave the matrix upright
            matrix = rotate_matrix(matrix, n)

        return matrix
    else:
        if rotation_iter % 4 == 0:
            row_to_fill += 1
        __row_to_fill = matrix[row_to_fill]
        for i in range(len(__row_to_fill)):
            if __row_to_fill[i] is None:
                current_fill += 1
                __row_to_fill[i] = current_fill
            else:
                continue
        matrix = rotate_matrix(matrix, n)
        return square_spiral_matrix(matrix, n, current_fill, rotation_iter + 1, row_to_fill)


def rotate_matrix(matrix, n):
    rotated = []
    for i in range(n-1, -1, -1):
        tmp = [sublist[i] for sublist in matrix]
        rotated.append(tmp)
    return rotated


def square_spiral_matrix_ii(n):
    empty_sqr_matrix = make_empty_square_matrix(n)
    matrix = square_spiral_matrix(empty_sqr_matrix, n, 0, 0, -1)
    for lst in matrix:
        print(lst)


def make_empty_square_matrix(n):
    square_matrix = []
    for _ in range(n):
        square_matrix.append([None for _ in range(n)])
    return square_matrix

square_spiral_matrix_ii(5)