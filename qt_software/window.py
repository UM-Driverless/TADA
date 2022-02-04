#importamos los objetos de la clase window_ui
from window_ui import *
#importamos los archivos
from variables import *
from sender import *
from data import *
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
        self.speed.setValue(0)
        #en esta funcion se recolectaran los datos de los xbee
        def datosPantalla():
            i = 0
            while(1):
                self.speed.setValue(vState)
                self.status.setText(vSpeed)
                sleep(1)
                i = i + 1


        #thread para mostrar datos por pantalla
        thread = Thread(target = datosPantalla)
        thread.start()

        #thread para enviar datos
        thread2 = Thread(target = envioDatos)
        thread2.start()

        #thread para recibir datos
        thread3 = Thread(target = comprobar)
        thread3.start()


        #llamamos a la funcion actualizar al pulsar el boton
        self.pushButton.clicked.connect(self.actualizar)

    #actualizamos el texto de la etiqueta
    def actualizar(self):
        self.label.setText("¡Acabas de hacer clic en el botón!")

    


#bucle de la ventana
if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

    

