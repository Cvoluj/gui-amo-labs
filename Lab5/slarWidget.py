from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QMessageBox, QGridLayout
from PyQt5.QtCore import Qt


from abstract import DnDMixin, UploadFileButton
from functions import gausian


class SlarWidget(QWidget, DnDMixin):

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
        self.calculate_button = QPushButton("Find system solutions")

        slar_label = QLabel('System of linear equations')
        slar_label.setAlignment(Qt.AlignCenter | Qt.AlignTop)

        self.matrix_layout = QGridLayout()
        self.create_matrix(3, 4)

        x1_label = QLabel('x1:')
        x2_label = QLabel('x2:')
        x3_label = QLabel('x3:')
        x1_label.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        x2_label.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        x3_label.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        self.x_labels = [x1_label, x2_label, x3_label]

        bottom_layout = QVBoxLayout()
        bottom_layout.addWidget(self.upload_file_button)
        bottom_layout.addWidget(self.calculate_button)
        for label in self.x_labels:
            bottom_layout.addWidget(label)

        layout.addWidget(slar_label)
        layout.addLayout(self.matrix_layout)
        layout.addLayout(bottom_layout)

        self.setLayout(layout)

    def pasteReadedFile(self):
        lines = str('\n'.join([str(val) for val in self.readedFileText])).split('\n')
        for row_index, line in enumerate(lines):
            values = line.split(' ')
            for col_index, value in enumerate(values):
                self.line_edits[row_index][col_index].setText(value)

    def load_file_dialog(self):
        try:
            if self.upload_file_button.readedFileText:
                lines = str('\n'.join([str(val) for val in self.upload_file_button.readedFileText])).split('\n')
                for row_index, line in enumerate(lines):
                    values = line.split(' ')
                    for col_index, value in enumerate(values):
                        self.line_edits[row_index][col_index].setText(value)
        except IndexError as e:
            QMessageBox.warning(self, "Error", "After reading file there are still empty rows")
        except Exception as e:
            QMessageBox.warning(self, "Error", "Upload only text files")

    def create_matrix(self, rows, cols):
        self.line_edits = []
        self.labels = []
        for i in range(rows):
            row = []
            self.line_edits.append(row)
            for j in range(cols):
                text_edit = QLineEdit()
                text_edit.setMinimumSize(50, 30)
                text_edit.setMaximumSize(50, 30)
                text_label = QLabel(f'x{j + 1}')
                if j <= 1:
                    self.matrix_layout.addWidget(text_label, i, 2 * j + 1)
                elif j == 2:
                    self.matrix_layout.addWidget(QLabel(f'x{j + 1}='), i, 2 * j + 1)

                self.matrix_layout.addWidget(text_edit, i, 2 * j)
                self.line_edits[i].append(text_edit)
                self.labels.append(text_label)

    def calculate(self):
        try:
            matrix = []
            for row in self.line_edits:
                empty_row = []
                matrix.append(empty_row)
                for value in row:
                    empty_row.append(float(value.text()))
            print(matrix)
            calculated_values = gausian(matrix, len(matrix))
            for index, value in enumerate(calculated_values):
                self.x_labels[index].setText(f'x{index + 1}: {value}')
        except Exception:
            QMessageBox.warning(self, "Error", "Couldn't calculate values, try another values")

