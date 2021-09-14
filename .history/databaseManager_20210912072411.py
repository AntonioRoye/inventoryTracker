import sqlite3

connection = sqlite3.connect("inventory.db")
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
    RECIPIENT TEXT
);"""

crsr.execute(createTable)
connection.commit()
connection.close()