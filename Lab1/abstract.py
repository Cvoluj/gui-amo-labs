import os
from typing import Union, List
from PyQt5.QtCore import QFile, QTextStream, Qt, QMimeData
from PyQt5.QtGui import QDragEnterEvent, QDropEvent, QDrag
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QWidget, QLabel, QLineEdit, QVBoxLayout, QTextEdit

class MainWindowStyle(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_stylesheet('design.qss')

    def load_stylesheet(self, filename):
        style_file = QFile(filename)
        if not style_file.open(QFile.ReadOnly | QFile.Text):
            print(f"Could not open stylesheet file {filename}")
            return

        stream = QTextStream(style_file)
        self.setStyleSheet(stream.readAll())
        style_file.close()

class DnDMixin():
    def __init__(self):
        self.readedFileText = str()

    def dragEnterEvent(self, a0: QDragEnterEvent | None) -> None:
        if a0.mimeData().hasUrls():
            a0.accept()
        else:
            a0.ignore()

    def dropEvent(self, event: QDragEnterEvent):
        mime_data = event.mimeData()
        urls = mime_data.urls()
        for url in urls:
            file_path = url.toLocalFile()
            try:
                with open(file_path, 'r') as file:
                    self.readedFileText = [line.strip() for line in file.readlines()]
                self.pasteReadedFile()
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")


class DnDQTextEdit(QTextEdit, DnDMixin):

    def __init__(self):
        super().__init__()

    def pasteReadedFile(self):
        print(self.readedFileText)
        self.setText('\n'.join(self.readedFileText))

