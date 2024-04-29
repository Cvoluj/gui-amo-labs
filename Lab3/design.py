DESIGN_QSS = """
QDialog {
    background-color: #ffffff; /* Зміна кольору фону на білий */
    border: 1px solid #e0e0e0; /* Зміна кольору рамки на білий відтінок */
    border-radius: 10px; /* Округлення кутів */
}

QWidget {
    background-color: #ffffff; /* Зміна кольору фону на білий */
    color: #333333; /* Зміна кольору тексту на темно-сірий */
    font-family: 'Segoe UI', sans-serif; 
}

QTextEdit {
    background-color: #f8f8f8; /* Повернення колір вікна редагування на вихідний */
    border: 2px solid #e0e0e0; /* Зміна кольору рамки на білий відтінок */
    padding: 8px;
    font-size: 18px; /* Збільшення розміру шрифту */
    border-radius: 5px;
}

QLabel {
    font-weight: bold;
    color: #666666; /* Зміна кольору тексту на темно-сірий */
    font-size: 16px;
}

QListWidget {
    border: 2px solid #e0e0e0; /* Зміна кольору рамки на білий відтінок */
    padding: 8px;
    font-size: 18px; /* Збільшення розміру шрифту */
    border-radius: 5px;
}

QListWidget::item {
    padding: 4px;
}

QPushButton {
    background-color: #4CAF50;
    color: white;
    border: none;
    padding: 10px 16px; /* Збільшення розміру кнопки */
    text-align: center;
    text-decoration: none;
    font-size: 14px; /* Збільшення розміру шрифту */
    margin: 4px 2px;
    border-radius: 4px;
}

QPushButton:hover {
    background-color: #45a049; /* Зміна кольору фону при наведенні курсору */
}
QLineEdit {
    font-size: 16px;
}

#StudentInfo {
    background-color: #f0f0f0; /* Light grey background */
    color: #333333; /* Dark grey text */
    font-family: 'Times New Roman', sans-serif;
    border: 1px solid #cccccc; /* Light grey border */
    border-radius: 10px; /* Rounded corners */
    padding: 20px; /* Add some padding */
}

#StudentInfo QLabel {
    font-size: 19px; /* Smaller font size */
    font-weight: bold; /* Bold font */
    color: #555555; /* Dark grey text */
    margin-bottom: 5px; /* Reduced bottom margin */
}

#StudentInfo QLabel#titleLabel {
    font-size: 24px; /* Larger title font size */
    color: #336699; /* Dark blue title */
}    
QTabWidget {
    background-color: #ffffff; /* Background color */
    color: #333333; /* Text color */
    font-size: 16px; /* Font size */
    font-family: 'Segoe UI', sans-serif; /* Font family */
}

QTabBar::tab {
    background-color: #f0f0f0; /* Background color of the tab */
    color: #555555; /* Text color of the tab */
    border: 1px solid #cccccc; /* Border color of the tab */
    padding: 8px 16px; /* Padding of the tab */
    margin-right: 2px; /* Margin between tabs */
}

QTabBar::tab:selected {
    background-color: #ffffff; /* Background color of the selected tab */
    color: #336699; /* Text color of the selected tab */
    border-bottom: 1px solid #ffffff; /* Hide bottom border of the selected tab */
}
"""