def create_2dim_list():
    n, m = 3, 4
    list_2d = [[0 for row in range(m)] for col in range(n)]
    print(list_2d)
    new_list = [[(row * col) for row in range(m)] for col in range(n)]
    print(new_list)


def create_2dim_list_by_loop():
    n, m = 3, 4
    lis = [[0] * m for _ in range(n)]  # Initialize a 2D list with zeros
    print(lis[0][0])
    for i in range(n):
        for j in range(m):
            lis[i][j] = i * j  # Assign values based on i * j
    print(lis)


def sum_of_matrix():
    lis2d = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    sum_matrix = []
    for i in range(len(lis2d[0])):
        tot = 0
        for j in range(len(lis2d)):
            print(lis2d[j][i])
            tot = tot + lis2d[j][i]
            print('tot', tot)
        sum_matrix.append(tot)

    print(sum_matrix)


def transpose_matrix():
    """
opt =
[1, 5, 9],[2, 6, 10],[3, 7, 11],[4, 8, 12]

"""
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    exp_matrix = [[0 for row in range(len(matrix))] for col in range(len(matrix[0]))]
    print(exp_matrix)
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            exp_matrix[col][row] = matrix[row][col]
    print(exp_matrix)


def multiplication():
    """
    A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]
optput--
  [
58 64
139 154 ]

    """
if __name__ == '__main__':
    # create_2dim_list()
    # create_2dim_list_by_loop()
    # sum_of_matrix()
    transpose_matrix()
