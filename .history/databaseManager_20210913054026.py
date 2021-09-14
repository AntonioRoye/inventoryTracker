import sqlite3

class InventoryDatabase():
    _database = "inventory.db"
    def __init__(self):
        connection = sqlite3.connect(self._database)
        crsr = connection.cursor()

        createTable = """ CREATE TABLE IF NOT EXISTS INVENTORY (
            PRODUCTCODE TEXT PRIMARY KEY NOT NULL,
            PRODUCT TEXT NOT NULL,
            PRICE REAL,
            COMPANY TEXT,
            COMPANYWEBSITE TEXT,
            AMOUNT INTEGER,
            SIZE TEXT,
            STORAGE TEXT,
            DATERECEIVED TEXT,
            RECIPIENT TEXT,
            NOTES TEXT
        );"""

        crsr.execute(createTable)
        connection.commit()
        connection.close()
    
    def insertItem(self, valuesList):
        connection = sqlite3.connect(self._database)
        crsr = connection.cursor()
        
        crsr.execute("""INSERT INTO INVENTORY VALUES 
                     (\"{1}\", \"{0}\", {2}, \"{3}\", 
                     \"{4}\", {5}, \"{6}\", \"{7}\", 
                     \"{8}\", \"{9}\", \"{10}\");""".format(
                valuesList[0], valuesList[1], valuesList[2],
                valuesList[3], valuesList[4], valuesList[5],
                valuesList[6], valuesList[7], valuesList[8],
                valuesList[9], valuesList[10]
            ))
        connection.commit()
        connection.close()

    def delItem(self, productCode):
        connection = sqlite3.connect(self._database)
        crsr = connection.cursor()

        crsr.execute("DELETE FROM INVENTORY WHERE PRODUCTCODE = \"{0}\";".format(productCode))
        
        connection.commit()
        connection.close()

    def updateItem(self, oldProductCode, valuesList):
        connection = sqlite3.connect(self._database)
        crsr = connection.cursor()
        
        crsr.execute("""UPDATE INVENTORY SET 
                    PRODUCTCODE = \"{1}\",
                    PRODUCT = \"{0}\",
                    PRICE = {2},
                    COMPANY = \"{3}\",
                    COMPANYWEBSITE = \"{4}\",
                    AMOUNT = {5},
                    SIZE = \"{6}\",
                    STORAGE = \"{7}\",
                    DATERECEIVED = \"{8}\",
                    RECIPIENT = \"{9}\",
                    NOTES = \"{10}\" WHERE PRODUCTCODE = \"{11}\";""".format(
                valuesList[0], valuesList[1], valuesList[2],
                valuesList[3], valuesList[4], valuesList[5],
                valuesList[6], valuesList[7], valuesList[8],
                valuesList[9], valuesList[10], oldProductCode
            ))
        
        connection.commit()
        connection.close()
    
    def viewInventory(self):
        connection = sqlite3.connect(self._database)
        crsr = connection.cursor()
        crsr.execute("SELECT * FROM INVENTORY")
        ans = crsr.fetchall()
        connection.close()
        
        return ans
    
    def viewItem(self, productCode):
        connection = sqlite3.connect(self._database)
        crsr = connection.cursor()
        
        crsr.execute(
            "SELECT * FROM INVENTORY WHERE PRODUCTCODE = \"{0}\";".format(productCode))
        ans = crsr.fetchall()
        print(ans)
        connection.commit()
        connection.close()