from .Nodos import Nodo, nCabecera
from .Cabecera import listaCabeceras

class matriz:
    def __init__(self):
        self.cFilas = listaCabeceras()
        self.CColumnas = listaCabeceras()

    def append(self, fila, columna, dato):
        nuevo = Nodo(fila, columna, dato)

        eFila = self.cFilas.getCabecera(fila)
        if eFila == None:
            eFila = nCabecera(fila)
            eFila.accesoNodo = nuevo
            self.cFilas.appendCabecera(eFila)
        else:
            if nuevo.columna <  eFila.accesoNodo.columna:
                nuevo.derecha = eFila.accesoNodo
                eFila.accesoNodo.izquierda = nuevo
                eFila.accesoNodo = nuevo
            else:
                actual = eFila.accesoNodo
                while actual.derecha != None:
                    if nuevo.columna < actual.derecha.columna:
                        nuevo.derecha = actual.derecha
                        actual.derecha.izquierda = nuevo
                        nuevo.izquierda = actual
                        actual.derecha = nuevo
                        break
                    actual = actual.derecha
                
                if actual.derecha == None:
                    actual.derecha = nuevo
                    nuevo.izquierda = actual

        eColumna = self.CColumnas.getCabecera(columna)
        if eColumna == None:
            eColumna = nCabecera(columna)
            eColumna.accesoNodo = nuevo
            self.CColumnas.appendCabecera(eColumna)
        else:
            if nuevo.fila <  eColumna.accesoNodo.fila:
                nuevo.abajo = eColumna.accesoNodo
                eColumna.accesoNodo.arriba = nuevo
                eColumna.accesoNodo = nuevo
            else:
                actual = eColumna.accesoNodo
                while actual.abajo != None:
                    if nuevo.fila < actual.abajo.fila:
                        nuevo.abajo = actual.abajo
                        actual.abajo.arriba = nuevo
                        nuevo.arriba = actual
                        actual.abajo = nuevo
                        break
                    actual = actual.abajo
                
                if actual.abajo == None:
                    actual.abajo = nuevo
                    nuevo.arriba = actual

    def recorrerFilas(self):
        print("***********************RECORRIDO POR FILAS*************************")
        eFila = self.cFilas.primero
        while eFila != None:
            actual = eFila.accesoNodo
            print("\nFila"+str(actual.fila))
            print("Columna   dato")
            while actual != None:
                print(str(actual.columna)+"         "+actual.dato)
                actual = actual.derecha
            eFila = eFila.siguiente
        print("*********************FIN RECORRIDO POR FILAS***********************\n")

    def recorrerColumnas(self):
        print("***********************RECORRIDO POR COLUMNAS*************************")
        eColumna = self.CColumnas.primero
        while eColumna != None:
            actual = eColumna.accesoNodo
            print("\nColumna"+str(actual.columna))
            print("Fila   dato")
            while actual != None:
                print(str(actual.fila)+"      "+actual.dato)
                actual = actual.abajo
            eColumna = eColumna.siguiente
        print("*********************FIN RECORRIDO POR COLUMNAS***********************\n")


