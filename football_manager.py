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
        club_label1 = QLabel('Clubs:')
        club_label1.setStyleSheet('font-weight: bold;' 'font-size: 12px;')
        club_label1.setMaximumWidth(40)

        # Combobox for Clubs NEED TO ADDITEMS
        club_cbox = QComboBox()
        club_cbox.setStyleSheet('border: 2px solid gray' 'border-radius: 2px;' 'min-width: 5em;')
        club_cbox.setMinimumHeight(22)
        club_cbox.setMaximumWidth(230)

        for cbox_item in range(soccer_club.team_count):
            club_cbox.addItem(soccer_club.team_data[cbox_item]['team_name'])

        # Search Button NEED TO ADD EVENTS WHEN CLICKED
        search_btn = QPushButton('Search')
        search_btn.setStyleSheet('background-color: rgb(255, 255, 240);' 'border: 2px solid black;' 'font: bold 12px;'
                           'min-width: 5em;' 'padding: 1px;' 'border-style: outset;')
        pressed_stylesheet = "::pressed{Background-color: orange; border-style: inset;}"
        search_btn.setStyleSheet(pressed_stylesheet)
        search_btn.setMaximumWidth(60)

        # Add the label, combobox, and search button to fm_hbox1 layout
        fm_hbox1 = QHBoxLayout()
        fm_hbox1.addWidget(club_label1)
        fm_hbox1.addWidget(club_cbox)
        fm_hbox1.addWidget(search_btn)

        # Club Images NEED TO MOVE TO SEARCH EVENT FUNCTION
        image_label = QLabel()
        image_label.setStyleSheet('background: white;' 'padding-left: 20px;' 'padding-right: 30px;')

        url = 'http://smimgs.com/images/logos/clubs/31.jpg' #PLACEHOLDER FOR NOW
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        data = urllib.request.urlopen(req).read()
        img = QImage()
        img.loadFromData(data)
        pimg = img.scaled(110, 110, Qt.KeepAspectRatio)
        image_label.setPixmap(QPixmap(pimg))
        image_label.setAlignment(Qt.AlignCenter)

        # Label Club Info for fm_hbox2 layout
        club_label2 = QLabel('Club Name:\n\nNickname:\n\nFounded:\n\nManager:\n\nLocation:\n\nStadium:')
        club_label2.setStyleSheet('background: white;' 'padding-top: 20px;' 'padding-right: 5px;' 'font-weight: bold;')
        club_label2.setAlignment(Qt.AlignRight)

        # Overall layout
        fm_vbox = QVBoxLayout()
        fm_vbox.addLayout(fm_hbox1)
        fm_vbox.setSpacing(5)
        self.setLayout(fm_vbox)
        self.setStyleSheet('background: white;')
        self.setGeometry(300, 300, 400, 600)
        self.setFixedSize(400, 600)  # Disable resizing widget window
        self.show()


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
    sys.exit(app.exec_())