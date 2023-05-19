from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QProgressBar,QPushButton, QApplication, QStackedLayout, QMainWindow 
from testWindow import StartWidget, TestWidget1, TestWidget2, TestWidget3, EndWidget




class ModalLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Пройти тест")
        self.setFixedSize(600, 500)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

        self.stackLayout = QStackedLayout()
        self.add_layouts()
        self.setLayout(self.stackLayout)

    def add_layouts(self):
        self.startWidget = StartWidget(lambda: self.close(), lambda:  self.enter_clicked())
        self.testWidget1 = TestWidget1(lambda: self.next_clicked1())
        self.testWidget2 = TestWidget2(lambda: self.next_clicked2())
        self.testWidget3 = TestWidget3(lambda: self.next_clicked3())
        self.endWidget = EndWidget()
        self.stackLayout.addWidget(self.startWidget)
        self.stackLayout.addWidget(self.testWidget1)
        self.stackLayout.addWidget(self.testWidget2)
        self.stackLayout.addWidget(self.testWidget3)
        self.stackLayout.addWidget(self.endWidget)

        with open('styles2.css') as style:
            self.setStyleSheet(style.read())

    def next_clicked1(self):
        if self.testWidget1.rb2.isChecked():
            self.stackLayout.setCurrentIndex(2)
            with open('styles2.css') as style:
                self.setStyleSheet(style.read())
        else:
            
            with open("styles4.css", "r") as css:
                self.setStyleSheet(css.read())    

    def next_clicked2(self):
        if self.testWidget2.rb3.isChecked():
            self.stackLayout.setCurrentIndex(3)
            with open('styles2.css') as style:
                self.setStyleSheet(style.read())
        else:
            
            with open("styles4.css", "r") as css:
                self.setStyleSheet(css.read())    

    def next_clicked3(self):
        if self.testWidget3.rb1.isChecked():
            self.stackLayout.setCurrentIndex(4)
            with open('styles2.css') as style:
                self.setStyleSheet(style.read())
        else:
            
            with open("styles4.css", "r") as css:
                self.setStyleSheet(css.read())    
            

    def enter_clicked(self):
        self.stackLayout.setCurrentIndex(1)