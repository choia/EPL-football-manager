import sys
import soccer_club
# from PyQt5.QtGui import QDoubleValidator, QRegExpValidator
# from PyQt5.QtCore import QRegExp
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget, QHBoxLayout, QVBoxLayout, QComboBox, \
    QGroupBox, QLineEdit, QLabel, QPushButton


class FootballManager(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        '''Initial UI'''
        self.setWindowTitle('Football Manager')
        self.resize(600, 550)
        self.center_window()

        cbox = QComboBox(self)
        for item_count in range(soccer_club.team_count):
            cbox.addItem(soccer_club.team_data[item_count]['team_name'])

        self.search_button = QPushButton('Search')
        self.search_button.clicked.connect(self.run_search)

        self.team_label = QLabel()
        self.team_label.setText('Test')

        hbox = QHBoxLayout()
        hbox.addWidget(cbox)
        hbox.addWidget(self.search_button)

        vbox = QVBoxLayout()
        vbox.addWidget(self.team_label)

        self.setLayout(hbox)

    def run_search(self):
        pass



    def center_window(self):
        '''Centers the Window on the screen'''
        window_screen = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        window_screen.moveCenter(center_point)
        self.move(window_screen.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    fm = FootballManager()
    fm.show()
    sys.exit(app.exec_())