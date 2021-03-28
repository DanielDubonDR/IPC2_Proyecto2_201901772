class datos:
    def __init__(self, id, nombre, nFila, nColumna, matriz):
        self.id=id
        self.nombre=nombre
        self.nFila=nFila
        self.nColumna=nColumna
        self.matriz=matriz
    
    def __str__(self):
        string=str("id: ")+str(self.id)+str("\nNombre: ")+str(self.nombre)+str("\nFilas: ")+str(self.nFila)+str("\nColumnas: ")+str(self.nColumna)+str("\nMatriz: ")+str(self.matriz.recorrerFilas())+str("\n")
        return string