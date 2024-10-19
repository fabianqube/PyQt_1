from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
import random

#подключение библиотек

#создание элементов интерфейса
app = QApplication([])
#привязка элементов к вертикальной линии
window = QWidget()
window.resize(400,200)
window.setWindowTitle('Генератор победителя')
text = QLabel('Нажми, чтобы узнать победителя')
q_mark = QLabel('?')
button = QPushButton('Сгенерировать')
#обработка событий
main_line = QVBoxLayout()
main_line.addWidget(text, alignment = Qt.AlignCenter)
main_line.addWidget(q_mark, alignment = Qt.AlignCenter)
main_line.addWidget(button, alignment = Qt.AlignCenter)
window.setLayout(main_line)

def show_winner():
    text.setText('Победитель:')
    num = random.randint(1,100)
    q_mark.setText(str(num))
button.clicked.connect(show_winner)
#запуск приложения
window.show()
app.exec_()