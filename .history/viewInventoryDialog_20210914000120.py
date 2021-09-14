# Form implementation generated from reading ui file 'viewInventoryDialog.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(321, 482)
        Dialog.setAutoFillBackground(False)
        Dialog.setSizeGripEnabled(False)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.productTable = QtWidgets.QTableWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.productTable.sizePolicy().hasHeightForWidth())
        self.productTable.setSizePolicy(sizePolicy)
        self.productTable.setAutoFillBackground(False)
        self.productTable.setDragEnabled(False)
        self.productTable.setObjectName("productTable")
        self.productTable.setColumnCount(3)
        self.productTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(2, item)
        self.gridLayout.addWidget(self.productTable, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "View Inventory"))
        item = self.productTable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Product Code"))
        item = self.productTable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Product"))
        item = self.productTable.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Amount"))
    
    def addRows(self, rowList):
        for row in rowList:
            currentRowCount = self.productTable.rowCount()
            self.productTable.insertRow(currentRowCount)
            for i, colItem in enumerate(row):
                self.productTable.setItem(currentRowCount, i, QtWidgets.QTableWidgetItem(str(colItem)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
