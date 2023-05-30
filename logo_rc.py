import sys
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5 import uic, QtWidgets
qtCreatorFile="grafica.ui"
Ui_MainWindow, QtBaseClass= uic.loadUiType(qtCreatorFile)
class VentanaPrincipal(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.importar.clicked.connect(self.getCSV)
        self.grafico.clicked.connect(self.plot)
        self.anomalia.clicked.connect(self.anomal)
        
    def getCSV(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/Windows(C:)/')
        if filePath != "":
            self.df = pd.read_csv(str(filePath))
            self.direccion.setText(filePath)
       
    def plot(self):
        plt.rcParams['figure.figsize']=(16.0, 6.0)
        columna = self.columnaa.toPlainText()
        columnacsv = self.df[columna]
        data=pd.DataFrame(columnacsv.iloc[0:250])
        plt.plot(data)
        plt.ylabel('datos')
        plt.show()
        estad_st="Estadisticas de datos: "+str(data.describe())
        self.resultado.setText(estad_st)
        
    def anomal(self):
        plt.rcParams['figure.figsize']=(20.0, 8.0)
        columna = self.columnaa.toPlainText()
        columnacsv = self.df[columna]
        data=pd.DataFrame(columnacsv.iloc[0:250])
        wind=15
        sigma=2
        data["suelo"] = data[columna].rolling(window=wind)\
            .mean() - (sigma * data[columna].rolling(window=wind).std())
        data["techo"] = data[columna].rolling(window=wind)\
            .mean() + (sigma * data[columna].rolling(window=wind).std())
        data.plot()
        plt.ylabel('datos')
        data["anomalía"] = data.apply(
            lambda row: row[columna] if (row[columna]<=row["suelo"] or row[columna]>=row["techo"]) else 0, axis=1)
        data.plot()
        plt.ylabel('Grafico Anomalía')
        plt.show()
        


if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=VentanaPrincipal()
    window.show()
    sys.exit(app.exec())
  
