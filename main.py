import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QGraphicsEllipseItem
from PyQt5.QtCore import Qt

class DrawingScene(QGraphicsScene):
    def __init__(self):
        super().__init__()
        self.mode = "rectangle"  # Default mode to draw rectangles

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            pos = event.scenePos()
            if self.mode == "rectangle":
                rect = QGraphicsRectItem(pos.x(), pos.y(), 100, 50)
                rect.setBrush(Qt.yellow)
                self.addItem(rect)
            elif self.mode == "ellipse":
                ellipse = QGraphicsEllipseItem(pos.x(), pos.y(), 100, 50)
                ellipse.setBrush(Qt.green)
                self.addItem(ellipse)
        super().mousePressEvent(event)

class SimpleDrawingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic Drawing Tool")
        self.setGeometry(100, 100, 800, 600)
        self.scene = DrawingScene()
        self.view = QGraphicsView(self.scene)
        self.setCentralWidget(self.view)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleDrawingApp()
    window.show()
    sys.exit(app.exec_())
