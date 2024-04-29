import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QTabWidget, QSizePolicy

from settingsWidget import SettingsWidget
from abstract import MainWindowStyle
from studentInfo import StudentInfo
from graphWidget import GraphWidget


class MainWindow(MainWindowStyle):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('AMO Lab3')

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

        settings_widget = SettingsWidget()
        self.notebook.addTab(settings_widget, "Settings")

        graph_widget = GraphWidget()
        self.notebook.addTab(graph_widget, "Graph")

        settings_widget.buildFucntionSignal.connect(graph_widget.update_function_graph)
        settings_widget.buildInterpolationSignal.connect(graph_widget.update_interpolation_graph)
        settings_widget.buildInterpolationErrorSignal.connect(graph_widget.update_interpolation_error_graph)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
