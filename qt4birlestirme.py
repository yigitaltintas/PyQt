from PyQt4.QtGui import *
from PyQt4.QtCore import *
import time

class birlesik(QDialog):
    def __init__(self, ebeveyn=None):
        super(birlesik, self).__init__(ebeveyn)

        grid = QGridLayout()
        surgu = QSlider()
        surgu.setRange(0, 100)
        surgu.setOrientation(Qt.Horizontal)
        grid.addWidget(surgu, 0, 0)

        dkutu = QSpinBox()
        dkutu.setRange(0, 100)
        grid.addWidget(dkutu, 1, 0)

        self.connect(surgu, SIGNAL('valueChanged(int)'), dkutu.setValue)
        self.connect(dkutu, SIGNAL('valueChanged(int)'), surgu.setValue)

        self.setLayout(grid)
        self.setWindowTitle('Nesneleri Birlestirme')

uyg = QApplication([])
pencere = birlesik()
pencere.show()
uyg.exec_()