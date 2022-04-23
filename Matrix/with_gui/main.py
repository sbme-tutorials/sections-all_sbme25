import PyQt6
from matrix import Matrix

# matrix1 = Matrix([[1, 2], [3, 4]])
# matrix2 = Matrix([[1, 2], [3, 4]])

# matrix3 = matrix1.multiply(matrix2)

# print(matrix3)

from PyQt6 import QtWidgets
from gui import Ui_MainWindow
import sys


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.but_equal.clicked.connect(self.onClick)

    def onClick(self):
        ui = self.ui
        operation = ui.cmBx_operation.currentText()
        matrix1 = Matrix([[int(ui.lnEdt_a11.text()), int(ui.lnEdt_a12.text())], [int(ui.lnEdt_a21.text()), int(ui.lnEdt_a22.text())]])
        matrix2 = Matrix([[int(ui.lnEdt_b11.text()), int(ui.lnEdt_b12.text())], [int(ui.lnEdt_b21.text()), int(ui.lnEdt_b22.text())]])

        match operation:
            case '+':
                matrix3 = matrix1.add(matrix2)
            case '-':
                matrix3 = matrix1.subtract(matrix2)
            case 'x':
                matrix3 = matrix1.multiply(matrix2)

        ui.lnEdt_c11.setText(str(matrix3.data[0][0]))
        ui.lnEdt_c12.setText(str(matrix3.data[0][1]))
        ui.lnEdt_c21.setText(str(matrix3.data[1][0]))
        ui.lnEdt_c22.setText(str(matrix3.data[1][1]))

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec()


if __name__ == "__main__":
    main()