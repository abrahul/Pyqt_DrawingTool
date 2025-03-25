import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene

class SimpleDrawingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic Drawing Tool")
        self.setGeometry(100, 100, 800, 600)

        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.setCentralWidget(self.view)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleDrawingApp()
    window.show()
    sys.exit(app.exec_())
