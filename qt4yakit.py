from PyQt4.QtGui import *
from PyQt4.QtCore import *

class yakitHesaplayicisi(QDialog):
    def __init__(self,ebeveyn=None):
        super(yakitHesaplayicisi,self).__init__(ebeveyn)

        grid=QGridLayout()
        grid.addWidget(QLabel('Gideceginiz Yol(KM): '),0,0)
        self.gidilenYol=QLineEdit()
        self.gidilenYol.setInputMask('0000000')
        grid.addWidget(self.gidilenYol,0,1)

        grid.addWidget(QLabel('Fiyat'),1,0)
        self.yakitFiyati=QLineEdit()
        self.yakitFiyati.setInputMask('0.00')
        grid.addWidget(self.yakitFiyati,1,1)

        grid.addWidget(QLabel('100 KM de tuketilen yakit :'),2,0)
        self.yakitTuketimi = QLineEdit()
        self.yakitTuketimi.setInputMask('00.0')
        grid.addWidget(self.yakitTuketimi,2,1)

        grid.addWidget(QLabel('Toplam TUtar : '),3,0)
        self.tutar=QLabel('KM giriniz')
        grid.addWidget(self.tutar,3,1)

        hesaplaDugme=QPushButton('Hesapla')
        self.connect(hesaplaDugme,SIGNAL('pressed()'),self.yakitHesapla)
        grid.addWidget(hesaplaDugme,4,0,1,2)

        self.setLayout(grid)
        self.setWindowTitle('Yakit Hesapla')

    def yakitHesapla(self):
        yol=0
        try: yol=int(self.gidilenYol.text())
        except: pass
        fiyat=0
        try: fiyat=float(self.yakitFiyati.text())
        except: pass
        tuketim=0
        try: tuketim=float(self.yakitTuketimi.text())
        except: pass

        if not yol:
            self.tutar.setText('KM Giriniz')
            self.gidilenYol.setFocus()
        elif not fiyat:
            self.tutar.setText('Fiyat Giriniz')
            self.yakitFiyati.setFocus()
        elif not tuketim:
            self.tutar.setText('Tuketim Miktarini Giriniz')
            self.yakitTuketimi.setFocus()
        else:
            tutar=fiyat*(yol*tuketim)/100
            self.tutar.setText('%0.2f' % tutar)

uyg=QApplication([])
pencere=yakitHesaplayicisi()
pencere.show()
uyg.exec_()