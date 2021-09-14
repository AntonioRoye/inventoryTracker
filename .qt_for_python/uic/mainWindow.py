# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(380, 145)
        MainWindow.setMinimumSize(QSize(380, 145))
        MainWindow.setMaximumSize(QSize(380, 145))
        self.actionConfigurations = QAction(MainWindow)
        self.actionConfigurations.setObjectName(u"actionConfigurations")
        self.actionCopy = QAction(MainWindow)
        self.actionCopy.setObjectName(u"actionCopy")
        self.actionPaste = QAction(MainWindow)
        self.actionPaste.setObjectName(u"actionPaste")
        self.actionSave_to_file = QAction(MainWindow)
        self.actionSave_to_file.setObjectName(u"actionSave_to_file")
        self.actionPrint = QAction(MainWindow)
        self.actionPrint.setObjectName(u"actionPrint")
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.actionCut = QAction(MainWindow)
        self.actionCut.setObjectName(u"actionCut")
        self.actionCreate_new_Admin = QAction(MainWindow)
        self.actionCreate_new_Admin.setObjectName(u"actionCreate_new_Admin")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.viewInventory = QPushButton(self.centralwidget)
        self.viewInventory.setObjectName(u"viewInventory")

        self.gridLayout.addWidget(self.viewInventory, 1, 2, 1, 1)

        self.editItem = QPushButton(self.centralwidget)
        self.editItem.setObjectName(u"editItem")

        self.gridLayout.addWidget(self.editItem, 0, 2, 1, 1)

        self.addItem = QPushButton(self.centralwidget)
        self.addItem.setObjectName(u"addItem")

        self.gridLayout.addWidget(self.addItem, 0, 0, 1, 1)

        self.viewItem = QPushButton(self.centralwidget)
        self.viewItem.setObjectName(u"viewItem")

        self.gridLayout.addWidget(self.viewItem, 1, 1, 1, 1)

        self.orderItem = QPushButton(self.centralwidget)
        self.orderItem.setObjectName(u"orderItem")
        self.orderItem.setEnabled(False)

        self.gridLayout.addWidget(self.orderItem, 1, 0, 1, 1)

        self.deleteItem = QPushButton(self.centralwidget)
        self.deleteItem.setObjectName(u"deleteItem")

        self.gridLayout.addWidget(self.deleteItem, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 380, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)
        QWidget.setTabOrder(self.addItem, self.deleteItem)
        QWidget.setTabOrder(self.deleteItem, self.editItem)
        QWidget.setTabOrder(self.editItem, self.orderItem)
        QWidget.setTabOrder(self.orderItem, self.viewItem)
        QWidget.setTabOrder(self.viewItem, self.viewInventory)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionSave_to_file)
        self.menuFile.addAction(self.actionPrint)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionCut)
        self.menuSettings.addAction(self.actionConfigurations)
        self.menuSettings.addAction(self.actionCreate_new_Admin)
        self.menuHelp.addAction(self.actionDocumentation)

        self.retranslateUi(MainWindow)
        self.addItem.clicked.connect(self.addItem.click)
        self.deleteItem.clicked.connect(self.deleteItem.click)
        self.editItem.clicked.connect(self.editItem.click)
        self.orderItem.clicked.connect(self.orderItem.click)
        self.viewItem.clicked.connect(self.viewItem.click)
        self.viewInventory.clicked.connect(self.viewInventory.click)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Inventory", None))
        self.actionConfigurations.setText(QCoreApplication.translate("MainWindow", u"Configurations", None))
        self.actionCopy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
#if QT_CONFIG(shortcut)
        self.actionCopy.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionPaste.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
#if QT_CONFIG(shortcut)
        self.actionPaste.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+V", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_to_file.setText(QCoreApplication.translate("MainWindow", u"Save to CSV", None))
        self.actionPrint.setText(QCoreApplication.translate("MainWindow", u"Print", None))
#if QT_CONFIG(shortcut)
        self.actionPrint.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.actionCut.setText(QCoreApplication.translate("MainWindow", u"Cut", None))
        self.actionCreate_new_Admin.setText(QCoreApplication.translate("MainWindow", u"Create new Admin", None))
        self.viewInventory.setText(QCoreApplication.translate("MainWindow", u"View Inventory", None))
        self.editItem.setText(QCoreApplication.translate("MainWindow", u"Edit Item", None))
        self.addItem.setText(QCoreApplication.translate("MainWindow", u"Add Item", None))
        self.viewItem.setText(QCoreApplication.translate("MainWindow", u"View Item", None))
        self.orderItem.setText(QCoreApplication.translate("MainWindow", u"Order Item", None))
        self.deleteItem.setText(QCoreApplication.translate("MainWindow", u"Delete Item", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

