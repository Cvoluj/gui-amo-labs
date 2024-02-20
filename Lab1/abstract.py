import mimetypes
from PyQt5.QtGui import QDragEnterEvent
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QTextEdit, QPushButton, QFileDialog, QMessageBox
from design import DESIGN_QSS

class MainWindowStyle(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_stylesheet(DESIGN_QSS)

    def load_stylesheet(self, filename):
        self.setStyleSheet(filename)


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
            except IndexError as e:
                QMessageBox.warning(self, "Error", "After reading file there are still empty rows")
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")
                QMessageBox.warning(self, "Error", "Upload only text files")


class DnDQTextEdit(QTextEdit, DnDMixin):

    def __init__(self):
        super().__init__()

    def pasteReadedFile(self):
        print(self.readedFileText)
        self.setText('\n'.join(self.readedFileText))


class UploadFileButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setText
        self.setText('⭳')
        self.setToolTip('Click to load a file')
        self.readedFileText = str()

        self.clicked.connect(self.upload_file)

    def is_text_file(self, file_path):
        mimetype, _ = mimetypes.guess_type(file_path)
        if mimetype and mimetype.startswith('text'):
            return True
        return False

    def upload_file(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Text files (*.txt *.csv);;All files (*)")

       
        
        if file_dialog.exec_():
            file_paths = file_dialog.selectedFiles()
            
            if not file_paths:
                return
            
            for file_path in file_paths:
                try:
                    if self.is_text_file(file_path):
                        with open(file_path, 'r') as file:
                            self.readedFileText = [line.strip() for line in file.readlines()]
                except IndexError as e:
                    QMessageBox.warning(self, "Error", "After reading file there are still empty rows")
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")
                    QMessageBox.warning(self, "Error", "Upload only text files")