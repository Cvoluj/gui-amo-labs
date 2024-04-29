import re

from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QLineEdit, QMessageBox, \
    QRadioButton, QTableWidget, QHeaderView, QTableWidgetItem
from PyQt5.QtCore import Qt, QRegExp, pyqtSignal

from abstract import DnDMixin, UploadFileButton
from functions import sin_x, sin_x_square, Point, lagrange_interpolation


class SettingsWidget(QWidget, DnDMixin):
    buildFucntionSignal = pyqtSignal(float, float, object)
    buildInterpolationSignal = pyqtSignal(list, list)
    buildInterpolationErrorSignal = pyqtSignal(list, object)
    def __init__(self, *args):
        super().__init__()
        self.setAcceptDrops(True)
        self.initUI(*args)

        self.splice_edit.setValidator((QRegExpValidator(QRegExp(r'^\d+\s\d+$'), self)))

        self.upload_file_button.clicked.connect(self.load_file_dialog)
        self.generate_nodes_by_splice_button.clicked.connect(self.on_generate_nodes_by_splice)
        self.generate_dots.clicked.connect(self.on_generate_dots)
        self.build_table_and_graph_button.clicked.connect(self.on_build_table_and_graph_button)

        self.function = sin_x
        self.points_list: list[Point] = []

    def initUI(self, *args):
        layout = QVBoxLayout()

        self.upload_file_button = UploadFileButton()
        self.upload_file_button.setText("Upload values from file")


        splice_label = QLabel('Interpolation splice')
        self.splice_edit = QLineEdit()
        interpolation_nodes_label = QLabel('Interpolation nodes')
        self.interpolation_nodes_edit = QLineEdit()
        interpolation_dots_label = QLabel('Interpolation dots')
        self.interpolation_dots_edit = QLineEdit()

        self.line_edits = [self.splice_edit, self.interpolation_nodes_edit, self.interpolation_dots_edit]
        for line_edit in self.line_edits:
            line_edit.setMinimumWidth(300)

        self.generate_nodes_by_splice_button = QPushButton('Generate nodes by splice')
        self.generate_dots = QPushButton('Generate dots (enter quantity)')

        self.radio_method1 = QRadioButton("f(x) = sin(x)")
        self.radio_method2 = QRadioButton("f(x) = sin(x^2)")
        self.radio_method1.setChecked(True)
        self.radio_method1.toggled.connect(self.on_radio_button1_selected)
        self.radio_method2.toggled.connect(self.on_radio_button2_selected)

        self.build_table_and_graph_button = QPushButton('Build tables and graphs')



        settings_layout = QVBoxLayout()

        settings_layout.addWidget(self.upload_file_button)
        settings_layout.addWidget(splice_label)
        settings_layout.addWidget(self.splice_edit)
        settings_layout.addWidget(interpolation_nodes_label)
        settings_layout.addWidget(self.interpolation_nodes_edit)
        settings_layout.addWidget(self.generate_nodes_by_splice_button)
        settings_layout.addWidget(interpolation_dots_label)
        settings_layout.addWidget(self.interpolation_dots_edit)
        settings_layout.addWidget(self.generate_dots)
        settings_layout.addWidget(self.radio_method1)
        settings_layout.addWidget(self.radio_method2)
        settings_layout.addWidget(self.build_table_and_graph_button)

        nodes_table_layout = QVBoxLayout()

        nodes_table_label = QLabel('Interpolation Nodes Table')
        nodes_table_label.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        self.nodes_table = QTableWidget()
        self.nodes_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.nodes_table.setColumnCount(2)
        self.nodes_table.setHorizontalHeaderLabels(['x', 'f(x)'])

        nodes_table_layout.addWidget(nodes_table_label)
        nodes_table_layout.addWidget(self.nodes_table)


        top_layout = QHBoxLayout()
        top_layout.addLayout(settings_layout)
        top_layout.addLayout(nodes_table_layout)


        bottom_layout = QVBoxLayout()

        deflaction_table_label = QLabel('Deflection table')
        deflaction_table_label.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        self.deflection_table = QTableWidget()
        self.deflection_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.deflection_table.setColumnCount(3)
        self.deflection_table.setHorizontalHeaderLabels(['Real value', 'Calculated value', 'Refinement factor'])
        self.deflection_table.setMinimumWidth(750)
        bottom_layout.addWidget(deflaction_table_label)
        bottom_layout.addWidget(self.deflection_table)


        layout.addLayout(top_layout)
        layout.addLayout(bottom_layout)
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

    def on_radio_button1_selected(self):
        if self.radio_method1.isChecked():
            self.function = sin_x

    def on_radio_button2_selected(self):
        if self.radio_method2.isChecked():
            self.function = sin_x_square

    def on_generate_nodes_by_splice(self):
        a_dot, b_dot = self.parse_splice_edit()
        if a_dot is None or b_dot is None:
            return


        self.interpolation_nodes = [round(a_dot + i * 0.2, 1) for i in range(0, int((b_dot - a_dot) / 0.2) + 1)]
        self.interpolation_nodes_edit.setText(' '.join([str(val) for val in self.interpolation_nodes]))

    def on_generate_dots(self):
        a_dot, b_dot = self.parse_splice_edit()
        if a_dot is None or b_dot is None:
            return

        quantity = self.interpolation_dots_edit.text().strip()
        if re.match(r'^\d+$', quantity) is None:
            return
        quantity = int(quantity)
        self.interpolation_dots = [round(a_dot + i * (b_dot - a_dot) / (quantity - 1), 3) for i in range(0, quantity)]
        self.interpolation_dots_edit.setText(' '.join([str(val) for val in self.interpolation_dots]))

    def parse_splice_edit(self):
        try:
            splice_dots = self.splice_edit.text().split(' ')
            a_dot = float(splice_dots[0])
            b_dot = float(splice_dots[1])
            return a_dot, b_dot
        except Exception:
            error_message = "You must specify both splice boundaries."
            QMessageBox.warning(self, "Warning", error_message)
            return None, None

    def on_build_table_and_graph_button(self):
        self.points_list = [Point(node, self.function(node)) for node in self.interpolation_nodes]
        self.build_nodes_table()
        self.build_function_graph()
        self.build_interpolation_graph()
        self.build_interpolation_error_graph()
        self.build_interpolation_table()


    def build_nodes_table(self):
        try:
            num_rows = len(self.interpolation_nodes)
            self.nodes_table.setRowCount(num_rows)
            self.nodes_table.verticalHeader().setVisible(False)

            for row, node in enumerate(self.interpolation_nodes):
                self.nodes_table.setItem(row, 0,  QTableWidgetItem(str(node)))
                self.nodes_table.setItem(row, 1,  QTableWidgetItem(str(self.function(node))))
        except Exception:
            QMessageBox.warning(self, 'Warning', 'There are no values for building Nodes Table')

    def build_function_graph(self):
        try:
            a_dot, b_dot = self.parse_splice_edit()
            self.buildFucntionSignal.emit(a_dot, b_dot, self.function)
        except Exception:
            QMessageBox.warning(self, 'Warning', 'Error on building Function Graph')

    def build_interpolation_graph(self):
        try:
            self.buildInterpolationSignal.emit(self.points_list, self.interpolation_dots)
        except Exception:
            QMessageBox.warning(self, 'Warning', 'Error on building Interpolation Graph')

    def build_interpolation_error_graph(self):
        try:
            self.buildInterpolationErrorSignal.emit(self.interpolation_dots, self.function)
        except Exception:
            QMessageBox.warning(self, 'Warning', 'Error on building Interpolation Error Graph')

    def build_interpolation_table(self):
        try:
            ty = lagrange_interpolation(self.points_list, self.interpolation_nodes)
            error = [1 - ty[i] / self.points_list[i].y if self.points_list[i].y != 0.0 else '0.0' for i in range(len(self.points_list))]
            num_rows = len(error)
            self.deflection_table.setRowCount(num_rows)

            for row, value in enumerate(error):
                self.deflection_table.setItem(row, 0, QTableWidgetItem(str(self.points_list[row].y)))
                self.deflection_table.setItem(row, 1, QTableWidgetItem(str(ty[row])))
                self.deflection_table.setItem(row, 2, QTableWidgetItem(str(error[row])))
        except Exception:
            QMessageBox.warning(self, 'Warning', 'There are no values for building Interpolation Deflection Table')
