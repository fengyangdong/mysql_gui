


header 可以改
user_table 是table的名称

header2 = CheckBoxHeader()
self.ui.user_table.setHorizontalHeader(header2)
header2.select_all_clicked.connect(header2.change_state)  # 行表头复选框单击信号与槽
self.ui.user_table.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置整行选中
self.ui.user_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)