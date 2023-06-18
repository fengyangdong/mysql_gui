# -*- coding: utf-8 -*-
from PySide2.QtUiTools import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import sys

all_header_checkbox = []


# 设置列不可编辑类
class EmptyDelegate(QItemDelegate):
    def __init__(self, parent):
        super(EmptyDelegate, self).__init__(parent)

    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex):
        return None


# 表格类
class qtableDelete():
    def __init__(self):
        qfile = QFile('data/ui/untitled.ui')
        qfile.open(QFile.ReadOnly)
        qfile.close()
        self.ui = QUiLoader().load(qfile)
        # self.ui = QUiLoader().load('data/ui/untitled.ui')
        self.settable()
        self.ui.delete_2.clicked.connect(self.delete_check)

    # 设置表格内容
    def settable(self):

        header = CheckBoxHeader()
        self.ui.table.setHorizontalHeader(header)  # 设置头复选框
        header.select_all_clicked.connect(header.change_state)  # 行表头复选框单击信号与槽
        self.ui.table.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置整行选中
        # self.ui.table.setSelectionMode(QAbstractItemView.SingleSelection)#设置选择模式，选择单行
        self.ui.table.setRowCount(15)  # 设置表格行数
        self.ui.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 设置表头自适应
        # 设置表格内容和复选框
        for i in range(15):

            checkbox = QCheckBox()
            all_header_checkbox.append(checkbox)
            # checkbox.setCheckState(Qt.Unchecked) #设置复选框为不选状态、Partially（半选）、Checked（全选）
            self.ui.table.setCellWidget(i, 0, checkbox)  # 设置表格可选项
            for j in range(4):
                self.ui.table.setItem(i, j, QTableWidgetItem(f'{i}row,{j}col'))

                self.ui.table.item(i, j).setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 设置表格内水平垂直居#设置指定列的颜色和下划线
            # 设置第4列样式
        for i in range(self.ui.table.rowCount()):
            self.ui.table.item(i, 3).setForeground(QBrush(QColor('Blue')))  # 设置颜色
            font = QFont()
            font.setUnderline(True)
            self.ui.table.item(i, 3).setFont(font)  # 设置下划线

        # 设置第1/2/3、5列不可编辑
        list = [1, 2, 0, 4]
        for i in list:
            self.ui.table.setItemDelegateForColumn(i, EmptyDelegate(self.ui))

    # 删除选中的行数
    # def delete_check(self):
    #     row_box_list = []
    #     # 获取选中数据
    #     for i in range(self.ui.table.rowCount()):
    #         if self.ui.table.cellWidget(i, 0).isChecked() is True:
    #             row_box_list.append(i)
    #             row_box_list.reverse()  # 将数据进行降序
    #     for j in row_box_list:
    #         self.ui.table.removeRow(j)  # 删除选中行数据
    #         all_header_checkbox.pop(j)  # 重新构建check box列表
    def delete_check(self):
        for i in range(self.ui.table.rowCount()):
            print(i)
            print(self.ui.table.cellWidget(i,0))
            print(self.ui.table.cellWidget(i,1))
            print(self.ui.table.cellWidget(i,2))


class CheckBoxHeader(QHeaderView):
    """自定义表头类"""
    # 自定义 复选框全选信号
    select_all_clicked = Signal(bool)
    # 这4个变量控制列头复选框的样式，位置以及大小
    _x_offset = 0
    _y_offset = 0
    _width = 20
    _height = 20

    def __init__(self, orientation=Qt.Horizontal, parent=None):
        super(CheckBoxHeader, self).__init__(orientation, parent)
        self.isOn = False

    def paintSection(self, painter, rect, logicalIndex):
        painter.save()
        super(CheckBoxHeader, self).paintSection(painter, rect, logicalIndex)
        painter.restore()

        self._y_offset = int((rect.height() - self._width) / 2.)

        if logicalIndex == 0:
            option = QStyleOptionButton()
            option.rect = QRect(rect.x() + self._x_offset, rect.y() + self._y_offset, self._width, self._height)
            option.state = QStyle.State_Enabled | QStyle.State_Active
            if self.isOn:
                option.state |= QStyle.State_On
            else:
                option.state |= QStyle.State_Off
            self.style().drawControl(QStyle.CE_CheckBox, option, painter)

    def mousePressEvent(self, event):
        index = self.logicalIndexAt(event.pos())
        if 0 == index:
            x = self.sectionPosition(index)
            if x + self._x_offset < event.pos().x() < x + self._x_offset + self._width and self._y_offset < event.pos().y() < self._y_offset + self._height:
                if self.isOn:
                    self.isOn = False
                else:
                    self.isOn = True
                    # 当用户点击了行表头复选框，发射 自定义信号 select_all_clicked()
                self.select_all_clicked.emit(self.isOn)

                self.updateSection(0)
        super(CheckBoxHeader, self).mousePressEvent(event)

    # 自定义信号 select_all_clicked 的槽方法
    def change_state(self, isOn):
        # 如果行表头复选框为勾选状态
        if isOn:
            # 将所有的复选框都设为勾选状态
            for i in all_header_checkbox:
                i.setCheckState(Qt.Checked)
        else:
            for i in all_header_checkbox:
                i.setCheckState(Qt.Unchecked)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    stats = qtableDelete()
    stats.ui.show()
    app.exec_()

