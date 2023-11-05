from PyQt5 import QtWidgets, QtSql

db_config = {
    "database": "QSQLITE",
    "databaseName": "database.sqlite",
    "mainTable": "devices",
}


class Database:
    def __init__(self):
        self.initDataBase()


    def initDataBase(self):
        self.db = QtSql.QSqlDatabase.addDatabase(db_config["database"])
        self.db.setDatabaseName(db_config["databaseName"])

        self.db.open()
        if db_config["mainTable"] not in self.db.tables():
            query = QtSql.QSqlQuery()
            query.exec(
                f"""
                CREATE TABLE {db_config['mainTable']} (
                    id integer primary key autoincrement,
                    shop varchar(50) not null,
                    type varchar(20) not null,
                    inventor varchar(30) not null,
                    model varchar(50) not null,
                    price integer not null
                )
            """
            )
            print(f"-----> Table {db_config['mainTable']} has created! <------")

        self.db.close()


    def insertRow(self, row):
        self.db.open()
        query = QtSql.QSqlQuery()
        query.exec(
            """
                INSERT INTO {4} (shop, type, inventor, model, price)
                VALUES ('chameleon', {0}, {1}, {2}, {3});
            """.format(*row, db_config['mainTable'])
        )
        self.db.close()
        self.selectRows()


    def deleteAllTableData(self):
        self.db.open()
        query = QtSql.QSqlQuery()
        self.db.close


    def insertRows(self, rows):
        self.db.open()
        query = QtSql.QSqlQuery()
        # query.exec(f'DELETE FROM {db_config["mainTable"]};')
        query_values_string = ""
        for row in rows:
            query_values_string += f"('{row['shop']}', '{row['type']}', '{row['inventor']}', '{row['model']}', '{row['price']}'), "

        query.exec(
            f"""
                INSERT INTO {db_config['mainTable']} (shop, type, inventor, model, price)
                VALUES {query_values_string[:-2]};
            """
        )
        self.db.close()


    def selectRows(self):
        self.db.open()
        query = QtSql.QSqlQuery()
        query.exec(
            f"""
                SELECT * FROM {db_config['mainTable']}
            """
        )

        result = []
        if query.isActive():
            query.first()
            while query.isValid():
                obj = {
                    "id": query.value("id"),
                    "shop": query.value("shop"),
                    "type": query.value("type"),
                    "inventor": query.value("inventor"),
                    "model": query.value("model"),
                    "price": query.value("price"),
                }
                result.append(obj)
                query.next()

        self.db.close()
        return result


    def getRowsByFilter(self, params):
        self.db.open()
        query = QtSql.QSqlQuery()
        # This is need to clear database if it data was wrong
        # query.exec(f'DELETE FROM {db_config["mainTable"]};')

        query_string = f"""SELECT * FROM {db_config['mainTable']} """

        if not params == None:
            print(params)
            query_string += f"""WHERE """
            for k, v in params.items():
                query_string += f"""{k} = '{v}' and """

        query_string = query_string[:-5] + ';'
        print(query_string)
        query.exec(query_string)

        result = []
        if query.isActive():
            query.first()
            while query.isValid():
                obj = {
                    "id": query.value("id"),
                    "shop": query.value("shop"),
                    "type": query.value("type"),
                    "inventor": query.value("inventor"),
                    "model": query.value("model"),
                    "price": query.value("price"),
                }
                result.append(obj)
                query.next()

        self.db.close()
        return result