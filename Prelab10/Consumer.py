import sys
import re

from PySide.QtGui import *
from BasicUI import *

class Consumer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(Consumer, self).__init__(parent)
        self.setupUi(self)
        
        # Organize box contents for iteration
        self.studentInfo = [self.txtStudentName, self.txtStudentID]
        self.componentNames = [self.txtComponentName_1, self.txtComponentName_2, self.txtComponentName_3,
                            self.txtComponentName_4, self.txtComponentName_5, self.txtComponentName_6,
                            self.txtComponentName_7, self.txtComponentName_8, self.txtComponentName_9,
                            self.txtComponentName_10, self.txtComponentName_11, self.txtComponentName_12,
                            self.txtComponentName_13, self.txtComponentName_14, self.txtComponentName_15,
                            self.txtComponentName_16, self.txtComponentName_17, self.txtComponentName_18,
                            self.txtComponentName_19, self.txtComponentName_20]
        self.componentCounts = [self.txtComponentCount_1, self.txtComponentCount_2, self.txtComponentCount_3,
                            self.txtComponentCount_4, self.txtComponentCount_5, self.txtComponentCount_6,
                            self.txtComponentCount_7, self.txtComponentCount_8, self.txtComponentCount_9,
                            self.txtComponentCount_10, self.txtComponentCount_11, self.txtComponentCount_12,
                            self.txtComponentCount_13, self.txtComponentCount_14, self.txtComponentCount_15,
                            self.txtComponentCount_16, self.txtComponentCount_17, self.txtComponentCount_18,
                            self.txtComponentCount_19, self.txtComponentCount_20]

        # 'Save' button disabled in 'Initial State'
        self.btnSave.setEnabled(False)

        # Clear must reset the form to the initial state
        self.btnClear.clicked.connect(self.reset)

        # The moment you start modifying any data entry widget (Save -> enabled, Load -> disabled)
        # text boxes
        for info in self.studentInfo:
            info.textChanged.connect(self.saveOloadX)
        for componentName in self.componentNames:
            componentName.textChanged.connect(self.saveOloadX)
        for componentCount in self.componentCounts:
            componentCount.textChanged.connect(self.saveOloadX)
        # check box
        self.cboCollege.currentIndexChanged.connect(self.saveOloadX)
        # combo box
        self.chkGraduate.stateChanged.connect(self.saveOloadX)
        
        # Save must save an XML file
        self.btnSave.clicked.connect(self.saveData)

        # Load must load an XML file
        self.btnLoad.clicked.connect(self.loadData)

    def reset(self):
        # reset text boxes
        for info in self.studentInfo:
            info.clear()
        for componentName in self.componentNames:
            componentName.clear()
        for componentCount in self.componentCounts:
            componentCount.clear()
        # reset check box
        self.cboCollege.setCurrentIndex(0)
        # reset combo box
        self.chkGraduate.setChecked(False)
        # enable Load button
        self.btnLoad.setEnabled(True)
        # disable Save button
        self.btnSave.setEnabled(False)

    def saveOloadX(self):
        self.btnSave.setEnabled(True)
        self.btnLoad.setEnabled(False)
    
    def saveData(self):
        with open('target.xml', 'w') as myFile:
            myFile.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            myFile.write('<Content>\n')
            if self.chkGraduate.isChecked() == True:
                myFile.write('    <StudentName graduate="true">')
            elif self.chkGraduate.isChecked() == False:
                myFile.write('    <StudentName graduate="false">')
            myFile.write(self.txtStudentName.text() + '</StudentName>\n')
            myFile.write('    <StudentID>' + self.txtStudentID.text() + '</StudentID>\n')
            myFile.write('    <College>' + self.cboCollege.itemText(self.cboCollege.currentIndex()) + '</College>\n')
            myFile.write('    <Components>\n')
            for i in range(20):
                if len(self.componentNames[i].text()) != 0 and len(self.componentCounts[i].text()) != 0:
                    myFile.write('        <Component name="' + self.componentNames[i].text() + '" count="' + self.componentCounts[i].text() + '" />\n')
            myFile.write('    </Components>\n')
            myFile.write('</Content>')

    def loadDataFromFile(self, filePath):
        """
        Handles the loading of the data from the given file name. This method will be invoked by the 'loadData' method.
        
        *** YOU MUST USE THIS METHOD TO LOAD DATA FILES. ***
        *** This method is required for unit tests! ***
        """
        cmpi = 0
        with open(filePath, 'r') as myFile:
            all_lines = myFile.readlines()
            for line in all_lines:
                line = line.strip()
                capture = re.search(r'<StudentName graduate="(?P<chk>(.*))">(?P<name>(.*))</StudentName>', line)
                if capture != None:
                    if capture.group('chk') == 'true':
                        self.chkGraduate.setChecked(True)
                    elif capture.group('chk') == 'false':
                        self.chkGraduate.setChecked(False)
                    self.txtStudentName.setText(capture.group('name'))
                capture = re.search(r'<StudentID>(?P<id>(.*))</StudentID>', line)
                if capture != None:
                    self.txtStudentID.setText(capture.group('id'))
                capture = re.search(r'<College>(?P<col>(.*))</College>', line)
                if capture != None:
                    loc = self.cboCollege.findText(capture.group('col'))
                    self.cboCollege.setCurrentIndex(loc)
                capture = re.search(r'<Component name="(?P<cmpname>(.*))" count="(?P<cmpcnt>(.*))" />', line)
                if capture != None:
                    if cmpi >= 20:
                        pass
                    else:
                        self.componentNames[cmpi].setText(capture.group('cmpname'))
                        self.componentCounts[cmpi].setText(capture.group('cmpcnt'))
                        cmpi = cmpi + 1

        # disable the Load button and enable the Save button (Ready-to-Save state)
        self.btnLoad.setEnabled(False)
        self.btnSave.setEnabled(True)

    def loadData(self):
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadDataFromFile(filePath)


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()
