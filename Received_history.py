# -*- coding: utf-8 -*-
import os
import subprocess
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from Encryption import Encryption
from Product import Product


class Ui_ReceivedHistory(object):
    def setupUi(self, ReceivedHistory):
        ReceivedHistory.setObjectName("ReceivedHistory")
        ReceivedHistory.resize(800, 500)
        ReceivedHistory.setMinimumSize(QtCore.QSize(800, 500))
        ReceivedHistory.setMaximumSize(QtCore.QSize(800, 500))
        self.pushButton = QtWidgets.QPushButton(ReceivedHistory)
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
        self.tableWidget = QtWidgets.QTableWidget(ReceivedHistory)
        self.tableWidget.setGeometry(QtCore.QRect(10, 70, 781, 411))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(ReceivedHistory)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.label.setStyleSheet("background-image: url(image/BG.jpeg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(ReceivedHistory)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 781, 41))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 75 24pt \"Perpetua Titling MT\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label.raise_()
        self.tableWidget.raise_()
        self.label_3.raise_()
        self.pushButton.raise_()

        # Add a combo box for selecting the month
        self.comboBox = QtWidgets.QComboBox(ReceivedHistory)
        self.comboBox.setGeometry(QtCore.QRect(70, 20, 151, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(["All", "January", "February", "March", "April", "May", "June", "July", "August",
                                "September", "October", "November", "December"])

        # Connect the combo box signal to the sorting function
        self.comboBox.currentIndexChanged.connect(self.display_table)

        self.retranslateUi(ReceivedHistory)
        QtCore.QMetaObject.connectSlotsByName(ReceivedHistory)

        self.pushButton.clicked.connect(self.backToMain)

    def retranslateUi(self, ReceivedHistory):
        _translate = QtCore.QCoreApplication.translate
        ReceivedHistory.setWindowTitle(_translate("ReceivedHistory", "Received History"))
        self.label_3.setText(_translate("ReceivedHistory", "Received History"))

    item = []

    def add_item(self, data):
        self.item.append(data)

    def retrieve(self):
        file_path = "Database/received_product_history.txt"  # Replace with the actual file path

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
        except IOError as e:
            print("Error reading file:", e)

    def display_table(self):
        selected_month = self.comboBox.currentText()

        num_cols = 9

        self.tableWidget.clear()

        # Define the desired attribute names
        attribute_names = ["ID", "Price", "Quantity", "ProductName", "Brand", "Description", "Category", "Supplier",
                           "Date"]
        self.tableWidget.setColumnCount(num_cols)
        self.tableWidget.setHorizontalHeaderLabels(attribute_names)

        # Filtered items list
        filtered_items = []

        # Filter the data based on the selected month
        if selected_month == "All":
            filtered_items = self.item
        else:
            filtered_items = [item for item in self.item if
                              datetime.strptime(item.getDate(), "%Y-%m-%d").strftime("%B") == selected_month]

        num_rows = len(filtered_items)

        # Set the table dimensions
        self.tableWidget.setRowCount(num_rows)

        if num_rows == 0:
            # Display "No data available" message
            table_item = QTableWidgetItem("No data available")
            table_item.setTextAlignment(QtCore.Qt.AlignCenter)
            table_item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(0, 0, table_item)
            self.tableWidget.setSpan(0, 0, 1, num_cols)
        else:
            # Populate the table with data
            for row, item in enumerate(filtered_items):
                for col in range(num_cols):
                    attribute_name = attribute_names[col]
                    value = getattr(item, attribute_name)
                    table_item = QTableWidgetItem(str(value))

                    # Set the item flags to make it read-only
                    table_item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)

                    self.tableWidget.setItem(row, col, table_item)

        # Adjust column widths to maximize space
        self.tableWidget.resizeColumnsToContents()

    # Adjust column widths to maximize space
    # table_width = self.tableWidget.viewport().width()
    # column_width = int(table_width / num_cols)
    # for col in range(num_cols):
    #     self.tableWidget.setColumnWidth(col, column_width)

    def backToMain(self):
        ReceivedHistory.destroy()
        current_directory = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(current_directory, "main.py")
        subprocess.run(["python", script_path])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ReceivedHistory = QtWidgets.QFrame()
    ui = Ui_ReceivedHistory()
    ui.setupUi(ReceivedHistory)
    ui.retrieve()
    ui.display_table()
    ReceivedHistory.show()
    sys.exit(app.exec_())
