from PyQt5.QtWidgets import QApplication, QPushButton, QWidget

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        button = QPushButton('Click me', self)
        button.clicked.connect(self.buttonClicked)
        button.move(50, 50)
        
        self.show()

    def buttonClicked(self):
        print('Button clicked')

if __name__ == '__main__':
    app = QApplication([])
    ex = Example()
    app.exec_()
