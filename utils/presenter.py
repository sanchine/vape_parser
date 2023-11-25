from .database import Database
from .parser import Parser
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
        # self.view.sidebar.btn_update_table.clicked.connect(self.onButtonClickedToUpdateTable)
        self.view.table.filterform.btn_apply_filter.clicked.connect(self.onButtonClickedToUpdateTable)
        self.view.sidebar.btn_update_database.clicked.connect(self.onButtonClickedToUpdateDatabase)
        self.view.table.table_controller.btn_insert_row.clicked.connect(self.onButtonClickedToInsertRowToTable)

    def test(self):
        print('test')

    def onButtonClickedToUpdateTable(self):
        self.updateTableHandler()
    
    def updateTableHandler(self):
        shop = self.view.sidebar.cbox_shop.currentText().lower()
        if shop == 'chameleon':
            self.view.table.table_controller.btn_insert_row.setDisabled(False)
            self.view.table.table_controller.btn_add_row.setDisabled(False)
        else:
            self.view.table.table_controller.btn_insert_row.setDisabled(True)
            self.view.table.table_controller.btn_add_row.setDisabled(True)
        params = {'shop': shop}
        if not self.view.table.filterform.tedit_device_type.text() == '':
            params['type'] = self.view.table.filterform.tedit_device_type.text().lower()
        if not self.view.table.filterform.tedit_device_name.text() == '':
            params['inventor'] = self.view.table.filterform.tedit_device_name.text().lower()
        if not self.view.table.filterform.tedit_device_model.text() == '':
            params['model'] = self.view.table.filterform.tedit_device_model.text().lower()
        rows = self.model.getRowsByFilter(params)
        self.view.table.updateTable(rows)
    
    def onButtonClickedToUpdateDatabase(self):
        self.updateDatabaseHandler()
    
    def updateDatabaseHandler(self):
        product_list = self.parser.getAllParsedData()
        self.model.insertRows(product_list)
        self.updateTableHandler()

    def onButtonClickedToInsertRowToTable(self):
        row = self.view.table.getRowItems()
        if len(row) == 0:
            return
        self.insertRowToDatabaseHandler(row)

    def insertRowToDatabaseHandler(self, row):
        self.model.insertRow(row)

   

