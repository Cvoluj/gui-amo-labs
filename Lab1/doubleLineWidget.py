from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QSizePolicy, QMessageBox
from abstract import MainWindowStyle, DnDMixin, UploadFileButton


class doubleLineWidget(QWidget, DnDMixin):

    def __init__(self, label1_name: str = 'Label 1:', label2_name: str = 'Label 2'):
        super().__init__()
        self.initUI(label1_name, label2_name)
        self.setAcceptDrops(True)
        self.calculateAction = None

        self.btn_load_file.clicked.connect(self.load_file_dialog)
        self.btn_calculate.clicked.connect(self.calculate)

    def initUI(self, label1_name: str, label2_name: str):
        layout = QVBoxLayout()
        btn_layout = QHBoxLayout()

        instructions = QLabel('1.Запишіть числа розділені пробілом або комою\nДля загрузки файлів можете перетягнути файл або натиснути "⭳" \n2.Якщо файл прийнято натисніть Calculate')
        self.btn_load_file = UploadFileButton()
        self.btn_calculate = QPushButton('Calculate')
        self.btn_calculate.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.btn_calculate.setToolTip('start calculations')

        btn_layout.addWidget(self.btn_load_file)
        btn_layout.addWidget(self.btn_calculate)

        layout.addWidget(instructions)
        layout.addLayout(btn_layout)

        self.label1 = QLabel(label1_name)
        self.line_edit1 = QLineEdit()

        layout.addWidget(self.label1)
        layout.addWidget(self.line_edit1)

        self.label2 = QLabel(label2_name)
        self.line_edit2 = QLineEdit()

        layout.addWidget(self.label2)
        layout.addWidget(self.line_edit2)

        self.setLayout(layout)

    def load_file_dialog(self):
        try:
            self.line_edit1.setText(self.btn_load_file.readedFileText[0])
            self.line_edit2.setText(self.btn_load_file.readedFileText[1])
        except IndexError as e:
            QMessageBox.warning(self, "Error", "After reading file there are still empty rows")
        except Exception as e:
            QMessageBox.warning(self, "Error", "Upload only text files")

    def calculate(self):
        self.validateLines()
        try:
            self.calculateAction()
        except TypeError as e:
            print(e)
        except Exception as e:
            print(e)

    def addCalculateButtonAction(self, method):
        self.calculateAction = method

    def pasteReadedFile(self):
        self.line_edit1.setText(self.readedFileText[0])
        self.line_edit2.setText(self.readedFileText[1])

    def validateLines(self, line_values: str):
        values = line_values.replace(',', ' ').strip().split()

        for value in values:
            try:
                int_value = int(value)
            except ValueError:
                try:
                    float_value = float(value)
                except ValueError:
                    QMessageBox.warning(self, "Error", "пропущена кома, пробіл або введено неправильні значення")
                    return False
        return True


class dobuleLineWindow(doubleLineWidget, MainWindowStyle):

    def __init__(self, title, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle(title)
        self.setGeometry(200, 200, 300, 200)