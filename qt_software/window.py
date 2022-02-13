#importamos los objetos de la clase window_ui
from window_ui import *
#importamos los archivos
from variables import *
from sender import *
from pruebaRecibir import *
from decoDatos import *
#importamos los threads
from threading import Thread
from time import sleep

#ventana principal
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    #añadimos los objetos a la ventana
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        

        #cambiamos el texto del botón y de la etiqueta
        self.status.setText("Haz clic en el botón")
        self.pushButton.setText("Presióname")
        #en esta funcion se recolectaran los datos de los xbee
        def datosPantalla():
            global rpm
            global ect
            global oilP
            global tps
            global apps
            global breakHdr
            global dvState

            while(1):
                
                #pack1:
                print(rpm)

                self.lcdRpm.display(rpm)
                self.lcdEct.display(ect)
                self.lcdOilP.display(oilP)
                self.lcdTps.display(tps)
                self.lcdApps.display(apps)
                self.lcdBreakHdr.display(breakHdr)

                #pack2:
                self.status.setText(str(dvState))
                sleep(2)

              
        #thread para enviar datos
        #thread2 = Thread(target = envioDatos)
        #thread2.start()

        #thread para recibir datos
        thread3 = Thread(target = recibo)
        thread3.start()

        thread4 = Thread(target = decodificar)
        thread4.start()

        #thread para mostrar datos por pantalla
        thread = Thread(target = datosPantalla)
        thread.start()

        #llamamos a la funcion actualizar al pulsar el boton
        self.pushButton.clicked.connect(self.actualizar)

    #actualizamos el texto de la etiqueta
    def actualizar(self):
        dvState = 10

    


#bucle de la ventana
if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

    

