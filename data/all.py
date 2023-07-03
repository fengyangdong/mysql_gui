


# header 可以改
# user_table 是table的名称

# header2 = CheckBoxHeader()
# self.ui.user_table.setHorizontalHeader(header2)
# header2.select_all_clicked.connect(header2.change_state)  # 行表头复选框单击信号与槽
# self.ui.user_table.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置整行选中
# self.ui.user_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)



"""
这个可以实现修改表进行判定
        for c in data_class:
            self.ui.select_class_box.addItem(c[0])
                def select2_student(self):
        print(self.ui.select_sdept_box.currentText())

                delete_list = []
        for row in range(self.ui.sdept_table.rowCount()):
            if self.ui.sdept_table.cellWidget(row, 0).isChecked() is True:
                # 把选中的行进行删除操作
                delete_list.append(self.ui.sdept_table.item(row,1).text())
"""
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