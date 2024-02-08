import sys
from PyQt5.QtGui import QDragEnterEvent, QDropEvent
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QCheckBox, QRadioButton, QComboBox, QMainWindow
from PyQt5.QtCore import QFile, QTextStream, QVariant
from abstract import MainWindowStyle, DnDQTextEdit
from doubleLineWidget import doubleLineWidget


class MainWindow(MainWindowStyle):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle('AMO App')

        self.layout = QVBoxLayout()

        button = QPushButton('Click Me')
        label = QLabel('Hello, World!')
        line_edit = QLineEdit()
        text_edit = DnDQTextEdit()
        checkbox = QCheckBox('Check me')
        radio_button = QRadioButton('Select me')
        combo_box = QComboBox()
        combo_box.addItems(['Option 1', 'Option 2', 'Option 3'])

        custom_widget = doubleLineWidget('Name1', 'Name2')

        self.layout.addWidget(button)
        self.layout.addWidget(label)
        self.layout.addWidget(line_edit)
        self.layout.addWidget(text_edit)
        self.layout.addWidget(checkbox)
        self.layout.addWidget(radio_button)
        self.layout.addWidget(combo_box)

        self.layout.addWidget(custom_widget)

        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

        

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
