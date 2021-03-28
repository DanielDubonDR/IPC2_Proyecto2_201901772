from Estructuras.MOrtogonal import matriz

def prueba():
    n = matriz()
    n.append(1, 0, "adolfo")
    n.append(1, 2, "eduardo")
    n.append(0, 1, "daniel")
    n.append(2, 1, "brandon")
    n.append(0, 2, "diego")
    n.append(0, 0, "javier")
    n.recorrerFilas()
    n.recorrerColumnas()

if __name__=="__main__":
    prueba()