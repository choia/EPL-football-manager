import soccer_club
import squad
import sys
import urllib.request
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget, QHBoxLayout, QVBoxLayout, QComboBox, \
    QTableWidget, QTableWidgetItem, QLabel, QPushButton, QAbstractItemView, QGroupBox, QLineEdit


class FootballManager(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        '''Initial UI'''
        # Label 'Clubs'
        club_label = QLabel('Clubs:')
        club_label.setStyleSheet('font-weight: bold;' 'font-size: 12px;')
        club_label.setMaximumWidth(40)

        # Combobox for Clubs NEED TO ADDITEMS
        club_cbox = QComboBox()
        club_cbox.setStyleSheet('border: 2px solid gray' 'border-radius: 2px;' 'min-width: 5em;')
        club_cbox.setMinimumHeight(22)
        club_cbox.setMaximumWidth(230)

        # Search Button
        search_btn = QPushButton('Search')
        search_btn.setStyleSheet('background-color: rgb(255, 255, 240);' 'border: 2px solid black;' 'font: bold 12px;'
                           'min-width: 5em;' 'padding: 1px;' 'border-style: outset;')
        pressed_stylesheet = "::pressed{Background-color: orange; border-style: inset;}"
        search_btn.setStyleSheet(pressed_stylesheet)
        search_btn.setMaximumWidth(60)

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