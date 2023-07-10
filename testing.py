import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from Encryption import Encryption

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data Table")
        self.setGeometry(100, 100, 400, 300)

        # Create a table widget
        self.table_widget = QTableWidget(self)
        self.table_widget.setGeometry(10, 10, 380, 280)

        # Read data from the text file and populate the table
        self.read_data_and_populate_table("Database/products.txt")

    def read_data_and_populate_table(self, filename):
        data = []
        with open(filename, "r") as file:
            for line in file:
                line = Encryption.decrypt(line)
                print(line)
                row = line.strip().split(" /")
                data.append(row)

        num_rows = len(data)
        num_cols = len(data[0]) if num_rows > 0 else 0

        # Set the table dimensions
        self.table_widget.setRowCount(num_rows)
        self.table_widget.setColumnCount(num_cols)

        # Populate the table with data
        for row in range(num_rows):
            for col in range(num_cols):
                item = QTableWidgetItem(data[row][col])
                self.table_widget.setItem(row, col, item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
