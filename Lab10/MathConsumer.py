# Import PySide classes
import sys

from PySide.QtCore import *
from PySide.QtGui import *

from calculator import *

class MathConsumer(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MathConsumer, self).__init__(parent)
        self.setupUi(self)
        
        # Calculate must perform the operation
        self.btnCalculate.clicked.connect(self.performOperation)
    
    def performOperation(self):
        # If either of the text boxes is empty
        if self.edtNumber1.text() == "" or self.edtNumber2.text() == "":
            self.edtResult.setText("E")
        
        try:
            float(self.edtNumber1.text())
            float(self.edtNumber2.text())
        except:
            # or does not contain a valid number (float or integer)
            self.edtResult.setText("E")
        else:
            if self.cboOperation.itemText(self.cboOperation.currentIndex()) == "+":
                self.edtResult.setText(str(float(self.edtNumber1.text()) + float(self.edtNumber2.text())))
            elif self.cboOperation.itemText(self.cboOperation.currentIndex()) == "-":
                self.edtResult.setText(str(float(self.edtNumber1.text()) - float(self.edtNumber2.text())))
            elif self.cboOperation.itemText(self.cboOperation.currentIndex()) == "*":
                self.edtResult.setText(str(float(self.edtNumber1.text()) * float(self.edtNumber2.text())))
            elif self.cboOperation.itemText(self.cboOperation.currentIndex()) == "/":
                if float(self.edtNumber2.text()) == 0:
                    self.edtResult.setText("E")
                else:
                    self.edtResult.setText(str(float(self.edtNumber1.text()) / float(self.edtNumber2.text())))

if __name__ == "__main__":
     currentApp = QApplication(sys.argv)
     currentForm = MathConsumer()
     
     currentForm.show()
     currentApp.exec_()
