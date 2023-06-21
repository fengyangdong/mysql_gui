from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt

def value_changed(row, column):
    item = table_widget.item(row, column)
    new_value = item.text()
    print(f"Changed value at row {row}, column {column}: {new_value}")

app = QApplication([])

table_widget = QTableWidget()
table_widget.setColumnCount(3)
table_widget.setRowCount(3)

# 给每个单元格添加初始值
for row in range(3):
    for col in range(3):
        item = QTableWidgetItem(f"Cell {row}-{col}")
        table_widget.setItem(row, col, item)

# 连接cellChanged信号到value_changed槽函数
table_widget.cellChanged.connect(value_changed)

table_widget.show()
app.exec_()