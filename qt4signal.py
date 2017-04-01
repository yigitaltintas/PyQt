from PyQt4.QtGui import *
from PyQt4.QtCore import *
import time

class signal(QDialog):
    def __init__(self, ebeveyn=None):
        super(signal, self).__init__(ebeveyn)

        grid = QGridLayout()
        surgu = QSlider()
        surgu.setRange(0, 100)
        surgu.setOrientation(Qt.Horizontal)
        grid.addWidget(surgu, 0, 0)

        dKutu = QSpinBox()
        dKutu.setRange(0, 100)
        grid.addWidget(dKutu, 1, 0)

        self.connect(dKutu, SIGNAL('valueChanged(int)'), surgu.setValue)
        self.connect(surgu, SIGNAL('valueChanged(int)'), dKutu.setValue)

        self.setLayout(grid)
        self.setWindowTitle('Signal Slot')

uyg = QApplication([])
win = signal()
win.show()
uyg.exec_()