import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QTabWidget
from bubbleSortWidget import BubbleSortWidget
from studentInfo import StudentInfo
from bublle_sort import bublle_sort
from abstract import MainWindowStyle
from generationWidget import generationWidget


class MainWindow(MainWindowStyle):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('AMO Lab2')
        self.setGeometry(100, 100, 200, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.notebook = QTabWidget()
        self.layout.addWidget(self.notebook)

        self.initUI()

    def initUI(self):
        student_info = StudentInfo()
        self.notebook.addTab(student_info, "Student Info")

        dnm_widget = BubbleSortWidget(*['Values'])
        dnm_widget.btn_calculate.setText('Sort')
        dnm_widget.algorithm_label.setText('Bubble sort from start to end')
        dnm_widget.addCalculateButtonAction(bublle_sort)

        self.notebook.addTab(dnm_widget, "Bubble Sort")

        generation_widget = generationWidget()

        self.notebook.addTab(generation_widget, "Generation")
        print(self.window())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
