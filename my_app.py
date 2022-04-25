from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QLabel,QPushButton,QVBoxLayout,QApplication
from instr import *
from second_win import*

class MainWin(QWidget):   
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    # создание окна
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.move(win_x,win_y)
        self.resize(win_width,win_height)
    # создание виджетов
    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.btn_next = QPushButton(txt_next)

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment= Qt.AlignCenter)
        self.layout_line.addWidget(self.instruction, alignment= Qt.AlignCenter)
        self.layout_line.addWidget(self.btn_next, alignment= Qt.AlignCenter)
        self.setLayout(self.layout_line)
    # работа кнопки
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
    # действия кнопки
    def next_click(self):
        self.hide()
        self.tw = TestWin()

app = QApplication([])
win = MainWin()
app.exec_()