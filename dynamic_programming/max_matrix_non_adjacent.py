def maximumNonAdjacentCellsSum(matrix):
    # base case: 1x1 matrix
    # recursive first case: 2x2 matrix
    # 1) get first number and calculate the numbers that can be summed (non-adjacent)
    # 2) store the sum.
    # 3) keep the max.
    # 4) repeat the same for all the matrix elements.

    max_row, max_col = len(matrix), len(matrix[0])

    pass


def get_max_matrix_non_adjacent(max, matrix, row, col, max_row, max_col):
    # base case
    if len(matrix[row][col]) == 1:
        return matrix[row][col]

    else:
        # max of having this number (x,y) as participant of the max
        matrix_1 = _get_non_adjacent_of_x_y(row, col)

        # max of not having this number (x, y) as participant of the max
        if row + 1 < row:
            matrix_2 = _get_non_adjacent_of_x_y(row + 1, col)


def _get_non_adjacent_of_x_y(matrix, x, y):
    # need to exclude x + 1 and y + 1
    pass


matrix_basic = [1,2]
matrix_med = [[1,2], [3,4]]
matrix_adv = [[1,2,3], [4,5,6], [7,8,9]]