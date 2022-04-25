from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QWidget,QLabel,QPushButton,QVBoxLayout,QApplication,QLineEdit,QHBoxLayout
from instr import *
from second_win import*

class FinalWin(QWidget):
    def __init__(self,index,result):
        super().__init__()
        self.index = index
        self.result = result
        self.set_appear()
        self.initUI()  
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.move(win_x,win_y)
        self.resize(win_width,win_height)

    def initUI(self):
        self.index_text = QLabel(txt_index + str(self.index))
        self.work_text = QLabel(txt_workheart + self.result)
        

        self.layout_line1 = QVBoxLayout()
        self.layout_line1.addWidget(self.index_text, alignment= Qt.AlignCenter)
        self.layout_line1.addWidget(self.work_text, alignment= Qt.AlignCenter)
        self.setLayout(self.layout_line1)