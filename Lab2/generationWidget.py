import numpy as np
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt

from bublle_sort import bublle_sort
from graphs import graph_input, graph_theoretical


class generationWidget(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(*args)

        self.generated_arrays: list
        self.button_generate_ten_arrays.clicked.connect(self.generate)
        self.button_plot_input_graph.clicked.connect(self.plot_input_graph)
        self.button_plot_theoretical_graph.clicked.connect(self.plot_theoretical_graph)

    def initUI(self, *args):
        layout = QVBoxLayout()

        button_plot_layout = QHBoxLayout()
        button_plot_layout.setAlignment(Qt.AlignTop)
        self.button_plot_theoretical_graph = QPushButton('Theoretical graph')
        self.button_plot_input_graph = QPushButton('Arrays graph')

        button_plot_layout.addWidget(self.button_plot_theoretical_graph)
        button_plot_layout.addWidget(self.button_plot_input_graph)

        self.generation_layout = QVBoxLayout()
        self.button_generate_ten_arrays = QPushButton('Generate ten arrays')
        self.label_generate_ten_arrays = QLabel('')
        self.label_generate_ten_arrays.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        self.generation_layout.addWidget(self.button_generate_ten_arrays)
        self.generation_layout.addWidget(self.label_generate_ten_arrays)
        self.generation_layout.setAlignment(Qt.AlignTop)

        layout.addLayout(self.generation_layout)
        self.generation_layout.addLayout(button_plot_layout)
        self.setLayout(layout)

    def generate_ten_arrays(self) -> list:
        generated_arrays = []
        # sizes = [10, 20, 100, 200, 500, 1000, 1500, 3000, 3500, 4000]
        sizes = [10, 20, 100, 200, 500, 1000, 2000, 5000, 7000, 10000]
        for size in sizes:
            random_array = np.random.randint(-10000, 10000, size)
            generated_arrays.append(random_array)
        return generated_arrays

    def generate(self):
        self.generated_arrays = self.generate_ten_arrays()
        self.sorted_arrays = bublle_sort(*self.generated_arrays)

        self.label_generate_ten_arrays.setText('Ten arrays were generated')

    def plot_theoretical_graph(self):
        parent_window = self.window()
        graph_theoretical(self.sorted_arrays, parent_window=parent_window)

    def plot_input_graph(self):
        parent_window = self.window()
        graph_input(self.sorted_arrays, parent_window=parent_window)
