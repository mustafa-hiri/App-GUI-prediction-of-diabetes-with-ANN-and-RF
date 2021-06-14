# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'code.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import keras


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Diabetes Prediction")
        Form.resize(611, 536)
        Form.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Form.setAcceptDrops(False)
        self.labelTitre = QtWidgets.QLabel(Form)
        self.labelTitre.setEnabled(True)
        self.labelTitre.setGeometry(QtCore.QRect(180, 30, 211, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        
        #-------------------------------------------------Line Edit
        self.lineEditNpreg = QtWidgets.QLineEdit(Form)
        self.lineEditNpreg.setGeometry(QtCore.QRect(90, 140, 171, 31))
        self.lineEditNpreg.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEditNpreg.setAcceptDrops(True)
        self.lineEditNpreg.setWhatsThis("")
        self.lineEditNpreg.setAccessibleName("")
        self.lineEditNpreg.setAccessibleDescription("")
        self.lineEditNpreg.setObjectName("lineEditNpreg")
        self.lineEditNpreg.setPlaceholderText("0 if male")
        
        self.lineEditBMI = QtWidgets.QLineEdit(Form)
        self.lineEditBMI.setGeometry(QtCore.QRect(400, 140, 171, 31))
        self.lineEditBMI.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEditBMI.setAcceptDrops(True)
        self.lineEditBMI.setWhatsThis("")
        self.lineEditBMI.setAccessibleName("")
        self.lineEditBMI.setAccessibleDescription("")
        self.lineEditBMI.setObjectName("lineEditBMI")
        self.lineEditBMI.setPlaceholderText("0-81")
        
        self.lineEditGlucose = QtWidgets.QLineEdit(Form)
        self.lineEditGlucose.setGeometry(QtCore.QRect(90, 210, 171, 31))
        self.lineEditGlucose.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEditGlucose.setAcceptDrops(True)
        self.lineEditGlucose.setWhatsThis("")
        self.lineEditGlucose.setAccessibleName("")
        self.lineEditGlucose.setAccessibleDescription("")
        self.lineEditGlucose.setObjectName("lineEditGlucose")
        self.lineEditGlucose.setPlaceholderText("0-199 mg/dl")
        
        self.lineEditAge = QtWidgets.QLineEdit(Form)
        self.lineEditAge.setGeometry(QtCore.QRect(400, 210, 171, 31))
        self.lineEditAge.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEditAge.setAcceptDrops(True)
        self.lineEditAge.setWhatsThis("")
        self.lineEditAge.setAccessibleName("")
        self.lineEditAge.setAccessibleDescription("")
        self.lineEditAge.setObjectName("lineEditAge")
        self.lineEditAge.setPlaceholderText("1-100 is recommended")
        
        
        #-------------------------------------------------Labels
        self.labelTitre.setFont(font)
        self.labelTitre.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.labelTitre.setMouseTracking(True)
        self.labelTitre.setAutoFillBackground(False)
        self.labelTitre.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.labelTitre.setScaledContents(False)
        self.labelTitre.setObjectName("labelTitre")
        
        self.labelNpreg = QtWidgets.QLabel(Form)
        self.labelNpreg.setGeometry(QtCore.QRect(18, 140, 70, 21))
        self.labelNpreg.setObjectName("labelNpreg")
        
        self.labelGlucose = QtWidgets.QLabel(Form)
        self.labelGlucose.setGeometry(QtCore.QRect(30, 210, 51, 21))
        self.labelGlucose.setObjectName("labelGlucose")
        
        self.labelBMI = QtWidgets.QLabel(Form)
        self.labelBMI.setGeometry(QtCore.QRect(350, 140, 31, 21))
        self.labelBMI.setObjectName("labelBMI")
        
        self.labelAge = QtWidgets.QLabel(Form)
        self.labelAge.setGeometry(QtCore.QRect(350, 210, 41, 21))
        self.labelAge.setObjectName("labelAge")
        
        
        self.labelPossibilityOfDiabetes = QtWidgets.QLabel(Form)
        self.labelPossibilityOfDiabetes.setGeometry(QtCore.QRect(50, 350, 250, 41))
        self.labelPossibilityOfDiabetes.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.labelPossibilityOfDiabetes.setObjectName("labelPossibilityOfDiabetes")
        
        self.labelResults = QtWidgets.QLabel(Form)
        self.labelResults.setGeometry(QtCore.QRect(70, 400, 241, 41))
        self.labelResults.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.labelResults.setObjectName("labelResults")
        
        self.label100 = QtWidgets.QLabel(Form)
        self.label100.setGeometry(QtCore.QRect(540, 400, 21, 31))
        self.label100.setObjectName("label100")
        
        
        #------------------------------------------------- Button
        self.pushButtonClear = QtWidgets.QPushButton(Form)
        self.pushButtonClear.setGeometry(QtCore.QRect(60, 300, 91, 31))
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.pushButtonClear.clicked.connect(self.clear)
        
        self.pushButtonResult = QtWidgets.QPushButton(Form)
        self.pushButtonResult.setGeometry(QtCore.QRect(460, 300, 91, 31))
        self.pushButtonResult.setObjectName("pushButtonResult")
        self.pushButtonResult.clicked.connect(self.calculation)
        
        
        #-------------------------------------------------lcdNumber
        self.lcdNumberReslults = QtWidgets.QLCDNumber(Form)
        self.lcdNumberReslults.setGeometry(QtCore.QRect(430, 400, 91, 31))
        self.lcdNumberReslults.setObjectName("lcdNumberReslults")
        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Diabetes Prediction"))
        self.labelTitre.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">Diabetes Prediction</span></p></body></html>"))
        self.labelNpreg.setText(_translate("Form", "Pregnancies :"))
        self.labelGlucose.setText(_translate("Form", "Glucose :"))
        self.labelBMI.setText(_translate("Form", "BMI :"))
        self.labelAge.setText(_translate("Form", "Age :"))
        self.pushButtonClear.setText(_translate("Form", "Clear"))
        self.pushButtonResult.setText(_translate("Form", "Result"))
        self.labelPossibilityOfDiabetes.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">--------- Possibility of Diabetes (in %)</span></p></body></html>"))
        self.labelResults.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">Results will be displayed here :</span></p></body></html>"))
        self.label100.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; color:#ff0000;\">%</span></p></body></html>"))

    def clear(self, Form):
        self.lineEditNpreg.clear()
        self.lineEditBMI.clear()
        self.lineEditGlucose.clear()
        self.lineEditAge.clear()
        self.lcdNumberReslults.display(0.000)
   
    def results(self, Form):
        
        pass
    def calculation(self):
        #feature_names ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
        model = keras.models.load_model('model_ANN.h5')
        arr     =[self.lineEditNpreg,self.lineEditBMI,self.lineEditGlucose,self.lineEditAge]
        arr ,ee = self.empty_entry_validation(arr)
        if ee == 0:
            arr     =list(map(float,arr))
            # re = self.range_validation(arr)
            # if re == 0: 
            self.arr=arr
            arr     =np.array([np.array(arr)])
            # arr     =self.model.std_scaling(arr)
            self.pred    =model.predict(arr.reshape(1,4))
            self.lcdNumberReslults.display(float(self.pred[0][0]*100))
            print(self.pred)
            # else:
            #     self.showdialog("invalid values as input")
        else:
            self.showdialog("please first enter the values")
            
    def empty_entry_validation(self,arr):
        l=[]
        empty=0
        for x in arr:
            l.append(x.text())
        if '' in l :
            empty=1
        for i in range(len(l)):
            if l[i]=='.':
                arr[i].clear()
                empty=1
        return l,empty
    
    def showdialog(self,s):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Message Alert!")
        msg.setInformativeText("Additional information")
        msg.setWindowTitle("Hi there!")
        msg.setDetailedText(s)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        msg.exec_()
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())