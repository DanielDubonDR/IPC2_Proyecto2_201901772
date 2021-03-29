class datos:
    def __init__(self, id, nombre, nFila, nColumna, matriz):
        self.id=id
        self.nombre=nombre
        self.nFila=nFila
        self.nColumna=nColumna
        self.matriz=matriz
    
    def __str__(self):
        string=str("id: ")+str(self.id)+str("\nNombre: ")+str(self.nombre)+str("\nFilas: ")+str(self.nFila)+str("\nColumnas: ")+str(self.nColumna)+str("\n")
        return string

class dtIterar:
    def __init__(self, f, c):
        self.f=f
        self.c=c
    def __str__(self):
        string=str("Fila: ")+str(self.f)+str("\nColumna: ")+str(self.c)+str("\n")
        return string