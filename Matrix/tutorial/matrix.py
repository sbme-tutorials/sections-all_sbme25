import copy


# A static function to create an empty matrix with size mxn
def dummy_matrix(m, n):
    new_mat = []
    for i in range(m):
        new_row = []
        for j in range(n):
            new_row.append(0)
        new_mat.append(new_row)
    return Matrix(new_mat)


class Matrix:

    def __init__(self, two_dim_arr):
        self.matrix = two_dim_arr
        self.rows_count = len(two_dim_arr)
        self.columns_count = len(two_dim_arr[0])

    def print(self):
        for row in range(self.rows_count):
            for col in range(self.columns_count):
                print(self.matrix[row][col], end=' ')
            print('\n')
        return self

    def add(self, other_matrix):
        # The copy.deepcopy() method makes a copy of the given list instead of mutating the original list
        # if you just wrote `new_mat = self.matrix` this will result in strange result
        new_mat = copy.deepcopy(self.matrix)
        if self.rows_count == other_matrix.rows_count and self.rows_count == other_matrix.rows_count:
            for i in range(self.rows_count):
                for j in range(self.columns_count):
                    new_mat[i][j] += other_matrix.matrix[i][j]
        return Matrix(new_mat)

    def subtract(self, other_matrix):
        new_mat = copy.deepcopy(self.matrix)
        if self.rows_count == other_matrix.rows_count and self.rows_count == other_matrix.rows_count:
            for i in range(self.rows_count):
                for j in range(self.columns_count):
                    new_mat[i][j] -= other_matrix.matrix[i][j]
        return Matrix(new_mat)

    def mult(self, other_mat):
        dummy = dummy_matrix(self.rows_count, other_mat.columns_count)
        for row in range(dummy.rows_count):
            for col in range(dummy.columns_count):
                for i in range(self.rows_count):
                    dummy.matrix[row][col] += self.matrix[row][i] * other_mat.matrix[i][col]
        return dummy
