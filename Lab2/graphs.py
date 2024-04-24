import numpy as np
from PyQt5.QtWidgets import QVBoxLayout, QDialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from scipy.interpolate import interp1d

from bublle_sort import BubbleSortResult


def graph_input(sorted_results: list[BubbleSortResult], parent_window):
    sub_window = QDialog(parent_window)
    sub_window.setWindowTitle('Inputed Data Graph')
    sub_window.setGeometry(200, 200, 600, 400)

    main_layout = QVBoxLayout(sub_window)

    sizes_list = [len(result.sequence) for result in sorted_results]
    times_list = [result.execution_time for result in sorted_results]

    print(sizes_list, times_list)

    f = interp1d(sizes_list, times_list, kind='cubic')

    sizes_smooth = np.linspace(min(sizes_list), max(sizes_list), 1000)
    times_smooth = f(sizes_smooth)

    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(sizes_smooth, times_smooth, linestyle='-', color='green')
    ax.set_title('Graph')
    ax.set_xlabel('Size')
    ax.set_ylabel('Time(s)')
    canvas = FigureCanvas(fig)

    main_layout.addWidget(canvas)

    sub_window.setLayout(main_layout)
    sub_window.show()


def graph_theoretical(sorted_results: list[BubbleSortResult], parent_window):
    sub_window = QDialog(parent_window)
    sub_window.setWindowTitle('Theoretical Graph')
    sub_window.setGeometry(200, 200, 600, 400)

    main_layout = QVBoxLayout(sub_window)

    sizes_list = [len(result.sequence) for result in sorted_results]
    operations_list = [result.operations for result in sorted_results]

    print(sizes_list, operations_list)

    f = interp1d(sizes_list, operations_list, kind='cubic')

    sizes_smooth = np.linspace(min(sizes_list), max(sizes_list), 1000)
    times_smooth = f(sizes_smooth)

    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(sizes_smooth, times_smooth, linestyle='-', color='green')
    ax.set_title('Graph')
    ax.set_xlabel('Size')
    ax.set_ylabel('Operations')
    canvas = FigureCanvas(fig)
    main_layout.addWidget(canvas)

    sub_window.setLayout(main_layout)
    sub_window.show()