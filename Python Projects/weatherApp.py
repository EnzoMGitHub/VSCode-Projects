from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

app = QApplication([])
window = QMainWindow()
layout = QVBoxLayout()
widget = QWidget()
widget.setLayout(layout)
window.setCentralWidget(widget)

def buttonOneClicked():
    print("1")

def buttonTwoClicked():
    print("2")

def buttonThreeClicked():
    print("3")

def buttonFourClicked():
    print("4")

def buttonFiveClicked():
    print("5")

# Qlabel
label = QLabel("Weather App")
label.setFont(QFont("Arial", 25, QFont.Bold))
layout.addWidget(label, alignment=Qt.AlignTop)  # Set alignment for the label

# ButtonOne
buttonOne = QPushButton('Show the weather for XX/XX/XXXX')
buttonOne.clicked.connect(buttonOneClicked)
buttonOne.setFixedSize(900,100)
layout.addWidget(buttonOne, alignment=Qt.AlignCenter)

# ButtonTwo
buttonTwo = QPushButton('Show the weather for XX/XX/XXXX')
buttonTwo.clicked.connect(buttonTwoClicked)
buttonTwo.setFixedSize(900,100)
layout.addWidget(buttonTwo, alignment=Qt.AlignCenter)

# ButtonThree
buttonThree = QPushButton('Show the weather for XX/XX/XXXX')
buttonThree.clicked.connect(buttonThreeClicked)
buttonThree.setFixedSize(900,100)
layout.addWidget(buttonThree, alignment=Qt.AlignCenter)

# ButtonFour
buttonFour = QPushButton('Show the weather for XX/XX/XXXX')
buttonFour.clicked.connect(buttonFourClicked)
buttonFour.setFixedSize(900,100)
layout.addWidget(buttonFour, alignment=Qt.AlignCenter)

# ButtonFive
buttonFive = QPushButton('Show the weather for XX/XX/XXXX')
buttonFive.clicked.connect(buttonFiveClicked)
buttonFive.setFixedSize(900,100)
layout.addWidget(buttonFive, alignment=Qt.AlignCenter)




window.setFixedSize(1000, 1000)
window.show()
app.exec_()