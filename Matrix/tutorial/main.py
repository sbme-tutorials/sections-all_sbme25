from matrix import Matrix

matrix1 = Matrix([[1, 2], [3, 4]])
matrix2 = Matrix([[1, 2], [3, 4]])
# matrix2 = Matrix([[1, 2, 3], [4, 5, 6], [2, 1, 4], [2, 2, 1]])
matrix3 = matrix1.add(matrix2).add(matrix1).add(matrix1)
print(matrix3.data)
