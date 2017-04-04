from PyQt4.QtGui import *
from PyQt4.QtCore import *


class kisayollar(QDialog):
    def __init__(self, ebeveyn=None):
        super(kisayollar, self).__init__(ebeveyn)

        self.boy=2
        self.metin = '''<div align="%s"><font size=+%d>Merhaba Dunya</font>'''
        self.hizalama = 'left'
        self.etiket = QLabel(self.metin % (self.hizalama, self.boy))

        izgara = QGridLayout()
        izgara.addWidget(self.etiket, 0, 0, 1, 3)

        boyEtiket = QLabel('&Yazi boyu:')
        izgara.addWidget(boyEtiket, 1, 0)
        self.donerKutu = QSpinBox()
        self.donerKutu.setRange(1, 4)
        self.donerKutu.setValue(self.boy)
        self.connect(self.donerKutu, SIGNAL('valueChanged(int)'), self.metinGuncelle)
        boyEtiket.setBuddy(self.donerKutu)
        izgara.addWidget(self.donerKutu, 1, 1, 1, 2)

        self.solDugme = QRadioButton('So&la Yasla')
        izgara.addWidget(self.solDugme, 2, 0)
        self.solDugme.setChecked(True)
        self.ortaDugme = QRadioButton('&Ortaya Yasla')
        izgara.addWidget(self.ortaDugme, 2, 1)
        self.sagDugme = QRadioButton('&Saga Yasla')
        izgara.addWidget(self.sagDugme, 2, 2)

        self.dugmeGrubu = QButtonGroup()
        self.dugmeGrubu.addButton(self.solDugme)
        self.dugmeGrubu.addButton(self.ortaDugme)
        self.dugmeGrubu.addButton(self.sagDugme)

        self.connect(self.dugmeGrubu, SIGNAL('buttonClicked(int)'), self.metinGuncelle)
        self.setLayout(izgara)
        self.setWindowTitle('PyQt Klavye Kisayollari')
        self.resize(250, 300)

    def metinGuncelle(self):
        self.boy = self.donerKutu.value()
        if self.solDugme.isChecked():
            self.hizalama = 'left'
        elif self.ortaDugme.isChecked():
            self.hizalama = 'center'
        else:
            self.hizalama = 'right'

        self.etiket.setText(self.metin % (self.hizalama, self.boy))

uyg = QApplication([])
pencere = kisayollar()
pencere.show()
uyg.exec_()
