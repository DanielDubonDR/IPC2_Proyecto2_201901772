import xml.dom.minidom as minidom
from Estructuras.MOrtogonal import matrizOrtogonal
from Estructuras.ListaSimple import linked_list
from .Clases import datos

class ExtraerXML:
    def __init__(self,listaRutas):
        self.listaDatos=linked_list()
        self.listaRutas=listaRutas
    
    def extraerDatos(self):
        id=1
        for rutas in self.listaRutas.iterar():
            doc=minidom.parse(rutas.dato)
            matrices=doc.getElementsByTagName("matriz")
            for matriz in matrices:
                nombreMatriz=matriz.getElementsByTagName("nombre")[0]
                filas=matriz.getElementsByTagName("filas")[0]
                columnas=matriz.getElementsByTagName("columnas")[0]
                imagen=matriz.getElementsByTagName("imagen")[0]
                #print(nombreMatriz.firstChild.data, filas.firstChild.data, columnas.firstChild.data)
                imagenConvertidaMatriz=self.convertirImagen(imagen.firstChild.data)
                aux=datos(id,nombreMatriz.firstChild.data, filas.firstChild.data, columnas.firstChild.data,imagenConvertidaMatriz)
                self.listaDatos.append(aux)
                #print(aux)
                id+=1

    
    def convertirImagen(self, imagen):
        matriz = matrizOrtogonal()
        imagen=imagen.replace(" ","").lstrip("\n")
        lineas=imagen.splitlines()
        fila=1
        for linea in lineas:
            columna=1
            for posicion in range(len(linea)):
                if linea[posicion]=="*":
                    matriz.append(fila,columna,"*")
                columna+=1
            fila+=1
        #matriz.recorrerFilas()
        return matriz

    def getLista(self):
        return self.listaDatos