# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(538, 226)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setAutoFillBackground(False)
        self.lbl_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_title.setObjectName("lbl_title")
        self.verticalLayout.addWidget(self.lbl_title)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lnEdt_a11 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lnEdt_a11.setFont(font)
        self.lnEdt_a11.setText("")
        self.lnEdt_a11.setObjectName("lnEdt_a11")
        self.gridLayout.addWidget(self.lnEdt_a11, 0, 0, 1, 1)
        self.lnEdt_a12 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lnEdt_a12.setFont(font)
        self.lnEdt_a12.setObjectName("lnEdt_a12")
        self.gridLayout.addWidget(self.lnEdt_a12, 0, 1, 1, 1)
        self.lnEdt_a21 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lnEdt_a21.setFont(font)
        self.lnEdt_a21.setObjectName("lnEdt_a21")
        self.gridLayout.addWidget(self.lnEdt_a21, 1, 0, 1, 1)
        self.lnEdt_a22 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lnEdt_a22.setFont(font)
        self.lnEdt_a22.setObjectName("lnEdt_a22")
        self.gridLayout.addWidget(self.lnEdt_a22, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.cmBx_operation = QtWidgets.QComboBox(self.centralwidget)
        self.cmBx_operation.setObjectName("cmBx_operation")
        self.cmBx_operation.addItem("")
        self.cmBx_operation.addItem("")
        self.cmBx_operation.addItem("")
        self.horizontalLayout.addWidget(self.cmBx_operation)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lnEdt_b11 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lnEdt_b11.setFont(font)
        self.lnEdt_b11.setObjectName("lnEdt_b11")
        self.gridLayout_2.addWidget(self.lnEdt_b11, 0, 0, 1, 1)
        self.lnEdt_b12 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lnEdt_b12.setFont(font)
        self.lnEdt_b12.setObjectName("lnEdt_b12")
        self.gridLayout_2.addWidget(self.lnEdt_b12, 0, 1, 1, 1)
        self.lnEdt_b21 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lnEdt_b21.setFont(font)
        self.lnEdt_b21.setObjectName("lnEdt_b21")
        self.gridLayout_2.addWidget(self.lnEdt_b21, 1, 0, 1, 1)
        self.lnEdt_b22 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lnEdt_b22.setFont(font)
        self.lnEdt_b22.setObjectName("lnEdt_b22")
        self.gridLayout_2.addWidget(self.lnEdt_b22, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.but_equal = QtWidgets.QPushButton(self.centralwidget)
        self.but_equal.setObjectName("but_equal")
        self.horizontalLayout.addWidget(self.but_equal)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lnEdt_c11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lnEdt_c11.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lnEdt_c11.setFont(font)
        self.lnEdt_c11.setObjectName("lnEdt_c11")
        self.gridLayout_3.addWidget(self.lnEdt_c11, 0, 0, 1, 1)
        self.lnEdt_c12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lnEdt_c12.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lnEdt_c12.setFont(font)
        self.lnEdt_c12.setObjectName("lnEdt_c12")
        self.gridLayout_3.addWidget(self.lnEdt_c12, 0, 1, 1, 1)
        self.lnEdt_c21 = QtWidgets.QLineEdit(self.centralwidget)
        self.lnEdt_c21.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lnEdt_c21.setFont(font)
        self.lnEdt_c21.setObjectName("lnEdt_c21")
        self.gridLayout_3.addWidget(self.lnEdt_c21, 1, 0, 1, 1)
        self.lnEdt_c22 = QtWidgets.QLineEdit(self.centralwidget)
        self.lnEdt_c22.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lnEdt_c22.setFont(font)
        self.lnEdt_c22.setObjectName("lnEdt_c22")
        self.gridLayout_3.addWidget(self.lnEdt_c22, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 538, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_title.setText(_translate("MainWindow", "Matrix Calculator"))
        self.cmBx_operation.setItemText(0, _translate("MainWindow", "+"))
        self.cmBx_operation.setItemText(1, _translate("MainWindow", "-"))
        self.cmBx_operation.setItemText(2, _translate("MainWindow", "x"))
        self.but_equal.setText(_translate("MainWindow", "="))
