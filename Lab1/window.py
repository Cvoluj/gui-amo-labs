import sys
from PyQt5.QtGui import QDragEnterEvent, QDropEvent
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QCheckBox, QRadioButton, QComboBox, QMainWindow, QHBoxLayout

from abstract import MainWindowStyle, DnDQTextEdit
from doubleLineWidget import dobuleLineWindow
from studentInfo import StudentInfo


class MainWindow(MainWindowStyle):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.tasks = [self.open_task1, self.open_task2, self.open_tesk3]
        self.setGeometry(100, 100, 200, 200)
        self.setWindowTitle('AMO Lab1')

        self.layout = QVBoxLayout()
        student_info = StudentInfo()

        btn_layout = QHBoxLayout()

        btn_task1 = QPushButton('Task1')
        btn_task2 = QPushButton('Task2')
        btn_task3 = QPushButton('Task3')

        self.btns = [btn_task1, btn_task2, btn_task3]
        for btn, task in zip(self.btns, self.tasks):
            btn.clicked.connect(task)
            btn_layout.addWidget(btn)

        self.layout.addWidget(student_info)
        self.layout.addLayout(btn_layout)

        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)
    
    def open_task1(self):
        self.task1_window = dobuleLineWindow("Task1", *['Значення а:', 'Значення b:'])
        self.task1_window.addCalculateButtonAction(task1)
        self.task1_window.show()

    def open_task2(self):
        self.task2_window = dobuleLineWindow("Task2")
        self.task2_window.addCalculateButtonAction(task2)
        self.task2_window.show()
        pass
    def open_tesk3(self):
        self.task3_window = dobuleLineWindow("Task3")
        self.task3_window.addCalculateButtonAction(task3)
        self.task3_window.show()

def task1():
    print('3')

def task2():
    print('4')
    
def task3():
    print('5')
        

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
