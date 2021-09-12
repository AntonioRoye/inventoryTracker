# Form implementation generated from reading ui file 'viewItemDialog.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(464, 553)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.productLabel = QtWidgets.QLabel(Dialog)
        self.productLabel.setObjectName("productLabel")
        self.gridLayout.addWidget(self.productLabel, 0, 0, 1, 1)
        self.product = QtWidgets.QLineEdit(Dialog)
        self.product.setReadOnly(True)
        self.product.setObjectName("product")
        self.gridLayout.addWidget(self.product, 0, 1, 1, 1)
        self.productCodeLabel = QtWidgets.QLabel(Dialog)
        self.productCodeLabel.setObjectName("productCodeLabel")
        self.gridLayout.addWidget(self.productCodeLabel, 1, 0, 1, 1)
        self.productCode = QtWidgets.QLineEdit(Dialog)
        self.productCode.setReadOnly(True)
        self.productCode.setObjectName("productCode")
        self.gridLayout.addWidget(self.productCode, 1, 1, 1, 1)
        self.priceLabel = QtWidgets.QLabel(Dialog)
        self.priceLabel.setObjectName("priceLabel")
        self.gridLayout.addWidget(self.priceLabel, 2, 0, 1, 1)
        self.price = QtWidgets.QLineEdit(Dialog)
        self.price.setReadOnly(True)
        self.price.setObjectName("price")
        self.gridLayout.addWidget(self.price, 2, 1, 1, 1)
        self.companyLabel = QtWidgets.QLabel(Dialog)
        self.companyLabel.setObjectName("companyLabel")
        self.gridLayout.addWidget(self.companyLabel, 3, 0, 1, 1)
        self.company = QtWidgets.QLineEdit(Dialog)
        self.company.setReadOnly(True)
        self.company.setObjectName("company")
        self.gridLayout.addWidget(self.company, 3, 1, 1, 1)
        self.companyWebsiteLabel = QtWidgets.QLabel(Dialog)
        self.companyWebsiteLabel.setObjectName("companyWebsiteLabel")
        self.gridLayout.addWidget(self.companyWebsiteLabel, 4, 0, 1, 1)
        self.companyWebsite = QtWidgets.QLineEdit(Dialog)
        self.companyWebsite.setReadOnly(True)
        self.companyWebsite.setObjectName("companyWebsite")
        self.gridLayout.addWidget(self.companyWebsite, 4, 1, 1, 1)
        self.amountLabel = QtWidgets.QLabel(Dialog)
        self.amountLabel.setObjectName("amountLabel")
        self.gridLayout.addWidget(self.amountLabel, 5, 0, 1, 1)
        self.amount = QtWidgets.QLineEdit(Dialog)
        self.amount.setReadOnly(True)
        self.amount.setObjectName("amount")
        self.gridLayout.addWidget(self.amount, 5, 1, 1, 1)
        self.sizeLabel = QtWidgets.QLabel(Dialog)
        self.sizeLabel.setObjectName("sizeLabel")
        self.gridLayout.addWidget(self.sizeLabel, 6, 0, 1, 1)
        self.size = QtWidgets.QLineEdit(Dialog)
        self.size.setReadOnly(True)
        self.size.setObjectName("size")
        self.gridLayout.addWidget(self.size, 6, 1, 1, 1)
        self.storageLabel = QtWidgets.QLabel(Dialog)
        self.storageLabel.setObjectName("storageLabel")
        self.gridLayout.addWidget(self.storageLabel, 7, 0, 1, 1)
        self.storage = QtWidgets.QLineEdit(Dialog)
        self.storage.setReadOnly(True)
        self.storage.setObjectName("storage")
        self.gridLayout.addWidget(self.storage, 7, 1, 1, 1)
        self.dateReceivedLabel = QtWidgets.QLabel(Dialog)
        self.dateReceivedLabel.setObjectName("dateReceivedLabel")
        self.gridLayout.addWidget(self.dateReceivedLabel, 8, 0, 1, 1)
        self.dateReceived = QtWidgets.QLineEdit(Dialog)
        self.dateReceived.setReadOnly(True)
        self.dateReceived.setObjectName("dateReceived")
        self.gridLayout.addWidget(self.dateReceived, 8, 1, 1, 1)
        self.recipientLabel = QtWidgets.QLabel(Dialog)
        self.recipientLabel.setObjectName("recipientLabel")
        self.gridLayout.addWidget(self.recipientLabel, 9, 0, 1, 1)
        self.Recipient = QtWidgets.QLineEdit(Dialog)
        self.Recipient.setReadOnly(True)
        self.Recipient.setObjectName("Recipient")
        self.gridLayout.addWidget(self.Recipient, 9, 1, 1, 1)
        self.notesLabel = QtWidgets.QLabel(Dialog)
        self.notesLabel.setObjectName("notesLabel")
        self.gridLayout.addWidget(self.notesLabel, 10, 0, 1, 1)
        self.notes = QtWidgets.QTextEdit(Dialog)
        self.notes.setReadOnly(True)
        self.notes.setObjectName("notes")
        self.gridLayout.addWidget(self.notes, 10, 1, 1, 1)
        self.cancelOkButtonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.cancelOkButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.cancelOkButtonBox.setCenterButtons(False)
        self.cancelOkButtonBox.setObjectName("cancelOkButtonBox")
        self.gridLayout.addWidget(self.cancelOkButtonBox, 11, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.cancelOkButtonBox.accepted.connect(Dialog.accept)
        self.cancelOkButtonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "View Item"))
        self.productLabel.setText(_translate("Dialog", "Product:"))
        self.productCodeLabel.setText(_translate("Dialog", "Product Code:"))
        self.priceLabel.setText(_translate("Dialog", "Price:"))
        self.companyLabel.setText(_translate("Dialog", "Company:"))
        self.companyWebsiteLabel.setText(_translate("Dialog", "Company website:"))
        self.amountLabel.setText(_translate("Dialog", "Amount:"))
        self.sizeLabel.setText(_translate("Dialog", "Size/Type:"))
        self.storageLabel.setText(_translate("Dialog", "Storage:"))
        self.dateReceivedLabel.setText(_translate("Dialog", "Date received:"))
        self.recipientLabel.setText(_translate("Dialog", "Recipient:"))
        self.notesLabel.setText(_translate("Dialog", "Notes:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())