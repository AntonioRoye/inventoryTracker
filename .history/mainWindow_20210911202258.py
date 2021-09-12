# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets, 
import addItemDialog, itemSearch, viewInventoryDialog, viewItemDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 145)
        MainWindow.setMinimumSize(QtCore.QSize(380, 145))
        MainWindow.setMaximumSize(QtCore.QSize(380, 145))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.viewInventory = QtWidgets.QPushButton(self.centralwidget)
        self.viewInventory.setObjectName("viewInventory")
        self.gridLayout.addWidget(self.viewInventory, 1, 2, 1, 1)
        self.editItem = QtWidgets.QPushButton(self.centralwidget)
        self.editItem.setObjectName("editItem")
        self.gridLayout.addWidget(self.editItem, 0, 2, 1, 1)
        self.addItem = QtWidgets.QPushButton(self.centralwidget)
        self.addItem.setObjectName("addItem")
        self.gridLayout.addWidget(self.addItem, 0, 0, 1, 1)
        self.viewItem = QtWidgets.QPushButton(self.centralwidget)
        self.viewItem.setObjectName("viewItem")
        self.gridLayout.addWidget(self.viewItem, 1, 1, 1, 1)
        self.orderItem = QtWidgets.QPushButton(self.centralwidget)
        self.orderItem.setEnabled(False)
        self.orderItem.setObjectName("orderItem")
        self.gridLayout.addWidget(self.orderItem, 1, 0, 1, 1)
        self.deleteItem = QtWidgets.QPushButton(self.centralwidget)
        self.deleteItem.setObjectName("deleteItem")
        self.gridLayout.addWidget(self.deleteItem, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 380, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionConfigurations = QtGui.QAction(MainWindow)
        self.actionConfigurations.setObjectName("actionConfigurations")
        self.actionCopy = QtGui.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtGui.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionSave_to_file = QtGui.QAction(MainWindow)
        self.actionSave_to_file.setObjectName("actionSave_to_file")
        self.actionPrint = QtGui.QAction(MainWindow)
        self.actionPrint.setObjectName("actionPrint")
        self.menuFile.addAction(self.actionSave_to_file)
        self.menuFile.addAction(self.actionPrint)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuSettings.addAction(self.actionConfigurations)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())

        self.retranslateUi(MainWindow)
        self.addItem.clicked.connect(self.addItemDialog)
        self.deleteItem.clicked.connect(self.deleteItem.click)
        self.editItem.clicked.connect(self.editItem.click)
        self.orderItem.clicked.connect(self.orderItem.click)
        self.viewItem.clicked.connect(self.viewItem.click)
        self.viewInventory.clicked.connect(self.viewInventory.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.addItem, self.deleteItem)
        MainWindow.setTabOrder(self.deleteItem, self.editItem)
        MainWindow.setTabOrder(self.editItem, self.orderItem)
        MainWindow.setTabOrder(self.orderItem, self.viewItem)
        MainWindow.setTabOrder(self.viewItem, self.viewInventory)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Inventory"))
        self.viewInventory.setText(_translate("MainWindow", "View Inventory"))
        self.editItem.setText(_translate("MainWindow", "Edit Item"))
        self.addItem.setText(_translate("MainWindow", "Add Item"))
        self.viewItem.setText(_translate("MainWindow", "View Item"))
        self.orderItem.setText(_translate("MainWindow", "Order Item"))
        self.deleteItem.setText(_translate("MainWindow", "Delete Item"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuExit.setTitle(_translate("MainWindow", "Exit"))
        self.actionConfigurations.setText(_translate("MainWindow", "Configurations"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionSave_to_file.setText(_translate("MainWindow", "Save to file"))
        self.actionPrint.setText(_translate("MainWindow", "Print"))
        self.actionPrint.setShortcut(_translate("MainWindow", "Ctrl+P"))
        
    def addItemDialog(self):
        Dialog = QtWidgets.QDialog()
        ui = addItemDialog.Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        ui.exec_()

class AddItemDlg(QDialog):
    """Employee dialog."""
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_Dialog()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())