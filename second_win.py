from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QWidget,QLabel,QPushButton,QVBoxLayout,QApplication,QLineEdit,QHBoxLayout
from instr import *
from PyQt5.QtGui import QFont
from final_win import *
class Experiment():
    def __init__(self,age,test1,test2,test3):
        self.age = age
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3
        

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
        
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.move(win_x,win_y)
        self.resize(win_width,win_height)

    def initUI(self):
        self.name = QLabel(txt_name)
        self.name_le = QLineEdit('')
        self.name_le.setFixedSize(250,25)
        self.name_le.setClearButtonEnabled(True)
        self.name_le.setPlaceholderText('Володимир Олександрович Зеленський')


        self.age = QLabel(txt_age)
        self.age_le = QLineEdit('')
        self.age_le.setClearButtonEnabled(True)
        self.age_le.setPlaceholderText('14')

        self.test_1 = QLabel(txt_test1)
        self.btn_test1 = QPushButton(txt_starttest1)
        self.test1_le = QLineEdit('')
        self.test1_le.setClearButtonEnabled(True)
        self.test1_le.setPlaceholderText('75')

        self.test_2 = QLabel(txt_test2)
        self.btn_test2 = QPushButton(txt_starttest2)

        self.test_3 = QLabel(txt_test3)
        self.btn_test3 = QPushButton(txt_starttest3)

        self.test2_le = QLineEdit('')
        self.test2_le.setClearButtonEnabled(True)
        self.test2_le.setPlaceholderText('75')
        self.test3_le = QLineEdit('')
        self.test3_le.setClearButtonEnabled(True)
        self.test3_le.setPlaceholderText('75')

        self.btn_next = QPushButton(txt_sendresults)

        self.txt_timer = QLabel(txt_timer)
        self.txt_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.txt_timer.setStyleSheet('color: rgb(0,0,0)')

        self.layout_line1 = QVBoxLayout()
        self.layout_line2 = QVBoxLayout()
        self.main_layout_line = QHBoxLayout()
        self.layout_line2.addWidget(self.name, alignment= Qt.AlignLeft)
        self.layout_line2.addWidget(self.name_le, alignment= Qt.AlignLeft)
        self.layout_line2.addWidget(self.age, alignment= Qt.AlignLeft)
        self.layout_line2.addWidget(self.age_le, alignment= Qt.AlignLeft)
        self.layout_line2.addWidget(self.test_1, alignment= Qt.AlignLeft)
        self.layout_line2.addWidget(self.btn_test1, alignment= Qt.AlignLeft)
        self.layout_line2.addWidget(self.test1_le, alignment= Qt.AlignLeft)
        self.layout_line2.addWidget(self.test_2, alignment= Qt.AlignLeft)
        self.layout_line2.addWidget(self.btn_test2, alignment= Qt.AlignLeft)
        self.layout_line2.addWidget(self.test_3, alignment= Qt.AlignLeft)
        self.layout_line2.addWidget(self.btn_test3, alignment= Qt.AlignLeft)
        self.layout_line2.addWidget(self.test2_le, alignment= Qt.AlignLeft)
        self.layout_line2.addWidget(self.test3_le, alignment= Qt.AlignLeft)
        self.layout_line2.addWidget(self.btn_next, alignment= Qt.AlignLeft)
        self.layout_line1.addWidget(self.txt_timer, alignment= Qt.AlignRight)
        self.main_layout_line.addLayout(self.layout_line2)
        self.main_layout_line.addLayout(self.layout_line1)
        self.setLayout(self.main_layout_line)

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
        self.btn_test1.clicked.connect(self.timer_test1)
        self.btn_test2.clicked.connect(self.timer_test2)
        self.btn_test3.clicked.connect(self.timer_test3)


    def next_click(self):
        self.hide()
        self.exp = Experiment(int(self.age_le.text()),self.test1_le.text(),self.test2_le.text(),self.test3_le.text())
        self.index = (4*(int(self.exp.test1)+int(self.exp.test2)+int(self.exp.test3))-200)/10
        self.fw = FinalWin(self.index,self.result())
    def result(self):
        if self.exp.age >= 15:
            if self.index >= 15:
                return txt_res1
            elif 11<=self.index<=14.9:
                return txt_res2
            elif 6<=self.index<=10.9:
                return txt_res3
            elif 0.5<=self.index<=5.9:
                return txt_res4
            elif self.index<=0.4:
                return txt_res5
        elif 14>=self.exp.age >= 13:
            if self.index >= 16.5:
                return txt_res1
            elif 12.5<=self.index<=16.4:
                return txt_res2
            elif 7.5<=self.index<=12.4:
                return txt_res3
            elif 2<=self.index<=7.4:
                return txt_res4
            elif self.index<=1.9:
                return txt_res5
        elif 12>=self.exp.age >= 11:
            if self.index >= 18:
                return txt_res1
            elif 14<=self.index<=17.9:
                return txt_res2
            elif 9<=self.index<=13.9:
                return txt_res3
            elif 3.5<=self.index<=8.9:
                return txt_res4
            elif self.index<=3.4:
                return txt_res5
        elif 10>=self.exp.age >= 9:
            if self.index >= 19.5:
                return txt_res1
            elif 15.5<=self.index<=19.4:
                return txt_res2
            elif 10.5<=self.index<=15.4:
                return txt_res3
            elif 5<=self.index<=10.4:
                return txt_res4
            elif self.index<=4.9:
                return txt_res5
        elif 8>=self.exp.age >= 7:
            if self.index >= 21:
                return txt_res1
            elif 17<=self.index<=20.9:
                return txt_res2
            elif 12<=self.index<=16.9:
                return txt_res3
            elif 6.5<=self.index<=11.9:
                return txt_res4
            elif self.index<=6.4:
                return txt_res5

    def timer_test1(self):
        global time
        self.timer = QTimer()
        time = QTime(0, 0, 15)
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.txt_timer.setText(time.toString('hh:mm:ss'))
        self.txt_timer.setStyleSheet('color: rgb(0:0:0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def timer_test2(self):
        global time
        self.timer = QTimer()
        time = QTime(0, 0, 30)
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.txt_timer.setText(time.toString('hh:mm:ss')[6:8])
        self.txt_timer.setStyleSheet('color: rgb(0,0,0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def timer_test3(self):
        global time
        self.timer = QTimer()
        time = QTime(0, 1, 0)
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)
    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.txt_timer.setText(time.toString('hh:mm:ss'))
        if int(time.toString('hh:mm:ss')[6:8])>=45:
            self.txt_timer.setStyleSheet('color: rgb(0,255,0)')
        elif int(time.toString('hh:mm:ss')[6:8])<=15:
            self.txt_timer.setStyleSheet('color: rgb(0,255,0)')
        else:
            self.txt_timer.setStyleSheet('color: rgb(0,0,0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()