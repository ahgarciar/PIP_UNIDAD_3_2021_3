import sys

from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "P4_ListaAlumnos.ui"  # Nombre del archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.alumnos = {
            "Pablo": ["Pablo",18, "Ing. en Mercadotecnia"],
            "Salma": ["Salma", 16, "Ing. Industrial"],
            "Gustavo": ["Gustavo", 21, "Ing. Civil"],
            "Alan": ["Alan", 19, "Ing. en Sistemas Computacionales"],
            "Leyva": ["Leyva", 20, "Ing. en Geomatica"]
        }

        self.lw_alumnos.addItem(self.alumnos.get("Pablo")[0])
        self.lw_alumnos.addItem(self.alumnos["Salma"][0])

        self.lw_alumnos.addItem(self.alumnos.get("Gustavo")[0])
        self.lw_alumnos.addItem(self.alumnos.get("Alan")[0])
        self.lw_alumnos.addItem(self.alumnos.get("Leyva")[0])

        cant_elementos = self.lw_alumnos.count()
        self.txt_total.setText(str(cant_elementos))

        self.lw_alumnos.currentRowChanged.connect(self.cambioFila)

        self.btn_eliminar.clicked.connect(self.eliminar)

    def eliminar(self):
        indice = self.lw_alumnos.currentRow()
        print(indice)
        if indice != -1:
            ##Error Detectado: Lineas al reves
            texto = self.lw_alumnos.currentItem().text()
            self.alumnos.pop(texto)

            self.lw_alumnos.takeItem(indice)


            print(self.alumnos)

    def cambioFila(self):
        try:
            indice = self.lw_alumnos.currentRow()
            texto = self.lw_alumnos.currentItem().text()
            print("indice: ", indice , "  texto: ", texto)

            #clave = indice + 1
                                     #clave
            nombre = self.alumnos.get(texto)[0] #nombre
            edad =  self.alumnos.get(texto)[1]  #edad
            carrera = self.alumnos.get(texto)[2] #carrera

            self.txt_nombre.setText(nombre)
            self.txt_edad.setText(str(edad))
            self.txt_carrera.setText(carrera)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())