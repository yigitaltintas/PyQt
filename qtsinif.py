from PyQt4.QtGui import *
from PyQt4.QtCore import *

class ilkProgram(QDialog):
    def __init__(self, ebeveyn=None):
        super(ilkProgram, self).__init__(ebeveyn)
        self.etiket=QLabel('<font color="blue" size=" +3">Merhaba</font>')
        dugme = QPushButton('Tikla')
        self.connect(dugme , SIGNAL('pressed()'),self.metinGuncelle)
        kutu = QHBoxLayout()
        kutu.addWidget(self.etiket)
        kutu.addWidget(dugme)

        self.setLayout(kutu)
        self.resize(300 , 400)
        self.move(250,50)
        self.setWindowTitle('Test')

    def metinGuncelle(self):
        self.etiket.setText('<font color="blue" size="+3">Dugmeye Basildi</font>')

uyg=QApplication([])
pencere = ilkProgram()
pencere.show()
uyg.exec_()