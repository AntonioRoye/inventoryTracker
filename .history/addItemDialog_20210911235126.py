# Form implementation generated from reading ui file 'addItemDialog.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def __init__(self, windowTitle = "Add Item"):
        self.windowTitle = windowTitle
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(414, 562)
        Dialog.setAutoFillBackground(False)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.company = QtWidgets.QLineEdit(Dialog)
        self.company.setObjectName("company")
        self.gridLayout.addWidget(self.company, 3, 1, 1, 2)
        self.companyWebsiteLabel = QtWidgets.QLabel(Dialog)
        self.companyWebsiteLabel.setObjectName("companyWebsiteLabel")
        self.gridLayout.addWidget(self.companyWebsiteLabel, 4, 0, 1, 1)
        self.companyLabel = QtWidgets.QLabel(Dialog)
        self.companyLabel.setObjectName("companyLabel")
        self.gridLayout.addWidget(self.companyLabel, 3, 0, 1, 1)
        self.companyWebsite = QtWidgets.QLineEdit(Dialog)
        self.companyWebsite.setObjectName("companyWebsite")
        self.gridLayout.addWidget(self.companyWebsite, 4, 1, 1, 2)
        self.size = QtWidgets.QLineEdit(Dialog)
        self.size.setObjectName("size")
        self.gridLayout.addWidget(self.size, 6, 1, 1, 2)
        self.date = QtWidgets.QDateEdit(Dialog)
        self.date.setObjectName("date")
        self.gridLayout.addWidget(self.date, 8, 1, 1, 2)
        self.priceLabel = QtWidgets.QLabel(Dialog)
        self.priceLabel.setObjectName("priceLabel")
        self.gridLayout.addWidget(self.priceLabel, 2, 0, 1, 1)
        self.dateReceivedLabel = QtWidgets.QLabel(Dialog)
        self.dateReceivedLabel.setObjectName("dateReceivedLabel")
        self.gridLayout.addWidget(self.dateReceivedLabel, 8, 0, 1, 1)
        self.recipient = QtWidgets.QLineEdit(Dialog)
        self.recipient.setObjectName("recipient")
        self.gridLayout.addWidget(self.recipient, 9, 1, 1, 2)
        self.productCodeLabel = QtWidgets.QLabel(Dialog)
        self.productCodeLabel.setObjectName("productCodeLabel")
        self.gridLayout.addWidget(self.productCodeLabel, 1, 0, 1, 1)
        self.storageLabel = QtWidgets.QLabel(Dialog)
        self.storageLabel.setObjectName("storageLabel")
        self.gridLayout.addWidget(self.storageLabel, 7, 0, 1, 1)
        self.notesLabel = QtWidgets.QLabel(Dialog)
        self.notesLabel.setObjectName("notesLabel")
        self.gridLayout.addWidget(self.notesLabel, 10, 0, 1, 1)
        self.sizeLabel = QtWidgets.QLabel(Dialog)
        self.sizeLabel.setObjectName("sizeLabel")
        self.gridLayout.addWidget(self.sizeLabel, 6, 0, 1, 1)
        self.amountLabel = QtWidgets.QLabel(Dialog)
        self.amountLabel.setObjectName("amountLabel")
        self.gridLayout.addWidget(self.amountLabel, 5, 0, 1, 1)
        self.product = QtWidgets.QLineEdit(Dialog)
        self.product.setObjectName("product")
        self.gridLayout.addWidget(self.product, 0, 1, 1, 2)
        self.cancelOkButtonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.cancelOkButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.cancelOkButtonBox.setCenterButtons(False)
        self.cancelOkButtonBox.setObjectName("cancelOkButtonBox")
        self.gridLayout.addWidget(self.cancelOkButtonBox, 11, 2, 1, 1)
        self.notes = QtWidgets.QTextEdit(Dialog)
        self.notes.setObjectName("notes")
        self.gridLayout.addWidget(self.notes, 10, 1, 1, 2)
        self.recipientLabel = QtWidgets.QLabel(Dialog)
        self.recipientLabel.setObjectName("recipientLabel")
        self.gridLayout.addWidget(self.recipientLabel, 9, 0, 1, 1)
        self.productLabel = QtWidgets.QLabel(Dialog)
        self.productLabel.setObjectName("productLabel")
        self.gridLayout.addWidget(self.productLabel, 0, 0, 1, 1)
        self.priceSpinBox = QtWidgets.QDoubleSpinBox(Dialog)
        self.priceSpinBox.setMaximum(1000000.0)
        self.priceSpinBox.setObjectName("priceSpinBox")
        self.gridLayout.addWidget(self.priceSpinBox, 2, 1, 1, 2)
        self.storageComboBox = QtWidgets.QComboBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.storageComboBox.sizePolicy().hasHeightForWidth())
        self.storageComboBox.setSizePolicy(sizePolicy)
        self.storageComboBox.setEditable(False)
        self.storageComboBox.setObjectName("storageComboBox")
        self.storageComboBox.addItem("")
        self.storageComboBox.addItem("")
        self.storageComboBox.addItem("")
        self.storageComboBox.addItem("")
        self.gridLayout.addWidget(self.storageComboBox, 7, 1, 1, 2)
        self.productCode = QtWidgets.QLineEdit(Dialog)
        self.productCode.setObjectName("productCode")
        self.gridLayout.addWidget(self.productCode, 1, 1, 1, 2)
        self.amount = QtWidgets.QSpinBox(Dialog)
        self.amount.setMaximum(100000)
        self.amount.setObjectName("amount")
        self.gridLayout.addWidget(self.amount, 5, 1, 1, 2)

        self.retranslateUi(Dialog)
        self.cancelOkButtonBox.accepted.connect(Dialog.accept)
        self.cancelOkButtonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.product, self.productCode)
        Dialog.setTabOrder(self.productCode, self.priceSpinBox)
        Dialog.setTabOrder(self.priceSpinBox, self.company)
        Dialog.setTabOrder(self.company, self.companyWebsite)
        Dialog.setTabOrder(self.companyWebsite, self.amount)
        Dialog.setTabOrder(self.amount, self.size)
        Dialog.setTabOrder(self.size, self.storageComboBox)
        Dialog.setTabOrder(self.storageComboBox, self.date)
        Dialog.setTabOrder(self.date, self.recipient)
        Dialog.setTabOrder(self.recipient, self.notes)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", self.windowTitle))
        self.companyWebsiteLabel.setText(_translate("Dialog", "Company website:"))
        self.companyLabel.setText(_translate("Dialog", "Company:"))
        self.priceLabel.setText(_translate("Dialog", "Price:"))
        self.dateReceivedLabel.setText(_translate("Dialog", "Date received:"))
        self.productCodeLabel.setText(_translate("Dialog", "Product Code:"))
        self.storageLabel.setText(_translate("Dialog", "Storage:"))
        self.notesLabel.setText(_translate("Dialog", "Notes:"))
        self.sizeLabel.setText(_translate("Dialog", "Size/Type:"))
        self.amountLabel.setText(_translate("Dialog", "Amount:"))
        self.recipientLabel.setText(_translate("Dialog", "Recipient:"))
        self.productLabel.setText(_translate("Dialog", "Product:"))
        self.storageComboBox.setItemText(0, _translate("Dialog", "Room Temp"))
        self.storageComboBox.setItemText(1, _translate("Dialog", " 4 °C"))
        self.storageComboBox.setItemText(2, _translate("Dialog", "-20 °C"))
        self.storageComboBox.setItemText(3, _translate("Dialog", "-80 °C"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
