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
        initial_index = 0

        # Label 'Clubs'
        club_label1 = QLabel('Clubs:')
        club_label1.setStyleSheet('font-weight: bold;' 'font-size: 12px;')
        club_label1.setMaximumWidth(40)

        # QCombobox for clubs
        club_cbox = QComboBox()
        club_cbox.setStyleSheet('border: 2px solid gray' 'border-radius: 2px;' 'min-width: 5em;')
        club_cbox.setMinimumHeight(22)
        club_cbox.setMaximumWidth(230)

        # Add items from team_data list
        for cbox_item in range(soccer_club.team_count):
            club_cbox.addItem(soccer_club.team_data[cbox_item]['team_name'])

        # Search Button NEED TO ADD EVENTS WHEN CLICKED
        search_btn = QPushButton('Search')
        search_btn.setStyleSheet('background-color: rgb(255, 255, 240);' 'border: 2px solid black;' 'font: bold 12px;'
                                 'min-width: 5em;' 'padding: 1px;' 'border-style: outset;')
        pressed_stylesheet = "::pressed{Background-color: orange; border-style: inset;}"
        search_btn.setStyleSheet(pressed_stylesheet)
        search_btn.setMaximumWidth(60)
        search_btn.clicked.connect(self.run_search)

        # Add the label, combobox, and search button to fm_hbox1 layout
        fm_hbox1 = QHBoxLayout()
        fm_hbox1.addWidget(club_label1)
        fm_hbox1.addWidget(club_cbox)
        fm_hbox1.addWidget(search_btn)

        # Club Images NEED TO MOVE/COPY TO SEARCH EVENT FUNCTION
        image_label = QLabel()
        image_label.setStyleSheet('background: white;' 'padding-left: 20px;' 'padding-right: 40px;')
        url = soccer_club.team_data[initial_index]['logo_url']
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        data = urllib.request.urlopen(req).read()
        img = QImage()
        img.loadFromData(data)
        pix_img = img.scaled(60, 60, Qt.KeepAspectRatio)
        image_label.setPixmap(QPixmap(pix_img))
        image_label.setAlignment(Qt.AlignCenter)

        # Label Club Info for fm_hbox2 layout
        club_label2 = QLabel('Club Name:\n\nNickname:\n\nFounded:\n\nManager:\n\nLocation:\n\nStadium:')
        club_label2.setStyleSheet('background: white;' 'padding-top: 20px;' 'padding-right: 5px;' 'font-weight: bold;')
        club_label2.setAlignment(Qt.AlignRight)

        # Display club information # DISPLAY INFO WHEN SEARCHED
        club_label3 = QLabel()
        club_label3.setText(soccer_club.team_data[initial_index]['team_name'] + "\n\n" +
                            soccer_club.team_data[initial_index]['nick_name'] + "\n\n" +
                            soccer_club.team_data[initial_index]['year_found'] + "\n\n" +
                            soccer_club.team_data[initial_index]['manager'] + "\n\n" +
                            soccer_club.team_data[initial_index]['location'] + "\n\n" +
                            soccer_club.team_data[initial_index]['stadium'] + "\n\n")
        club_label3.setStyleSheet('background: white;' 'padding-top: 20px;' 'padding-right: 50px;')
        club_label3.setAlignment(Qt.AlignLeft)

        # Add label widgets to fm_hbox2 layout
        fm_hbox2 = QHBoxLayout()
        fm_hbox2.setSpacing(0)
        fm_hbox2.addWidget(image_label)
        fm_hbox2.addWidget(club_label2)
        fm_hbox2.addWidget(club_label3)
        fm_hbox2.addStretch(1)

        # Add QTableWidget # NEED  TO DISPLAY DATA WHEN SEARCHED
        table1 = QTableWidget()
        table1.setStyleSheet('font-size: 11px;' 'alternate-background-color: rgb(176, 224, 208);'
                             'background-color: rgb(255, 255, 240);')
        table1.setAlternatingRowColors(True)  # Alternate row colors
        table1.setColumnCount(3)
        table1.setEditTriggers(QAbstractItemView.NoEditTriggers)  # Set the rows in Read Only
        table_vertical = table1.verticalHeader()
        table_vertical.setVisible(False)  # Disable vertical column numbers
        table1_horizontal = table1.horizontalHeader()
        table1_horizontal.setStretchLastSection(True)  # Stretch and close the gap

        header_name = [
            'Player Name',
            'Age',
            'Position'
        ]

        # Set number_of_rows for the table
        for number_of_row in range(squad.player_count):
            table1.setRowHeight(number_of_row, 1)

        # Print(len(soccer_club.team_data[initial_index]['players']))

        # Set rows on table by number of data
        table1.setRowCount(len(soccer_club.team_data[initial_index]['players']))

        # Adding player data into table
        for number_of_player, key in enumerate(soccer_club.team_data[initial_index]['players'].keys()):
            for number_of_data, item in enumerate(soccer_club.team_data[initial_index]['players'][key]):
                table1.setItem(number_of_player, number_of_data, QTableWidgetItem(item))

        table1.setHorizontalHeaderLabels(header_name)  # Set column name
        stylesheet = "::section{Background-color:rgb(248,248,255)}"
        table1.horizontalHeader().setStyleSheet(stylesheet)
        table1.setColumnWidth(0, 160)  # Set column width
        table1.resizeRowsToContents()

        # fm_hbox3 layout
        fm_hbox3 = QHBoxLayout()
        fm_hbox3.addWidget(table1)

        # Overall layout
        fm_vbox = QVBoxLayout()
        fm_vbox.addLayout(fm_hbox1)
        fm_vbox.addLayout(fm_hbox2)
        fm_vbox.addLayout(fm_hbox3)
        fm_vbox.setSpacing(5)
        self.setLayout(fm_vbox)
        self.setStyleSheet('background: white;')
        #self.setGeometry(300, 300, 400, 600)
        self.center_window()
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