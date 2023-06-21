from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget
from PyQt5.QtGui import QFont

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # layout
        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        window.setCentralWidget(widget)
        # buttonOne
        buttonOne = QPushButton('XX/XX/XXXX', self)
        buttonOne.clicked.connect(self.buttonClicked)
        buttonOne.setGeometry(50,100,100,50)
        buttonOne.move(50,50)
        layout.addWidget(buttonOne)

        # buttonTwo
        buttonTwo = QPushButton('XX/XX/XXXX', self)
        buttonTwo.clicked.connect(self.buttonClicked)
        buttonTwo.move(100, 150)
        buttonTwo.setGeometry(50,100,100,50)
        layout.addWidget(buttonTwo)

        # buttonThree
        buttonThree = QPushButton('XX/XX/XXXX', self)
        buttonThree.clicked.connect(self.buttonClicked)
        buttonThree.setGeometry(50,100,100,50)
        buttonThree.move(150, 100)
        layout.addWidget(buttonThree)

        # buttonFour
        buttonFour = QPushButton('XX/XX/XXXX', self)
        buttonFour.clicked.connect(self.buttonClicked)
        buttonFour.setGeometry(50,100,100,50)
        buttonFour.move(150, 100)
        layout.addWidget(buttonFour)

        # buttonFive
        buttonFive = QPushButton('XX/XX/XXXX', self)
        buttonFive.clicked.connect(self.buttonClicked)
        buttonFive.setGeometry(50,100,100,50)
        buttonFive.move(150, 100)
        layout.addWidget(buttonFive)

        # label
        label = QLabel("Weather App",self)
        label.move(0,0)
        label.setFont(QFont("Arial",25, QFont.Bold))
        layout.addWidget(label)


    def buttonClicked(self):
        print('Button clicked')

    

if __name__ == '__main__':
    app = QApplication([])
    window = QMainWindow()
    ex = Example()
    
    window.setFixedSize(1000,1000)
    window.show()
    app.exec_()
