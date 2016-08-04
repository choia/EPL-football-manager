import sys
# from PyQt5.QtGui import QDoubleValidator, QRegExpValidator
# from PyQt5.QtCore import QRegExp
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QGroupBox, QLineEdit, QLabel, QDesktopWidget


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())