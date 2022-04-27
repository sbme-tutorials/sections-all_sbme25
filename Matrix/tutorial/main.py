from matrix import Matrix

if __name__ == '__main__':
    # Test examples
    matrix1 = Matrix([[3, 12, 4], [5, 6, 8], [1, 0, 2]])
    matrix2 = Matrix([[7, 3, 8], [11, 9, 5], [6, 8, 4]])

    # You can now print the matrix using two ways
    # matrix1.print()
    # print(matrix1)

    print("matrix1 + matrix2 =")
    matrix1.add(matrix2).print()
    # you can use method chaining addition e.g: matrix1.add(matrix2).add(matrix2).add(<etc>).print()

    print("matrix1 - matrix2 =")
    matrix1.subtract(matrix2).print()

    print("matrix1 X matrix2 =")
    matrix1.mult(matrix2).print()
