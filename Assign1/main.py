#-*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from PyQt5 import uic
from functools import partial

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = uic.loadUi("basic.ui")
        self.initButtons()
        self.ui.show()

    def initButtons(self):
        """ initButtons -- 버튼마다 시그널/슬롯 설정 """
        InputButtons = [(self.ui.Button0,'0'), (self.ui.Button1,'1'),
                        (self.ui.Button2,'2'), (self.ui.Button3,'3'),
                        (self.ui.Button4,'4'), (self.ui.Button5,'5'),
                        (self.ui.Button6,'6'), (self.ui.Button7,'7'),
                        (self.ui.Button8,'8'), (self.ui.Button9,'9'),
                        (self.ui.plusButton,'+'), (self.ui.minusButton,'-'),
                        (self.ui.multButton,'*'), (self.ui.divButton,'/')]
        for button, symbol in InputButtons:
            button.clicked.connect(
                lambda v, x=symbol: self.ui.formula.setText(
                    self.ui.formula.text() + x))
        
        evalButton = self.ui.evalButton
        evalButton.clicked.connect(
            lambda v: self.ui.result.setText(
                str(eval(self.ui.formula.text()))))
        
        clearButton = self.ui.clearButton
        clearButton.clicked.connect(
            lambda v: self.ui.formula.setText(""))
        
        backButton = self.ui.backButton
        backButton.clicked.connect(
            lambda v: self.ui.formula.setText(
                self.ui.formula.text()[:-1]))

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec())
