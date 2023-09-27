from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout,
                             QPushButton, QTableWidget, QTableWidgetItem,
                             QHeaderView, QComboBox, QLabel, QLineEdit, QGridLayout)
from strings import errors


class TableController(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()


    def initUi(self):
        self.layout = QGridLayout()
        self.btn_add_row = QPushButton('Add row')
        self.btn_insert_row = QPushButton('Insert row')
        self.btn_insert_row.setDisabled(True)
        self.btn_add_row.setDisabled(True)

        self.layout.addWidget(self.btn_add_row, 1, 1)
        self.layout.addWidget(self.btn_insert_row, 1, 2)

        self.setLayout(self.layout)
        self.show()