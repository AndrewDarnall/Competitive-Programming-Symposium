import numpy as np

def create_matrix(num_list: list, n: int, m: int) -> np.array:
    mat = np.zeros((n, m), dtype=int)
    index = 0
    for i in range(n):
        for j in range(m):
            mat[i][j] = num_list[index]
            index += 1
    return mat

def get_matrix_list(matrix: np.array) -> list:
    result = list()
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            result.append(matrix[i][j])
    return result