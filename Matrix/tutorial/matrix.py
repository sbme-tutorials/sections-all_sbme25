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

    def __str__(self):
        result = ""
        for row in range(self.rows_count):
            for col in range(self.columns_count):
                result += str(self.matrix[row][col]) + " "
            result += "\n"
        return result

    def print(self):
        # The point of having this way is for being able to method chain
        # on any matrix object for example:
        # matrix1.add(matrix2).print().add(matrix3) ...
        # this is possible by returning self
        print(self)
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

    # Adding the identity matrix to the original matrix from the right (Augmenting the matrix)
    def add_identity_matrix(self):
        for i in range(self.rows_count):
            for j in range(self.rows_count):
                if i == j:
                    self.matrix[i].append(1)
                else:
                    self.matrix[i].append(0)
        self.columns_count *= 2
        return self

    def get_the_right_half(self):
        # This will be used for removing the identity matrix - after inverting - from the left
        # e.g : for matrix
        # 3 12 4 1 0 0
        # 5 6 8 0 1 0
        # 1 0 2 0 0 1
        # Matrix(list).get_the_right_side(), will result in
        # 1 0 0
        # 0 1 0
        # 0 0 1
        new_mat = []
        for i in range(self.rows_count):
            new_mat.append(self.matrix[i][self.rows_count:])
        self.matrix = new_mat
        self.columns_count = self.columns_count // 2
        return self

    # Inverting the matrix
    # NOTE: this program assumes the given matrix is already invertible and non-singular
    # for more info: https://mathworld.wolfram.com/NonsingularMatrix.html

    def get_inverse(self):
        # Handling the 2x2 matrix inverse case
        if self.rows_count == 2:
            det = self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
            new_mat = [
                [self.matrix[1][1], -self.matrix[0][1]],
                [-self.matrix[1][0], self.matrix[0][0]]
            ]
            for i in range(self.rows_count):
                for j in range(self.rows_count):
                    new_mat[i][j] /= det
            # NOT IN PLACE!
            return Matrix(new_mat)

        aug_mat = self.add_identity_matrix().matrix

        for i in range(self.rows_count):
            pivot = aug_mat[i][i]

            for a in range(2 * self.rows_count):
                aug_mat[i][a] = aug_mat[i][a] / pivot

            for j in range(self.rows_count):
                if j != i:
                    pivot = aug_mat[i][i]
                    target = aug_mat[j][i]
                    ratio = -target / pivot
                    for k in range(2 * self.rows_count):
                        aug_mat[j][k] = ratio * aug_mat[i][k] + aug_mat[j][k]
        return self.get_the_right_half()
