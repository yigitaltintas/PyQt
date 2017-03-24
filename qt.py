from PyQt4.QtGui import *
from PyQt4.QtCore import *

def click():
    a.setText('test')

uyg=QApplication([])

pencere=QWidget()
a=QLabel('<b>Merhaba</b>')
dugme=QPushButton('Click')
pencere.connect(dugme, SIGNAL('pressed()'), click)
kutu = QHBoxLayout()

kutu.addWidget(a)
kutu.addWidget(dugme)


pencere.setLayout(kutu)
pencere.setWindowTitle('Test')
pencere.show()
uyg.exec_()