import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt


class MyWidget(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.black)
        painter.setBrush(QColor(255, 0, 0))
        painter.drawRect(50, 50, 100, 100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.setGeometry(100, 100, 200, 200)
    window.show()
    sys.exit(app.exec_())
