import numpy as np
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from functions import equation
from design import DESIGN_QSS


class PlotDialog(QDialog):
    def __init__(self, result, precision):
        super().__init__()
        self.setStyleSheet(DESIGN_QSS)
        self.fig, self.axs = plt.subplots()
        self.canvas = FigureCanvas(self.fig)

        x_values = np.linspace(-3, 3, 1000)
        y_values = [equation(x) for x in x_values]
        self.axs.plot(x_values, y_values, label='Equation: $f(x) = x^3 - x + 1$')
        self.axs.scatter(result, equation(result), color='red', label='Result')

        self.axs.axhline(0, color='black', linewidth=0.5)
        self.axs.axvline(0, color='black', linewidth=0.5)
        self.axs.set_xlabel('x')
        self.axs.set_ylabel('f(x)')
        self.axs.grid(True)
        self.axs.legend()

        self.canvas.draw()

        root_label = QLabel(f'The approximate root: {result}')
        precision_label = QLabel(f'Precision: {precision}')

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(root_label)
        layout.addWidget(precision_label)
        self.setLayout(layout)