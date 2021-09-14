import sqlite3

connection = sqlite3.connect("inventory.db")
crsr = connection.cursor()

createTable = """ CREATE TABLE IF NOT EXISTS INVENTORY (
    PRODUCTCODE TEXT PRIMARY KEY NOT NULL,
    PRODUCT TEXT NOT NULL,
    PRICE INTEGER,
    COMPANY TEXT,
    COMPANYWEBSITE TEXT,
    AMOUNT FLOAT
);"""
crsr.execute(createTable)
connection.commit()
connection.close()