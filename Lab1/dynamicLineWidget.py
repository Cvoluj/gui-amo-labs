from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QSizePolicy, QMessageBox
from PyQt5 import Qt
from functions import CalculationError

from abstract import MainWindowStyle, DnDMixin, UploadFileButton


class dynamicLineWidget(QWidget, DnDMixin):

    def __init__(self, *args):
        super().__init__()
        self.initUI(*args)
        self.setAcceptDrops(True)
        self.calculateAction = None
        self.values = list()
        self.results = list()

        self.btn_load_file.clicked.connect(self.load_file_dialog)
        self.btn_calculate.clicked.connect(self.calculate)

    def initUI(self, *args):
        layout = QVBoxLayout()
        btn_layout = QHBoxLayout()

        self.instructions = QLabel('1.Запишіть числа розділені пробілом або комою\nДля загрузки файлів можете перетягнути файл або натиснути "⭳" \n2.Якщо файл прийнято натисніть Calculate')
        self.btn_load_file = UploadFileButton()
        self.btn_calculate = QPushButton('Calculate')
        self.btn_calculate.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.btn_calculate.setToolTip('start calculations')

        btn_layout.addWidget(self.btn_load_file)
        btn_layout.addWidget(self.btn_calculate)

        self.algorithm_label = QLabel("Your Algorithm")
        self.algorithm_label.setAlignment(Qt.Qt.AlignCenter)

        layout.addWidget(self.instructions)
        layout.addLayout(btn_layout)
        layout.addWidget(self.algorithm_label)

        self.labels = []
        self.line_edits = []

        for label_name in args:
            label = QLabel(label_name)
            line_edit = QLineEdit()
            layout.addWidget(label)
            layout.addWidget(line_edit)
            self.labels.append(label)
            self.line_edits.append(line_edit)

        self.label3 = QLabel('Результати:')
        self.line_edit3 = QLineEdit()
        self.line_edit3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        layout.addWidget(self.label3)
        layout.addWidget(self.line_edit3)

        self.setLayout(layout)

    def load_file_dialog(self):
        try:
            if self.btn_load_file.readedFileText:
                for index, line_edit in enumerate(self.line_edits):
                    line_edit.setText(self.btn_load_file.readedFileText[index])
        except IndexError as e:
            QMessageBox.warning(self, "Error", "After reading file there are still empty rows")
        except Exception as e:
            QMessageBox.warning(self, "Error", "Upload only text files")

    def calculate(self):

        success = self.validateLines(*[line_edit.text() for line_edit in self.line_edits])
        if success:
            try:
                results = self.calculateAction(*self.values)
                self.line_edit3.setText(', '.join(format(result, '.3f') for result in results))
            except CalculationError as ce:
                QMessageBox.warning(self, "Error", str(ce))

    def addCalculateButtonAction(self, method):
        self.calculateAction = method
        

    def pasteReadedFile(self):
        for index, line_edit in enumerate(self.line_edits):
                    line_edit.setText(self.readedFileText[index])

    def validateLines(self, *args: str):
        self.values = [arg.replace(',', ' ').strip().split() for arg in args]

        try:
            converted_values = list()
            for line in self.values:
                converted_line = [float(value) for value in line]
                converted_values.append(converted_line)
            self.values = converted_values
        except ValueError:
            QMessageBox.warning(self, "Error", "пропущена кома, пробіл або введено неправильні значення")
            return False
        return True


class dynamicLineWindow(dynamicLineWidget, MainWindowStyle):

    def __init__(self, title, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle(title)
        self.setGeometry(200, 200, 300, 200)