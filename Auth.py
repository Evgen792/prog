import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget,QLineEdit,QLabel,QVBoxLayout,QPushButton, QMessageBox, QProgressBar, QStackedLayout
from PyQt6.QtCore import Qt, QTimer, QBasicTimer

import random
from win import ModalLogin


class Avtoriz(QMainWindow):
    def __init__(self):
        super().__init__()
        
        layout  = QVBoxLayout()
        self.Layout = QStackedLayout()
        self.login_lbl = QLabel("логин")
        self.login_box= QLineEdit()
        self.password_lbl = QLabel("Пароль")
        self.password_box = QLineEdit()
        self.auth_btn = QPushButton("Вход")
        self.exit_btn = QPushButton("Выход")
        
        
        layout.addWidget(self.login_lbl)
        layout.addWidget(self.login_box)
        layout.addWidget(self.password_lbl)
        layout.addWidget(self.password_box)
        layout.addWidget(self.auth_btn)
        layout.addWidget(self.exit_btn)
        
        self.auth_btn.clicked.connect(self.auth)
        self.auth_btn.setObjectName("int")
        self.exit_btn.setObjectName("OUT")
        self.exit_btn.clicked.connect(self.exit)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        layout.addLayout(self.Layout)
        
        with open("styles.css", "r") as css:
            widget.setStyleSheet(css.read())
    
        

    def auth(self):
        self.sw = Captcha()
        self.sw.show()
        self.close()
    
    def exit(self):
        exe.close()    






class Captcha(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        layout  = QVBoxLayout()
        self.captcha_lbl = QLabel("Введите капчу:")
        self.captcha_box= QLineEdit()
        self.timer_lbl = QLabel("Таймер:10")
        self.capth_ver = QPushButton("Проверить")
        self.captcha_ran = QLabel(str(random.randint(1000,9000)))
        
        self.timer = QTimer()
        self.count = 10
        self.timer_lbl.setText(str(self.count))
        self.timer.timeout.connect(self.timer_tick)
        
        
        
        layout.addWidget(self.captcha_lbl)
        layout.addWidget(self.captcha_ran)
        layout.addWidget(self.captcha_box)
        layout.addWidget(self.timer_lbl)
        layout.addWidget(self.capth_ver)
        
        self.capth_ver.clicked.connect(self.ver)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        with open("styles.css", "r") as css:
            widget.setStyleSheet(css.read())
        
    def ver (self):
            
        
        if self.captcha_box.text() == self.captcha_ran.text():
            QMessageBox.information(self, "Успех", "Капча введена правильно")
            Captcha.close(self)
            self.w2 = Example()
            self.w2.show()
            self.close()
        
        else:
            self.captcha_box.setDisabled(True)
            self.timer.start()
            QMessageBox.critical(self, "ОШИБКА", "Вы ввели неправильно")
            
            
        with open("styles.css", "r") as css:
            self.setStyleSheet(css.read())
            
    def timer_tick(self):
        self.timer.start(1000)
        self.count -=1
        self.timer_lbl.setText(str(self.count))
        
        if  self.count == 0:
            self.timer.stop()
            self.captcha_box.setDisabled(False)
            
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
    

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)
        self.timer = QBasicTimer()
        self.step = 0
        self.setWindowTitle('Загрузка теста')
        
        if self.timer.isActive():
            self.timer.stop()
            
        else:
            self.timer.start(100, self)
        
        self.show()

    def timerEvent(self, e):

        if self.step >= 100:
            self.timer.stop()
            self.w2 = ModalLogin()
            self.w2.show()
            self.close()
            
        self.step = self.step + 1
        self.pbar.setValue(self.step)
        
    
app= QApplication(sys.argv)
exe = Avtoriz()
exe.show()
app.exec()      