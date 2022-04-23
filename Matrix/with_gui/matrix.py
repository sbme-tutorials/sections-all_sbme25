class Matrix:

    def __init__(self, data: list[list[int]]):

        self.data = data
        self.row = len(data)
        self.col = len(data[0])

    def add(self, matrix):

        if self.row == matrix.row and self.col == matrix.col:
            result = self.data.copy()
            for i in range(matrix.row):
                for j in range(matrix.col):
                    result[i][j] += matrix.data[i][j]

        return Matrix(result)

    def subtract(self, matrix):
        if self.row == matrix.row and self.col == matrix.col:
            result = self.data.copy()
            for i in range(matrix.row):
                for j in range(matrix.col):
                    result.data[i][j] -= matrix.data[i][j]

        return Matrix(result)

    def multiply(self, matrix):

        result = []
        if self.col == matrix.row:
            for i in range(self.row):
                result.append([])
                for j in range(self.row):
                    result[i].append(0)

            for i in range(self.row):
                for j in range(matrix.row):
                    for k in range(matrix.col):
                        result[i][j] += self.data[i][k] * matrix.data[k][j]

        return Matrix(result)

    def __str__(self):

        result = ""
        for i in range(self.row):
            for j in range(self.col):
                result += str(self.data[i][j]) + " "
            result += "\n"

        return result
