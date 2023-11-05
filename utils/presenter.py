from .database import Database
from .parser import Parser
from PyQt5.QtWidgets import QTableWidgetItem
from widgets.application import Application


class Presenter:
    def __init__(self, _model: Database, _view: Application):
        self.initProps(_model, _view)

    def initProps(self, _model, _view):
        self.model = _model
        self.view = _view
        self.parser = Parser()

        self.updateTableHandler()

        # TODO: each button should be have self methods for actions
        self.view.btn_update_table.clicked.connect(self.onButtonClickedToUpdateTable)
        self.view.btn_update_database.clicked.connect(self.onButtonClickedToUpdateDatabase)
        self.view.btn_insert_row.clicked.connect(self.onButtonClickedToInsertRowToTable)

    def onButtonClickedToUpdateTable(self):
        self.updateTableHandler()
    
    def updateTableHandler(self):
        shop = self.view.cbox_shop.currentText().lower()
        if shop == 'chameleon':
            self.view.btn_insert_row.setDisabled(False)
            self.view.btn_add_row.setDisabled(False)
        else:
            self.view.btn_insert_row.setDisabled(True)
            self.view.btn_add_row.setDisabled(True)
        params = {'shop': shop}
        if not self.view.tedit_device_name.text() == '':
            params['inventor'] = self.view.tedit_device_name.text().lower()
        rows = self.model.getRowsByFilter(params)
        self.view.updateTable(rows)
    
    def onButtonClickedToUpdateDatabase(self):
        self.updateDatabaseHandler()
    
    def updateDatabaseHandler(self):
        product_list = self.parser.getAllParsedData()
        self.model.insertRows(product_list)
        self.updateTableHandler()

    def onButtonClickedToInsertRowToTable(self):
        rowCount = self.view.table.rowCount()
        row = []
        for i in range(self.view.table.columnCount()):
            item_text = QTableWidgetItem.text(QTableWidgetItem(self.view.table.item(rowCount - 1, i)))
            if item_text == '':
                return # except error of empty  
            row.append(item_text)
        self.insertRowToDatabaseHandler(row)

    def insertRowToDatabaseHandler(self, row):
        self.model.insertRow(row)

   

