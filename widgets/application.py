from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout,
                             QPushButton, QTableWidget, QTableWidgetItem,
                             QHeaderView, QComboBox, QLabel, QLineEdit)


class Application(QWidget):
    
    def __init__(self):
        super().__init__()

        self.initUI()

    
    def initUI(self):
        # UI config
        self.setGeometry(800, 600, 800, 600)
        self.setWindowTitle('Vape parser')

        # widgets init
        main_layout = QHBoxLayout()
        sidebar_layout = QVBoxLayout()
        content_layout = QVBoxLayout()
        insert_layout = QHBoxLayout()

        self.label_shop = QLabel('Shop')
        self.label_app_error = QLabel('Error: undefined')

        self.cbox_shop = QComboBox()
        self.cbox_shop.addItems(['Chameleon', 'Zenmod', 'VapeLuxe'])

        self.tedit_device_name = QLineEdit()
        self.tedit_device_name.setMaximumHeight(20)

        self.btn_update_table = QPushButton('Update table')
        self.btn_save_table = QPushButton('Save table')
        self.btn_update_database = QPushButton('Update database')
        self.btn_add_row = QPushButton('Add row')
        self.btn_insert_row = QPushButton('Insert row')
        self.btn_insert_row.setDisabled(True)
        self.btn_add_row.setDisabled(True)

        self.btn_add_row.clicked.connect(self.addRowToTable)

        self.table = QTableWidget()
        self.table.setRowCount(1)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['Type', 'Name', 'Model', 'Price'])

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)       
        header.setSectionResizeMode(2, QHeaderView.Stretch)

        # adding to layouts
        sidebar_layout.addWidget(self.label_shop)
        sidebar_layout.addWidget(self.cbox_shop)
        sidebar_layout.addWidget(self.btn_update_table)
        sidebar_layout.addWidget(self.btn_update_database)
        sidebar_layout.addStretch()

        insert_layout.addWidget(self.btn_add_row)
        insert_layout.addWidget(self.btn_insert_row)

        content_layout.addWidget(self.tedit_device_name)
        content_layout.addWidget(self.table)
        content_layout.addLayout(insert_layout)

        main_layout.addLayout(sidebar_layout)
        main_layout.addLayout(content_layout)
        content_layout.addWidget(self.label_app_error)
        self.setLayout(main_layout)

        self.show()

    def addRowToTable(self):
        rowCount = self.table.rowCount()
        if not self.table.item(rowCount - 1, 0) == None:
            self.table.setRowCount(rowCount + 1)
    
    def updateTable(self, rows):
        self.table.setRowCount(0)
        
        if len(rows) == 0:
            self.table.setRowCount(1)
        else:
            self.table.setRowCount(len(rows))

        for i, val in enumerate(rows):
            self.table.setItem(i, 0, QTableWidgetItem(val['type']))
            self.table.setItem(i, 1, QTableWidgetItem(val['inventor']))
            self.table.setItem(i, 2, QTableWidgetItem(val['model']))
            self.table.setItem(i, 3, QTableWidgetItem(str(val['price'])))
