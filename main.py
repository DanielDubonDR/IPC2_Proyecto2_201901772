from Estructuras.MOrtogonal import matrizOrtogonal
from Funciones.LeerXML import ExtraerXML
from Funciones.Graficar import graficarM

def prueba():
    n = matrizOrtogonal()
    n.append(1, 0, "adolfo")
    n.append(1, 2, "eduardo")
    n.append(0, 1, "daniel")
    n.append(2, 1, "brandon")
    n.append(0, 2, "diego")
    n.append(0, 0, "javier")
    n.recorrerFilas()
    n.recorrerColumnas()

if __name__=="__main__":
    #prueba()
    extraer=ExtraerXML("Archivos_Prueba/entrada.xml")
    extraer.extraerDatos()
    lista=extraer.getLista()
    graficarM(lista.search(1))
    '''iterar=lista.search(1).matriz.iterarFilas()
    for i in iterar:
        print(i)
        '''
    