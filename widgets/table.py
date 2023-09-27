from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout,
                             QPushButton, QTableWidget, QTableWidgetItem,
                             QHeaderView, QComboBox, QLabel, QLineEdit)
from strings import errors
from widgets.filterform import FilterForm
from widgets.table_controller import TableController


class Table(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    
    def initUI(self):
        self.filterform = FilterForm()
        self.table_controller = TableController()

        self.layout = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setRowCount(1)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['Type', 'Name', 'Model', 'Price'])

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)       
        header.setSectionResizeMode(2, QHeaderView.Stretch)

        self.table_controller.btn_add_row.clicked.connect(self.addRowToTable)

        self.layout.addWidget(self.filterform)
        self.layout.addWidget(self.table)
        self.layout.addWidget(self.table_controller)

        self.setLayout(self.layout)
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


    def getRowItems(self):
        rowCount = self.table.rowCount()
        row = []
        for i in range(self.table.columnCount()):
            item_text = QTableWidgetItem.text(QTableWidgetItem(self.table.item(rowCount - 1, i)))
            if item_text == '':
                self.setErrorLabel(errors.ROW_ITEMS_EMPTY_ERROR)
                return []
            row.append(item_text)
        return row