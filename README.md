# AMO Lab works
This repository for my lab works, but I also try to use here interesting features, for example Drag'n'Drop.

# Key Components

## 1. Drag and Drop File Handling:

* The `DnDMixin` class and `DnDQTextEdit` subclass provide functionality to drag and drop files for easy data input.
* The `UploadFileButton` class facilitates file upload with error handling for unsupported file types or empty rows.
## 2. Signals

* Actively using `pyqtSignal` for updating plots for new data


# Installing
Use pyinstaller for generating .exe files or run `window.py`
```
pip install requirements.txt
python <path>/window.py
```
Generate onefile executable
```
pyinstaller --onefile --windowed --name=<name> --add-data="<Folder>/*.py;." --hidden-import="mimetypes" --hidden-import="pyqt5" --hidden-import="numpy" --hidden-import="matplotlib" --hidden-import="scipy" --hidden-import="scipy.interpolate" <Folder>/window.py
```
