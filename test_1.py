from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QStackedWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QStackedWidget(self)

        self.page1 = QWidget()
        self.label1 = QLabel("Page 1", self.page1)
        self.layout1 = QVBoxLayout(self.page1)
        self.layout1.addWidget(self.label1)
        self.stacked_widget.addWidget(self.page1)

        self.page2 = QWidget()
        self.label2 = QLabel("Page 2", self.page2)
        self.layout2 = QVBoxLayout(self.page2)
        self.layout2.addWidget(self.label2)
        self.stacked_widget.addWidget(self.page2)

        self.page3 = QWidget()
        self.label3 = QLabel("Page 3", self.page3)
        self.layout3 = QVBoxLayout(self.page3)
        self.layout3.addWidget(self.label3)
        self.stacked_widget.addWidget(self.page3)

        self.button1 = QPushButton("Page 1", self)
        self.button1.clicked.connect(lambda: self.set_current_page("page1"))

        self.button2 = QPushButton("Page 2", self)
        self.button2.clicked.connect(lambda: self.set_current_page("page2"))

        self.button3 = QPushButton("Page 3", self)
        self.button3.clicked.connect(lambda: self.set_current_page("page3"))

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.stacked_widget)
        self.setCentralWidget(central_widget)

    def set_current_page(self, page_name):
        index = self.stacked_widget.indexOf(self.findChild(QWidget, page_name))
        if index != -1:
            self.stacked_widget.setCurrentIndex(index)

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()