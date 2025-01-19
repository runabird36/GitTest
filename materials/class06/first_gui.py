
from PyQt5 import QtWidgets, QtCore
import sys

class NamePrintView(QtWidgets.QMainWindow):
    def __init__(self, _parnet=None):
        super(NamePrintView, self).__init__()

        self.setupUi()

    def setupUi(self):

        self.print_output_lb    = QtWidgets.QLabel()
        self.print_output_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.input_le           = QtWidgets.QLineEdit()
        self.print_ok_btn       = QtWidgets.QPushButton()
        self.print_ok_btn.setText("나 프린트할래")
        self.print_ok_btn.clicked.connect(self.print_input)

        self.main_vl = QtWidgets.QVBoxLayout()
        self.main_vl.addWidget(self.print_output_lb)
        self.main_vl.addWidget(self.input_le)
        self.main_vl.addWidget(self.print_ok_btn)

        self.main_wg = QtWidgets.QWidget()
        self.main_wg.setLayout(self.main_vl)

        self.setCentralWidget(self.main_wg)
        self.resize(500, 600)


    def print_input(self):
        input_str = self.input_le.text()
        self.print_output_lb.setText(input_str)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    main_view = NamePrintView()
    main_view.show()

    app.exec_()
