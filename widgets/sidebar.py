from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout,
                             QPushButton, QTableWidget, QTableWidgetItem,
                             QHeaderView, QComboBox, QLabel, QLineEdit)
from strings import errors


class Sidebar(QWidget):

    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.vbox = QVBoxLayout()
        self.label_shop = QLabel('Shop')
        self.cbox_shop = QComboBox()
        self.cbox_shop.addItems(['Chameleon', 'Zenmod', 'VapeLuxe'])
        self.btn_update_table = QPushButton('Update table')
        self.btn_update_database = QPushButton('Update database')

        self.vbox.addWidget(self.label_shop)
        self.vbox.addWidget(self.cbox_shop)
        self.vbox.addWidget(self.btn_update_table)
        self.vbox.addWidget(self.btn_update_database)
        self.vbox.addStretch()

        self.setLayout(self.vbox)

        self.show()