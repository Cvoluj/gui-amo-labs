import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QTabWidget, QSizePolicy


from abstract import MainWindowStyle
from studentInfo import StudentInfo
from equationWidget import EquationWidget


class MainWindow(MainWindowStyle):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('AMO Lab4')

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.notebook = QTabWidget()
        self.layout.addWidget(self.notebook)

        self.initUI()

    def initUI(self):
        student_info = StudentInfo()
        student_info.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.notebook.addTab(student_info, "Student Info")

        equation_widget = EquationWidget()
        self.notebook.addTab(equation_widget, "Equation")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
