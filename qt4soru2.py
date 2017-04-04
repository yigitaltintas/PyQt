from PyQt4.QtGui import *
from PyQt4.QtCore import *


class myBody(QDialog):
    def __init__(self, ebeveyn=None):
        super(myBody, self).__init__(ebeveyn)

        grid = QGridLayout()
        grid.addWidget(QLabel('Kg'), 0, 0)
        self.kilograms = QLineEdit()
        self.kilograms.setInputMask('00')
        grid.addWidget(self.kilograms, 0, 1)

        grid.addWidget(QLabel('Height'), 1, 0)
        self.height = QLineEdit()
        self.height.setInputMask('000')
        grid.addWidget(self.height, 1, 1)

        self.result = QLabel()
        grid.addWidget(self.result, 2, 1, 1, 2)

        self.connect(self.kilograms, SIGNAL('textChanged(QString)'), self.findBody)
        self.connect(self.height, SIGNAL('textChanged(QString)'), self.findBody)

        self.setLayout(grid)
        self.setWindowTitle('My Body')

    def findBody(self):
        kilo = 0
        try: kilo = int(self.kilograms.text())
        except: pass
        boy = 0
        try: boy = int(self.height.text())
        except: pass

        if not kilo:
            self.result.setText('Please write your kilograms')
        elif not boy:
            self.result.setText('Please write your height')
        else:
            ok = kilo * boy
            ok *=bo
            self.result.setText('%f' % ok)


myApp = QApplication([])
window = myBody()
window.show()
myApp.exec_()
