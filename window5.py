from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget,QLineEdit,QLabel,QVBoxLayout,QPushButton, QMessageBox

class Wwindow5(QMainWindow):
    def __init__(self):
        super().__init__()
        
        layout  = QVBoxLayout()
        self.login_lbl = QLabel("Вы успешно прошли тест")
        
        self.exit_btn = QPushButton("завершить")
        
        
        layout.addWidget(self.login_lbl)
        layout.addWidget(self.exit_btn)
        
        
        self.exit_btn.clicked.connect(self.exit)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        
            
    def exit(self):
        exe.close()   
            
        with open("style.css", "r") as css:
            widget.setStyleSheet(css.read())