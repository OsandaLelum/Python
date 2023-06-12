import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # Create the application object
    app = QApplication(sys.argv)

    # Create a window
    window = QWidget()
    window.setWindowTitle('PyQT5 Example')
    window.setGeometry(100, 100, 300, 200)  # Set the window size and position

    # Show the window
    window.show()

    # Start the event loop
    sys.exit(app.exec_())
