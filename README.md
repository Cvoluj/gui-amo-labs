# AMO Lab works
This repository for my lab works, but I also try to use here best practices and features, like Drag'n'Drop, etc.

# Installing
Download .exe or do it by your own
```
pip install requirements.txt
python <path>/window.py
```
Generate onefile executable
```
pyinstaller --onefile --windowed --name=lab1 --add-data="Lab1/*.py;." --hidden-import="mimetypes" --hidden-import="pyqt5" Lab1/window.py
```
