from PyQt5.QtWidgets import QApplication, QPushButton, QWidget

# How to create a button
# Button Class
class Button(QWidget):
    # constructor is below
    def __init__(self):
        # calls parent constructor
        super().__init__()
        # tells pyqt5 that im boutta do some ui stuff
        self.initUI()
    # Creates the button
    def initUI(self):
        button = QPushButton('Click me', self) # makes a button object and stores it in the button variable, the string is the text that is shown on the button
        button.clicked.connect(self.buttonClicked) # When the button is clicked it calls the buttonClicked function
        button.move(50, 50) # moves the button to x:50 y:50
        
        self.show() # shows the button object

    # This is the function that is called when the button object is clicked
    def buttonClicked(self):
        # code here
        print('Button clicked')

if __name__ == '__main__':
    app = QApplication([])
    ex = Button()
    app.exec_()
