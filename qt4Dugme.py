from PyQt4.QtGui import *
from PyQt4.QtCore import *

class ilkProgram(QDialog):
    def __init__(self,ebeveyn=None):
        super(ilkProgram,self).__init__(ebeveyn)

        self.boy = 3
        self.metin ='''<center><font color="blue" size="+%d">Message</font></center>'''
        self.etiket = QLabel(self.metin % self.boy)
        dugmeKucult = QPushButton('Shrink')
        self.connect(dugmeKucult , SIGNAL('pressed()'),self.metinKucult)
        dugmeBuyult = QPushButton('Enlarge')
        self.connect(dugmeBuyult , SIGNAL('pressed()'),self.metinBuyult)

        izgara = QGridLayout()
        izgara.addWidget(self.etiket,0,0,1,2)
        izgara.addWidget(dugmeKucult,1,0)
        izgara.addWidget(dugmeBuyult,1,1)

        self.setLayout(izgara)
        self.setWindowTitle('Window Title')
        self.resize(300,100)

    def metinBuyult(self):
        if self.boy <= 4:
            self.boy += 1
            self.etiket.setText(self.metin % self.boy)
            print(self.boy)

    def metinKucult(self):
        if self.boy >= 1:
            self.boy -= 1
            self.etiket.setText(self.metin % self.boy)
            print (self.boy)

uyg = QApplication([])
pencere = ilkProgram()
pencere.show()
uyg.exec_()