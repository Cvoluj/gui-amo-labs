# AMO Lab works
This repository for my lab works, but I also try to use here best practices and features, like Drag'n'Drop, etc.

**UPD:** in small amount of free time this labs can look little scary**

# Installing
Download .exe or do it by your own
```
pip install requirements.txt
python <path>/window.py
```
Generate onefile executable
```
pyinstaller --onefile --windowed --name=<name> --add-data="<Folder>/*.py;." --hidden-import="mimetypes" --hidden-import="pyqt5" --hidden-import="numpy" --hidden-import="matplotlib" --hidden-import="scipy" --hidden-import="scipy.interpolate" <Folder>/window.py
```
