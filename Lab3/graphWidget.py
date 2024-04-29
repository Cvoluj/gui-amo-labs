import numpy as np
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from functions import lagrange_interpolation, Point

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class GraphWidget(QWidget):
    function_name_map = {
        'sin_x': 'sin(x)',
        'sin_x_square': 'sin(x^2)',
    }

    def __init__(self, *args):
        super().__init__()
        self.initUI(*args)

    def initUI(self, *args):
        layout = QVBoxLayout()

        self.fig, self.axs = plt.subplots(3)
        self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvas)

        self.setLayout(layout)

    def update_function_graph(self, a_dot, b_dot, function):
        self.axs[0].clear()
        self.axs[0].set_title('Function')

        tx = np.linspace(a_dot, b_dot, 10000)
        y = [function(x) for x in tx]
        self.axs[0].plot(tx, y, label=f'{self.function_name_map[function.__name__]}')

        self.axs[0].legend()
        self.fig.tight_layout()
        self.canvas.draw()

    def update_interpolation_graph(self, points_list: list[Point], interpolation_dots):
        self.axs[1].clear()
        self.axs[1].set_title('Interpolation')
        print(len(points_list), len(interpolation_dots))
        self.ty = lagrange_interpolation(points_list, interpolation_dots)
        self.axs[1].plot(interpolation_dots, self.ty)

        self.fig.tight_layout()
        self.canvas.draw()

    def update_interpolation_error_graph(self, interpolation_dots, function):
        self.axs[2].clear()
        self.axs[2].set_title('Interpolation Error')

        y = [function(dot) for dot in interpolation_dots]
        self.axs[2].plot(interpolation_dots, [(y[i] - self.ty[i]) for i in range(len(interpolation_dots))])

        self.fig.tight_layout()
        self.canvas.draw()
