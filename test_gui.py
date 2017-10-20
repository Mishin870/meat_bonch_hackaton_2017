# import speech_recognition as sr
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import (QWidget, QPushButton, QMessageBox, QTextEdit, QLineEdit, QDesktopWidget, QApplication)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

# from input_analys import *


class GUI_2(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    # def btn_click(self):
    #     with sr.Microphone() as source:
    #         self.editor.insertPlainText('Я вас слушаю\n')
    #         audio = r.listen(source)
    #     try:
    #         x = r.recognize_google(audio, language="ru-RU")
    #         self.line.insert(str(x))
    #     except sr.UnknownValueError:
    #         self.editor.insertPlainText('Я вас не поняла\n')
    #     except sr.RequestError as e:
    #         self.editor.insertPlainText("Ошибка сервиса; {0}".format(e))

    def initUI(self):
        # создание окна
        self.setGeometry(0, 0, 500, 600)
        self.center()
        self.setWindowTitle('Aika')

        # Выбор изображения ярлыка
        self.setWindowIcon(QIcon('web.png'))

        # Поле ввода
        self.line = QLineEdit(self)
        self.line.setGeometry(5, 5, 205, 25)
        self.line.setFont(QtGui.QFont("Courier New", 10))
        self.line2 = QLineEdit(self)
        self.line2.setGeometry(215, 5, 180, 25)
        self.line2.setFont(QtGui.QFont("Courier New", 10))
        # self.line.keyPressEvent(self)

        # кнопка голосового ввода
        self.btn = QPushButton('Звук', self)
        self.btn.move(400, 5)
        # self.btn.clicked.connect(self.btn_click)

        # Поле вывода
        self.editor = QTextEdit(self)
        self.editor.setGeometry(5, 35, 490, 550)
        # self.editor.setFont(QFont='Courier New')
        self.editor.setFont(QtGui.QFont("Courier New", 10))
        self.editor.setReadOnly(True)
        self.editor.insertPlainText('Словарь успешно подключен\n')

        self.show()

    # def set_editor(self, words='', param=''):
    #     words = obj_input.input(obj_input, words=words, param=param)
    #     self.editor.insertPlainText(words)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Return:
            buf1 = str(self.line.text())
            buf2 = str(self.line2.text())

            GUI_2.set_editor(self, buf1, buf2)
            self.line.clear()
            self.line2.clear()

    def closeEvent(self, event):

        self.setWindowIcon(QIcon('web2.png'))
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            self.setWindowIcon(QIcon('web.png'))
            event.ignore()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        buf = QDesktopWidget().availableGeometry()
        buf = str(buf)
        buf = buf.split(',')
        buf.pop(0)
        buf.pop(1)
        buf[0] = buf[0].lstrip(' ')
        buf[1] = buf[1].strip(' )')
        qr.moveCenter(cp)
        self.move(qr.topLeft())


# if __name__ == '__main__':
# r = sr.Recognizer()
app = QApplication(sys.argv)
ex = GUI_2()
sys.exit(app.exec_())
