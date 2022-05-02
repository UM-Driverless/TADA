#importamos los objetos de la clase window_ui
from window_ui import *
#importamos los archivos
from variables import *
from datos import *
#importamos los threads
from time import sleep
from PyQt5.QtCore import Qt, QTimer

#ventana principal
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    #añadimos los objetos a la ventana
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.okO.clicked.connect(self.empezar)
        
    def actualizar(self):
        datosPantalla(self)
        #en esta funcion se recolectaran los datos de los xbee
    
    def empezar(self):
        global puerto
        global continuar
        global endserial
        puerto = self.portO.text()
        serial.Serial(port=puerto, baudrate=9600, bytesize=8, parity='N', stopbits=1)
        continuar = 1


#bucle de la ventana
if __name__ == "__main__":
    
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    if continuar == 1:
        timer = QTimer()
        timer.timeout.connect(window.actualizar)  # execute `display_time`
        timer.setInterval(100)  
        timer.start()

    app.exec_()

    

