import numpy as np

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from abstract import DnDMixin, UploadFileButton
from functions import equation, bisection
from plotDialog import PlotDialog


class EquationWidget(QWidget, DnDMixin):

    def __init__(self, *args):
        super().__init__()
        self.setAcceptDrops(True)
        self.initUI(*args)

        self.upload_file_button.clicked.connect(self.load_file_dialog)
        self.calculate_button.clicked.connect(self.calculate)

    def initUI(self, *args):
        layout = QVBoxLayout()

        self.upload_file_button = UploadFileButton()
        self.upload_file_button.setText("Upload values from file")

        equation_label = QLabel('x^3 - x + 1 = 0')
        equation_label.setAlignment(Qt.AlignCenter | Qt.AlignTop)

        a_label = QLabel('a:')
        self.a_edit = QLineEdit()
        b_label = QLabel('b:')
        self.b_edit = QLineEdit()
        e_label = QLabel('ε:')
        self.e_edit = QLineEdit()

        self.line_edits = [self.a_edit, self.b_edit, self.e_edit]
        for line_edit in self.line_edits:
            line_edit.setMinimumWidth(300)

        plot_layout = QVBoxLayout()

        self.fig, self.axs = plt.subplots(1)
        self.canvas = FigureCanvas(self.fig)
        self.plot_equation()


        self.calculate_button = QPushButton('Calculate')

        plot_layout.addWidget(equation_label)
        plot_layout.addWidget(self.canvas)
        plot_layout.addWidget(self.upload_file_button)
        plot_layout.addWidget(a_label)
        plot_layout.addWidget(self.a_edit)
        plot_layout.addWidget(b_label)
        plot_layout.addWidget(self.b_edit)
        plot_layout.addWidget(e_label)
        plot_layout.addWidget(self.e_edit)
        plot_layout.addWidget(self.calculate_button)

        layout.addLayout(plot_layout)
        self.setLayout(layout)

    def pasteReadedFile(self):
        for index, line_edit in enumerate(self.line_edits):
            line_edit.setText(self.readedFileText[index])

    def load_file_dialog(self):
        try:
            if self.upload_file_button.readedFileText:
                for index, line_edit in enumerate(self.line_edits):
                    line_edit.setText(self.upload_file_button.readedFileText[index])
        except IndexError as e:
            QMessageBox.warning(self, "Error", "After reading file there are still empty rows")
        except Exception as e:
            QMessageBox.warning(self, "Error", "Upload only text files")

    def plot_equation(self):
        self.axs.clear()

        x_values = np.linspace(-3, 3, 1000)
        y_values = [equation(x) for x in x_values]

        self.axs.plot(x_values, y_values, label='Equation: $f(x) = x^3 - x + 1$')
        self.axs.axhline(0, color='black', linewidth=0.5)
        self.axs.axvline(0, color='black', linewidth=0.5)
        self.axs.set_xlabel('x')
        self.axs.set_ylabel('f(x)')
        self.axs.grid(True)
        self.axs.legend()

        self.fig.tight_layout()
        self.canvas.draw()

    def calculate(self):
        try:
            a = float(self.a_edit.text().strip())
            b = float(self.b_edit.text().strip())
            precision = float(self.e_edit.text().strip())
            if precision < 0:
                raise QMessageBox.warning(self, 'Error', 'Epsilon cannot be negative')

            result = bisection(a, b, precision)
            if result is None:
                raise QMessageBox.warning(self, 'Error', 'No solution found, try another boundaries')

            dialog = PlotDialog(result, len(str(precision).split('0.')[1]))
            dialog.show()

        except Exception:
            QMessageBox.warning(self, 'Error', 'There are error value in Text Edits')
