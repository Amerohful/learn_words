import sys
from PyQt5.QtCore import Qt, QTimer, QEventLoop
from PyQt5.QtWidgets import (QLabel, QAction, qApp, QHBoxLayout, QVBoxLayout,
                             QInputDialog, QPushButton, QMainWindow, QApplication,
                             QLineEdit, QWidget, QMessageBox)
from ArrWords import ListWords, Word

class Window(QMainWindow):

    List = ... # type: ListWords
    SIZE = 0
    ITER = 0

    def __init__(self):
        super().__init__()
        self.form_widjet = FormWidjet()
        self.setCentralWidget(self.form_widjet)

        self.initUI()


    def initUI(self):
        exitAction = QAction('&Exit', self)
        exitAction.triggered.connect(qApp.quit)

        openAction = QAction('&Open', self)
        openAction.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(openAction)
        filemenu.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Learn Words')
        self.show()


    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Open file', 'Enter path:')
        if ok:
            try:
                self.List = ListWords(str(text))
                self.form_widjet.word.setText(self.List.L[self.ITER].word)
                self.SIZE = len(self.List.L)
            except:
                QMessageBox.about(self, "Error path", "Нет такого файла или каталога(")
                self.showDialog()


    def keyPressEvent(self, QKeyEvent):
        try:
            if QKeyEvent.key() == Qt.Key_Enter \
                    or QKeyEvent.key() == Qt.Key_Return:

                if self.ITER + 1 < self.SIZE:
                    self.checkAnswer()
                    self.setWord()
                else:
                    self.checkAnswer()
                    self.List.sortWords()
                    self.ITER = 0
                    self.SIZE = len(self.List.L)
                    self.setWord()
        except:
            pass

    def checkAnswer(self):
        if not self.List.L[self.ITER].checkTranslate(str(self.form_widjet.line.text())):
            self.form_widjet.result.setText(self.List.L[self.ITER].translate)
            loop = QEventLoop()
            QTimer.singleShot(1500, lambda: loop.quit())
            loop.exec_()
        self.form_widjet.result.setText('')
        self.form_widjet.line.setText('')


    def setWord(self):
        self.ITER += 1
        try:
            self.form_widjet.word.setText(self.List.L[self.ITER].word)
        except:
            QMessageBox.about(self, "Grats", "Список слов закончился, выберите новый)")
            self.form_widjet.word.setText('')



class FormWidjet(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        mainbox = QVBoxLayout()
        self.setLayout(mainbox)

        mainbox.addStretch(0.2)

        wordbox = QVBoxLayout()

        self.word = QLabel()
        self.line = QLineEdit()
        self.result = QLabel()

        wordbox.addWidget(self.word)
        wordbox.addWidget(self.line)
        wordbox.addWidget(self.result)

        midbox = QHBoxLayout()
        midbox.addStretch(0.3)
        midbox.addLayout(wordbox)
        midbox.addStretch(0.3)

        mainbox.addLayout(midbox)
        mainbox.addStretch(0.2)



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())