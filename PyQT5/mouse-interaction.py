import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QPointF


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.points = []

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.black)
        painter.setBrush(QColor(255, 0, 0))
        for point in self.points:
            painter.drawEllipse(point, 5, 5)

    def mousePressEvent(self, event):
        self.points.append(event.pos())
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.setGeometry(100, 100, 400, 300)
    window.show()
    sys.exit(app.exec_())

