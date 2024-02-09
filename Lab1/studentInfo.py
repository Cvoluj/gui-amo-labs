from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDragEnterEvent, QDropEvent
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QCheckBox, QRadioButton, QComboBox, QMainWindow, QHBoxLayout

class StudentInfo(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setObjectName('StudentInfo')
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        
        name_layout = QHBoxLayout()
        group_layout = QHBoxLayout()

        title_label = QLabel('Інформація про студента')
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        name_label = QLabel('ПІБ:')
        name_value_label = QLabel('Бережанський Данііл Вадимович')

        name_layout.addWidget(name_label)
        name_layout.addWidget(name_value_label)

        group_label = QLabel('Група:')
        group_value_label = QLabel('ІО-24')
        group_layout.addWidget(group_label)
        group_layout.addWidget(group_value_label)


        layout.addLayout(name_layout)
        layout.addLayout(group_layout)
        self.setLayout(layout)

