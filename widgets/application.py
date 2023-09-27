from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout,
                             QPushButton, QTableWidget, QTableWidgetItem,
                             QHeaderView, QComboBox, QLabel, QLineEdit)
from strings import errors
from widgets.sidebar import Sidebar
from widgets.table import Table


class Application(QWidget):
    
    def __init__(self):
        super().__init__()

        self.initUI()

    
    def initUI(self):
        # UI config
        self.setGeometry(800, 600, 800, 600)
        self.setWindowTitle('Vape parser')

        # widgets init
        self.sidebar = Sidebar()
        self.table = Table()

        main_layout = QHBoxLayout()
        content_layout = QVBoxLayout()

        self.label_app_error = QLabel(errors.NOT_ERROR)

        # adding to layouts

        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(self.table)
        self.setLayout(main_layout)

        self.show()


    def setErrorLabel(self, error):
        self.label_app_error.setText(error)