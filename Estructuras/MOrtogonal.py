from .Nodos import Nodo, nCabecera
from .Cabecera import listaCabeceras

class matrizOrtogonal:
    def __init__(self):
        self.CFilas = listaCabeceras()
        self.CColumnas = listaCabeceras()

    def append(self, fila, columna, dato):
        nuevo = Nodo(fila, columna, dato)

        CFila = self.CFilas.getCabecera(fila)
        if CFila == None:
            CFila = nCabecera(fila)
            CFila.accesoNodo = nuevo
            self.CFilas.appendCabecera(CFila)
        else:
            if nuevo.columna <  CFila.accesoNodo.columna:
                nuevo.derecha = CFila.accesoNodo
                CFila.accesoNodo.izquierda = nuevo
                CFila.accesoNodo = nuevo
            else:
                actual = CFila.accesoNodo
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

        CColumna = self.CColumnas.getCabecera(columna)
        if CColumna == None:
            CColumna = nCabecera(columna)
            CColumna.accesoNodo = nuevo
            self.CColumnas.appendCabecera(CColumna)
        else:
            if nuevo.fila <  CColumna.accesoNodo.fila:
                nuevo.abajo = CColumna.accesoNodo
                CColumna.accesoNodo.arriba = nuevo
                CColumna.accesoNodo = nuevo
            else:
                actual = CColumna.accesoNodo
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
        CFila = self.CFilas.primero
        while CFila != None:
            actual = CFila.accesoNodo
            print("\nFila"+str(actual.fila))
            print("Columna   dato")
            while actual != None:
                print(str(actual.columna)+"         "+actual.dato)
                actual = actual.derecha
            CFila = CFila.siguiente
        print("*********************FIN RECORRIDO POR FILAS***********************\n")

    def recorrerColumnas(self):
        print("***********************RECORRIDO POR COLUMNAS*************************")
        CColumna = self.CColumnas.primero
        while CColumna != None:
            actual = CColumna.accesoNodo
            print("\nColumna"+str(actual.columna))
            print("Fila   dato")
            while actual != None:
                print(str(actual.fila)+"      "+actual.dato)
                actual = actual.abajo
            CColumna = CColumna.siguiente
        print("*********************FIN RECORRIDO POR COLUMNAS***********************\n")


