from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QRadioButton

class StartWidget(QWidget):
    def __init__(self, btn_exitClicked, btn_enterClicked):
        super().__init__()
        self.question = QLabel("<center>Готовы ли вы пройти тест?</center>")
        self.btn_enter = QPushButton("Да")
        self.btn_exit = QPushButton("Выход")
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.btn_enter)
        self.hbox.addWidget(self.btn_exit)
        self.question.setObjectName('LabelTestWindow')
        self.btn_exit.clicked.connect(btn_exitClicked)
        self.btn_enter.clicked.connect(btn_enterClicked)
        vbox = QVBoxLayout()
        vbox.addWidget(self.question)
        vbox.addLayout(self.hbox)
        self.setLayout(vbox)
        

class TestWidget1(QWidget):
    def __init__(self, btn_nextClicked):
        super().__init__()
        self.question = QLabel("<center>Вопрос 1: Какой формат используется для изображений в интернете?</center>")
        self.btn_next = QPushButton("Далее")
        self.rb1 = QRadioButton("Ответ 1: BMP")
        self.rb2 = QRadioButton("Ответ 2: JPEG")
        self.rb3 = QRadioButton("Ответ 3: TIFF")
        self.btn_next.clicked.connect(btn_nextClicked)
        self.btn_next.setObjectName("LabelQuestionTestWindow")
        self.question.setObjectName("LabelQuestionTestWindow")
        vbox = QVBoxLayout()
        vbox.addWidget(self.question)
        vbox.addWidget(self.rb1)
        vbox.addWidget(self.rb2)
        vbox.addWidget(self.rb3)
        vbox.addWidget(self.btn_next)
        self.setLayout(vbox)
        

class TestWidget2(QWidget):
    def __init__(self, btn_nextClicked):
        super().__init__()
        self.question = QLabel("<center>Вопрос 2: Какие форматы видеозаписей поддерживает сайт?</center>")
        self.btn_next = QPushButton("Далее")
        self.rb1 = QRadioButton("Ответ 1: AVI, MP4, 3GP, MPEG, MOV, MP3")
        self.rb2 = QRadioButton("Ответ 2: FLV, WMV, MKV, TS, VOB.")
        self.rb3 = QRadioButton("Ответ 3: Оба варианта верны")
        self.btn_next.setObjectName("LabelQuestionTestWindow")
        self.question.setObjectName("LabelQuestionTestWindow")
        self.btn_next.clicked.connect(btn_nextClicked)
        vbox = QVBoxLayout()
        vbox.addWidget(self.question)
        vbox.addWidget(self.rb1)
        vbox.addWidget(self.rb2)
        vbox.addWidget(self.rb3)
        vbox.addWidget(self.btn_next)
        self.setLayout(vbox)
        

class TestWidget3(QWidget):
    def __init__(self, btn_nextClicked):
        super().__init__()
        self.question = QLabel("<center>Вопрос 3: Какой формат используется для изображений в интернете?</center>")
        self.btn_next = QPushButton("Далее")
        self.rb1 = QRadioButton("Ответ 1: PHP, JavaScript, ActionScript, HTML, CSS")
        self.rb2 = QRadioButton("Ответ 2: Python, CSS, HTML")
        self.rb3 = QRadioButton("Ответ 3: C++, HTML, CSS,")
        self.btn_next.clicked.connect(btn_nextClicked)
        self.btn_next.setObjectName("LabelQuestionTestWindow")
        self.question.setObjectName("LabelQuestionTestWindow")
        vbox = QVBoxLayout()
        vbox.addWidget(self.question)
        vbox.addWidget(self.rb1)
        vbox.addWidget(self.rb2)
        vbox.addWidget(self.rb3)
        vbox.addWidget(self.btn_next)
        self.setLayout(vbox)
        

class EndWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.txt = QLabel("<center>Тест пройден успешно</center>")
        self.txt.setObjectName("LabelQuestionTestWindow")
        vbox = QVBoxLayout()
        vbox.addWidget(self.txt)
        self.setLayout(vbox)
        