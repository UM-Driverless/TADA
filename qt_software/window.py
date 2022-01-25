#importamos los objetos de la clase window_ui
from window_ui import *
#importamos las variables
from variables import *
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
        self.label.setText("Haz clic en el botón")
        self.pushButton.setText("Presióname")
        
        #en esta funcion se recolectaran los datos de los xbee
        def threaded_function():
            i = 0
            while(1):
                self.label.setText("bucle " + str(i))
                sleep(1)
                i = i + 1


        #creacion e inicio de un thread para poder recolectar y actualizar los datos
        thread = Thread(target = threaded_function)
        thread.start()

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

    

