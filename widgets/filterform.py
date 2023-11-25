from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout,
                             QPushButton, QTableWidget, QTableWidgetItem,
                             QHeaderView, QComboBox, QLabel, QLineEdit, QGridLayout)
from strings import errors


class FilterForm(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    
    def initUI(self):
        self.layout = QGridLayout()

        lineHeight = 15

        self.label_name = QLabel("Name")
        self.tedit_device_name = QLineEdit()
        self.tedit_device_name.setMaximumHeight(lineHeight)

        self.label_model = QLabel("Model")
        self.tedit_device_model = QLineEdit()
        self.tedit_device_model.setMaximumHeight(lineHeight)

        self.label_type = QLabel("Type")
        self.tedit_device_type = QLineEdit()
        self.tedit_device_type.setMaximumHeight(lineHeight)

        self.btn_apply_filter = QPushButton('Apply filter')

        self.label_price_range = QLabel("Price range")
        self.tedit_device_price_range_from = QLineEdit()
        self.tedit_device_price_range_from.setPlaceholderText('From')
        self.tedit_device_price_range_from.setMaximumHeight(lineHeight)
        self.tedit_device_price_range_to = QLineEdit()
        self.tedit_device_price_range_to.setPlaceholderText('To')
        self.tedit_device_price_range_to.setMaximumHeight(lineHeight)

        self.layout.addWidget(self.label_type, 0, 0)
        self.layout.addWidget(self.tedit_device_type, 0, 1)
        
        self.layout.addWidget(self.label_name, 1, 0)
        self.layout.addWidget(self.tedit_device_name, 1, 1)

        self.layout.addWidget(self.label_model, 2, 0)
        self.layout.addWidget(self.tedit_device_model, 2, 1)

        self.layout.addWidget(self.label_price_range, 0, 2)
        self.layout.addWidget(self.tedit_device_price_range_from, 1, 2)
        self.layout.addWidget(self.tedit_device_price_range_to, 2, 2)

        self.layout.addWidget(self.btn_apply_filter)

        self.setLayout(self.layout)
        self.show()
