import os
from typing import Union
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtGui import QDragEnterEvent, QDropEvent
from PyQt5.QtWidgets import QMainWindow, QTextEdit

class MainWindowStyle(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_stylesheet('design.qss')

    def load_stylesheet(self, filename):
        style_file = QFile(filename)
        if not style_file.open(QFile.ReadOnly | QFile.Text):
            print(f"Could not open stylesheet file {filename}")
            return

        # Read the QSS content and apply it to the application
        stream = QTextStream(style_file)
        self.setStyleSheet(stream.readAll())
        style_file.close()


class DnDQTextEdit(QTextEdit):

    def __init__(self):
        super().__init__()
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


    def pasteReadedFile(self):
        self.setText('\n'.join(self.readedFileText))