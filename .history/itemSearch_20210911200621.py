# Form implementation generated from reading ui file 'itemSearch.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(244, 72)
        Dialog.setMinimumSize(QtCore.QSize(244, 72))
        Dialog.setMaximumSize(QtCore.QSize(244, 72))
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(10, 10, 223, 55))
        self.splitter.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.productCodeLabel = QtWidgets.QLabel(self.layoutWidget)
        self.productCodeLabel.setObjectName("productCodeLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.productCodeLabel)
        self.productCode = QtWidgets.QLineEdit(self.layoutWidget)
        self.productCode.setObjectName("productCode")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.productCode)
        self.cancelOkButtonBox = QtWidgets.QDialogButtonBox(self.splitter)
        self.cancelOkButtonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.cancelOkButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.cancelOkButtonBox.setObjectName("cancelOkButtonBox")

        self.retranslateUi(Dialog)
        self.cancelOkButtonBox.accepted.connect(Dialog.accept)
        self.cancelOkButtonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Item Search"))
        self.productCodeLabel.setText(_translate("Dialog", "Product Code:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
