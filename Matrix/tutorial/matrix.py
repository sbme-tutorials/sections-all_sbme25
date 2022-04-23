class Matrix:

    def __init__(self, data):
        self.row = len(data)
        self.col = len(data[0])
        self.data = data

    def add(self, some_matrix):
        result = self.data.copy()
        if self.row == some_matrix.row and self.col == some_matrix.col:
            for i in range(self.row):
                for j in range(self.col):
                    result[i][j] += some_matrix.data[i][j]
        
        return Matrix(result)

    def subtract(self, matrix):
        pass

    def multiply(self, matrix):    
        pass