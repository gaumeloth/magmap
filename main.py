#!/home/guido_d/github/mapper/venv/bin/python3.11
import sys
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QMainWindow, QGraphicsEllipseItem
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QPointF

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Mappa del Magazzino')

        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene, self)
        self.setCentralWidget(self.view)

        # Carica l'immagine della mappa (assumendo che il file si chiami 'mappa.png')
        pixmap = QPixmap('mappa.png')
        self.map_image = self.scene.addPixmap(pixmap)

        # Aggiungi un segnaposto come esempio
        self.add_marker(100, 100)

    def add_marker(self, x, y):
        marker = QGraphicsEllipseItem(x - 10, y - 10, 20, 20)
        marker.setBrush(Qt.red)
        self.scene.addItem(marker)
        marker.setFlag(QGraphicsEllipseItem.ItemIsMovable)
        marker.setFlag(QGraphicsEllipseItem.ItemIsSelectable)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

