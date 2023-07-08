# -*- coding: utf-8 -*-
import os
import subprocess

# Form implementation generated from reading ui file 'Inventory.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QTableWidgetItem

from Encryption import Encryption
from Product import Product


class Ui_inventory(object):
    def setupUi(self, inventory):
        inventory.setObjectName("inventory")
        inventory.resize(800, 500)
        inventory.setMinimumSize(QtCore.QSize(800, 500))
        inventory.setMaximumSize(QtCore.QSize(800, 500))
        self.label_3 = QtWidgets.QLabel(inventory)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 781, 41))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 24pt \"Perpetua Titling MT\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(inventory)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 50, 50))
        self.pushButton.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton.setAcceptDrops(False)
        self.pushButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/Back_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(inventory)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.label.setStyleSheet("background-image: url(image/BG.jpeg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(inventory)
        self.tableWidget.setGeometry(QtCore.QRect(20, 70, 761, 411))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label.raise_()
        self.label_3.raise_()
        self.pushButton.raise_()
        self.tableWidget.raise_()

        self.retranslateUi(inventory)
        QtCore.QMetaObject.connectSlotsByName(inventory)

        self.tableWidget.setFont(QFont("Tahoma", 12))
        self.pushButton.clicked.connect(self.backToMain)

    def retranslateUi(self, inventory):
        _translate = QtCore.QCoreApplication.translate
        inventory.setWindowTitle(_translate("inventory", "Inventory"))
        self.label_3.setText(_translate("inventory", "inventory"))

    item = []

    def add_item(self, data):
        self.item.append(data)

    def retrieve(self):
        file_path = "Database/products.txt"  # Replace with the actual file path

        try:
            with open(file_path, "r") as reader:
                for line in reader:
                    line = Encryption.decrypt(line)
                    arr_line = line.split(" / ")
                    temp = Product()  # Create a new instance for each item
                    temp.setID(int(arr_line[0].strip()))
                    temp.setPrice(int(arr_line[1].strip()))
                    temp.setQuantity(int(arr_line[2].strip()))
                    temp.setProductName(arr_line[3].strip())
                    temp.setBrand(arr_line[4].strip())
                    temp.setDescription(arr_line[5].strip())
                    temp.setCategory(arr_line[6].strip())
                    temp.setSupplier(arr_line[7].strip())
                    temp.setDate(arr_line[8].strip())
                    self.add_item(temp)
                    temp = Product()  # Create a new instance for each item
        except IOError as e:
            print("Error reading file:", e)

    def display_table(self):
        num_rows = len(self.item)
        num_cols = 9

        # Set the table dimensions
        self.tableWidget.setRowCount(num_rows)
        self.tableWidget.setColumnCount(num_cols)

        # Define the desired attribute names
        attribute_names = ["ID", "Price", "Quantity", "ProductName", "Brand", "Description", "Category", "Supplier", "Date"]
        self.tableWidget.setHorizontalHeaderLabels(attribute_names)

        # Populate the table with data
        for row in range(num_rows):
            item = self.item[row]
            for col in range(num_cols):
                attribute_name = attribute_names[col]
                value = getattr(item, attribute_name)
                table_item = QTableWidgetItem(str(value))

                # Set the item flags to make it read-only
                table_item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)

                self.tableWidget.setItem(row, col, table_item)

        # Adjust column widths to maximize space
        # table_width = self.tableWidget.viewport().width()
        # column_width = int(table_width / num_cols)
        # for col in range(num_cols):
        #     self.tableWidget.setColumnWidth(col, column_width)

    def backToMain(self):
        inventory.destroy()
        current_directory = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(current_directory, "main.py")
        subprocess.run(["python", script_path])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    inventory = QtWidgets.QFrame()
    ui = Ui_inventory()
    ui.setupUi(inventory)
    ui.retrieve()
    ui.display_table()
    inventory.show()
    sys.exit(app.exec_())