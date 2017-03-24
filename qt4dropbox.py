from PyQt4.QtGui import *
from PyQt4.QtCore import *

class dropbox(QDialog):
    def __init__(self,ebeveyn=None):
        super(dropbox, self).__init__(ebeveyn)

        self.boy=2
        self.yaziTipi='Century'
        self.metin = '''<center><font color="blue" size="+%d" face="%s">Hello World</font></center>'''
        self.etiket = QLabel(self.metin % (self.boy,self.yaziTipi))

        izgara = QGridLayout()
        izgara.addWidget(self.etiket , 0,0,1,2)
        izgara.addWidget(QLabel('Yazi Boyu: '),1,0)

        donerKutu = QSpinBox()
        donerKutu.setRange(1,4)
        donerKutu.setValue(self.boy)
        self.connect(donerKutu,
                     SIGNAL('valueChanged(int)'),
                     self.metinBoyuDegistir)
        izgara.addWidget(donerKutu,1,1)
        izgara.addWidget(QLabel('Yazi Tipi: '),2,0)

        acilirListe = QComboBox()
        acilirListe.addItem('Cantarell')
        acilirListe.addItem('Century')
        acilirListe.addItem('DejaVu , Bold')

        listeIndis=acilirListe.findText(self.yaziTipi)
        acilirListe.setCurrentIndex(listeIndis)
        self.connect(acilirListe,
                     SIGNAL('currentIndexChanged(QString)'),
                     self.yaziTipiDegistir)
        izgara.addWidget(acilirListe , 2 , 1)

        self.setLayout(izgara)
        self.setWindowTitle('PyQt Izgara Sistemi')
        self.resize(250,150)

    def metinBoyuDegistir(self,boy):
            self.boy=boy
            self.etiket.setText(self.metin % (self.boy , self.yaziTipi))

    def yaziTipiDegistir(self,yaziTipi):
        self.yaziTipi=yaziTipi
        self.etiket.setText(self.metin % (self.boy , self.yaziTipi))

uyg = QApplication([])
pencere = dropbox()
pencere.show()
uyg.exec_()