from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget

# How to create a button
# Button Class
class UiStuffs(QWidget):
    # constructor is below
    def __init__(self):
        # calls the constructor of the inherited Qwidget class
        super().__init__()
        # tells pyqt5 that im boutta do some ui stuff
        self.initUI()
    # Initializes the user interface
    def initUI(self):
        layout = QVBoxLayout()

        # Creating a QlistWidget
        list_widget = QListWidget(self)
        list_widget.addItem("Item 1")
        list_widget.addItem("Item 2")
        list_widget.addItem("Item 3")
        layout.addWidget(list_widget)

        # Create a Qlabel
        label = QLabel("This is a label", self)
        layout.addWidget(label)

        # Creating a QPushButton
        button = QPushButton('Click me', self) # makes a button object and stores it in the button variable, the string is the text that is shown on the button
        button.clicked.connect(self.buttonClicked) # When the button is clicked it calls the buttonClicked function
        button.move(50, 50) # moves the button to x:50 y:50
        
        self.setLayout(layout)
        self.show() # shows the button object

    # This is the function that is called when the button object is clicked
    def buttonClicked(self):
        # code here
        print('Button clicked')

# The if statement checks if the script this is being run in is the main script
if __name__ == '__main__':
    app = QApplication([]) # creates an instance of Qapplication which manages the GUI application
    ex = UiStuffs() # This line creates an instance of the Example class, which represents the main window of the application.
    app.exec_() # This line starts the main event loop of the application, which waits for events (such as button clicks) and handles them.
