from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #layout stuffs
        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        window.setCentralWidget(widget)

        # Qlabel
        label = QLabel("Weather App", self)
        label.setFont(QFont("Arial", 25, QFont.Bold))
        layout.addWidget(label, alignment=Qt.AlignTop)  # Set alignment for the label

        # ButtonOne
        buttonOne = QPushButton('Show the weather for XX/XX/XXXX', self)
        buttonOne.clicked.connect(self.buttonClicked)
        layout.addWidget(buttonOne, alignment=Qt.AlignCenter)

        # ButtonTwo
        buttonTwo = QPushButton('Show the weather for XX/XX/XXXX', self)
        buttonTwo.clicked.connect(self.buttonClicked)
        layout.addWidget(buttonTwo, alignment=Qt.AlignCenter)

        # ButtonThree
        buttonThree = QPushButton('Show the weather for XX/XX/XXXX', self)
        buttonThree.clicked.connect(self.buttonClicked)
        layout.addWidget(buttonThree, alignment=Qt.AlignCenter)

        # ButtonFour
        buttonFour = QPushButton('Show the weather for XX/XX/XXXX', self)
        buttonFour.clicked.connect(self.buttonClicked)
        layout.addWidget(buttonFour, alignment=Qt.AlignCenter)

        # ButtonFive
        buttonFive = QPushButton('Show the weather for XX/XX/XXXX', self)
        buttonFive.clicked.connect(self.buttonClicked)
        layout.addWidget(buttonFive, alignment=Qt.AlignCenter)

    def buttonClicked(self):
        print("ok")

if __name__ == '__main__':
    app = QApplication([])
    window = QMainWindow()
    ex = Example()

    window.setFixedSize(1000, 1000)
    window.show()
    app.exec_()
