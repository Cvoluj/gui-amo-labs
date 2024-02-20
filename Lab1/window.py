import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout

from abstract import MainWindowStyle
from dynamicLineWidget import dynamicLineWindow
from studentInfo import StudentInfo
import functions


class MainWindow(MainWindowStyle):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.tasks = [self.open_task1, self.open_task2, self.open_task3]
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
        self.task1_window = dynamicLineWindow("Task1", *['Значення а:', 'Значення c:'])
        self.task1_window.algorithm_label.setText('Y1=sqrt(a + c) + 1 / (a + c)')
        self.task1_window.addCalculateButtonAction(functions.calculate_y1)
        
        self.task1_window.show()

    def open_task2(self):
        self.task2_window = dynamicLineWindow("Task2")
        self.task2_window.instructions.setText('1. Натисніть Calculate')
        self.task2_window.algorithm_label.setText('57.567x^2 - 11.675x - 34.114 = 0')
        self.task2_window.btn_load_file.setVisible(False)
        self.task2_window.addCalculateButtonAction(functions.find_roots)
        self.task2_window.show()
        
    def open_task3(self):
        self.task3_window = dynamicLineWindow("Task3", *['Значення а:', 'Значення c:', 'значення g:'])
        self.task3_window.algorithm_label.setText('f = sum[i=0, 10](ai^2 + 56ci*f*gi)')
        self.task3_window.addCalculateButtonAction(functions.calculate_f)

        self.task3_window.show()

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
