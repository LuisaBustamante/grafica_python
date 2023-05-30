import sys
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5 import uic, QtWidgets
import logonormal_rc
qtCreatorFile="grafica.ui"
Ui_MainWindow, QtBaseClass= uic.loadUiType(qtCreatorFile)
class VentanaPrincipal(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.importar.clicked.connect(self.getCSV)
        self.graficar.clicked.connect(self.plot)
    def getCSV(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/Windows(C:)/')
        if filePath != "":
            print ("Dirección",filePath) #Opcional imprimir la dirección del archivo
            self.df = pd.read_csv(str(filePath))
    def plot(self):
        x=self.df["col1"]
        y=self.df["col2"]
        plt.plot(x,y)
        plt.show()
        estad_st="Estadisticas de datos: "+str(self.df['col'].describe())
        self.resultado.setText(estad_st)
  
        
if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=VentanaPrincipal()
    window.show()
    sys.exit(app.exec())