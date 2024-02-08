from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit
from abstract import DnDMixin


class doubleLineWidget(QWidget, DnDMixin):

    def __init__(self, label1_name: str = 'Label 1:', label2_name: str = 'Label 2'):
        super().__init__()
        self.initUI(label1_name, label2_name)
        self.setAcceptDrops(True)


    def initUI(self, label1_name: str = 'Label 1:', label2_name: str = 'Label 2'):
        layout = QVBoxLayout()

        self.label1 = QLabel(label1_name)
        self.line_edit1 = QLineEdit()

        layout.addWidget(self.label1)
        layout.addWidget(self.line_edit1)

        self.label2 = QLabel(label2_name)
        self.line_edit2 = QLineEdit()

        layout.addWidget(self.label2)
        layout.addWidget(self.line_edit2)

        self.setLayout(layout)

    def pasteReadedFile(self):
        self.line_edit1.setText(self.readedFileText[0])
        self.line_edit2.setText(self.readedFileText[1])
