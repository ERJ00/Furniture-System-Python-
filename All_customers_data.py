import os
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from CustomerData import CustomerData
from Encryption import Encryption


class Ui_allCustomersData(object):
    def setupUi(self, allCustomersData):
        allCustomersData.setObjectName("allCustomersData")
        allCustomersData.resize(1000, 500)
        allCustomersData.setMinimumSize(QtCore.QSize(1000, 500))
        allCustomersData.setMaximumSize(QtCore.QSize(1000, 500))
        self.label = QtWidgets.QLabel(allCustomersData)
        self.label.setGeometry(QtCore.QRect(0, 0, 1001, 501))
        self.label.setStyleSheet("background-image: url(image/BG2.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(allCustomersData)
        self.pushButton.setGeometry(QtCore.QRect(0, 10, 50, 50))
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
        self.label_3 = QtWidgets.QLabel(allCustomersData)
        self.label_3.setGeometry(QtCore.QRect(0, 20, 991, 41))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 75 24pt \"Perpetua Titling MT\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(allCustomersData)
        self.tableWidget.setGeometry(QtCore.QRect(10, 80, 981, 401))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setStyleSheet("font: 75 12pt \"Tahoma\";")
        self.frame = QtWidgets.QFrame(allCustomersData)
        self.frame.setGeometry(QtCore.QRect(700, 20, 280, 50))
        self.frame.setMinimumSize(QtCore.QSize(280, 50))
        self.frame.setMaximumSize(QtCore.QSize(280, 50))
        self.frame.setStyleSheet("background-color: rgb(0, 36, 66);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 81, 31))
        self.label_2.setStyleSheet("font: 75 16pt \"Tahoma\";\n"
                                    "color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(100, 10, 181, 31))
        self.comboBox.setStyleSheet("background-color: rgb(51, 51, 55);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "font: 75 16pt \"Tahoma\";")
        self.comboBox.setObjectName("comboBox")
        self.label.raise_()
        self.label_3.raise_()
        self.pushButton.raise_()
        self.tableWidget.raise_()
        self.frame.raise_()

        self.retranslateUi(allCustomersData)
        QtCore.QMetaObject.connectSlotsByName(allCustomersData)

        self.comboBox.addItems(["PAID", "BALANCE"])
        self.comboBox.setCurrentIndex(-1)
        self.comboBox.currentIndexChanged.connect(lambda: self.display_table(self.comboBox.currentText()))
        self.pushButton.clicked.connect(self.backToMain)

    def retranslateUi(self, allCustomersData):
        _translate = QtCore.QCoreApplication.translate
        allCustomersData.setWindowTitle(_translate("allCustomersData", "All Customers Data"))
        self.label_3.setText(_translate("allCustomersData", "Customers Data"))
        self.label_2.setText(_translate("allCustomersData", "Status :"))

    customer = []

    def add_item(self, data):
        self.customer.append(data)

    def retrieve(self):
        file_path = "Database/customers_data.txt"

        try:
            with open(file_path, "r") as reader:
                lines = reader.readlines()

                for line in lines:
                    line = Encryption.decrypt(line)
                    arr_line = line.split(" / ")
                    temp = CustomerData()  # Create a new instance for each item
                    temp.setStatus(arr_line[0].strip())
                    temp.setName(arr_line[1].strip())
                    temp.setBirthday(arr_line[2].strip())
                    temp.setContactNumber(arr_line[3].strip())
                    temp.setAddress(arr_line[4].strip())
                    temp.setProductName(arr_line[5].strip())
                    temp.setCategory(arr_line[6].strip())

                    try:
                        temp.setQuantity(int(arr_line[7].strip()))
                        temp.setTotalPayment(int(arr_line[8].strip()))
                        temp.setPaymentReceived(int(arr_line[9].strip()))
                        temp.setBalance(int(arr_line[10].strip()))
                        temp.setChange(int(arr_line[11].strip()))
                        temp.setID(int(arr_line[13].strip()))
                    except ValueError as e:
                        # Handle the exception gracefully (e.g., log the error, skip the item, etc.)
                        print("Error parsing integer value:", str(e))
                        continue  # Skip this item and proceed to thenext iteration

                    temp.setDate(arr_line[12].strip())
                    self.add_item(temp)

        except IOError as e:
            print("Error reading file:", str(e))

    def display_table(self, status):
        num_cols = 14

        # Filter items based on the category
        filtered_items = [item for item in self.customer if item.getStatus() == status]
        num_rows = len(filtered_items)

        # Set the table dimensions
        self.tableWidget.setRowCount(num_rows)
        self.tableWidget.setColumnCount(num_cols)

        # Define the desired attribute names
        attribute_names = [
            "id","status", "name", "birthday", "contactNumber", "address",
            "productName", "category",  "quantity", "totalPayment", "paymentReceived",
            "balance", "change","date"
        ]
        self.tableWidget.setHorizontalHeaderLabels(attribute_names)

        # Populate the table with data
        for row in range(num_rows):
            item = filtered_items[row]
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
        allCustomersData.close()
        current_directory = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(current_directory, "main.py")
        subprocess.run(["python", script_path])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    allCustomersData = QtWidgets.QFrame()
    ui = Ui_allCustomersData()
    ui.setupUi(allCustomersData)
    ui.retrieve()
    allCustomersData.show()
    sys.exit(app.exec_())
