import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

def on_button_click():
    print("Button clicked!")

if __name__ == '__main__':
    # Create the application object
    app = QApplication(sys.argv)

    # Create a window
    window = QWidget()
    window.setWindowTitle('PyQt5 Example')
    window.setGeometry(100, 100, 300, 200)  # Set the window size and position

    # Create a button
    button = QPushButton('Click me', window)
    button.setGeometry(100, 50, 100, 50)  # Set the button size and position

    # Connect the button's clicked signal to a custom slot
    button.clicked.connect(on_button_click)

    # Show the window
    window.show()

    # Start the event loop
    sys.exit(app.exec_())
