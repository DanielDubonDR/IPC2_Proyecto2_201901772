from tkinter import *
from tkinter import messagebox

def m1():
    operaciones=Tk()
    ancho_ventana = 1200
    alto_ventana = 620
    x_ventana = operaciones.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = operaciones.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)

    operaciones.geometry(posicion)
    operaciones.resizable(0,0)
    operaciones.title("Operación sobre una  imagen")
    operaciones.config(bg="white")

    barra1=Frame(operaciones, bg="#273c75")
    barra1.place(x=0, y=0, width=1200, height=70)

    lb1=Label(barra1, bg="#273c75", fg="white",text="Última operación realizada:", font=("Consolas",11), justify=LEFT)
    lb1.place(x=10, y=20, width=220, height=30)

    lb2=Label(barra1, bg="#273c75", fg="white",text="Agregar linea horizontal a una imagen", font=("Consolas",11), justify=RIGHT)
    lb2.place(x=240, y=20, width=300, height=30)


    lbM1=Label(operaciones, bg="white")
    lbM1.place(x=0, y=70, width=600, height=520)

    lbM2=Label(operaciones, bg="#f5f6fa")
    lbM2.place(x=600, y=70, width=600, height=520)


    identificador1=Label(operaciones, bg="#40739e", text="Imagen Original",  font=("Consolas",12), fg="white")
    identificador1.place(x=0, y=590, width=600, height=30)
    
    identificador2=Label(operaciones, bg="#487eb0", text="Imagen Resultante",  font=("Consolas",12), fg="white")
    identificador2.place(x=600, y=590, width=600, height=30)

    operaciones.mainloop()

def m2():
    operaciones=Tk()
    ancho_ventana = 1200
    alto_ventana = 620
    x_ventana = operaciones.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = operaciones.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)

    operaciones.geometry(posicion)
    operaciones.resizable(0,0)
    operaciones.title("Operación sobre dos imagenes")
    operaciones.config(bg="white")

    barra1=Frame(operaciones, bg="#273c75")
    barra1.place(x=0, y=0, width=1200, height=70)

    lb1=Label(barra1, bg="#273c75", fg="white",text="Última operación realizada:", font=("Consolas",11), justify=LEFT)
    lb1.place(x=10, y=20, width=220, height=30)

    lb2=Label(barra1, bg="#273c75", fg="white",text="Agregar linea horizontal a una imagen", font=("Consolas",11), justify=RIGHT)
    lb2.place(x=240, y=20, width=300, height=30)

    lbM3=Label(operaciones, bg="white")
    lbM3.place(x=0, y=70, width=400, height=520)

    lbM4=Label(operaciones, bg="#f5f6fa")
    lbM4.place(x=400, y=70, width=400, height=520)

    lbM5=Label(operaciones, bg="#f1f2f6")
    lbM5.place(x=800, y=70, width=400, height=520)

    identificador3=Label(operaciones, bg="#273c75", text="Imagen A",  font=("Consolas",12), fg="white")
    identificador3.place(x=0, y=590, width=400, height=30)
    
    identificador4=Label(operaciones, bg="#40739e", text="Imagen B",  font=("Consolas",12), fg="white")
    identificador4.place(x=400, y=590, width=400, height=30)
    
    identificador5=Label(operaciones, bg="#487eb0", text="Imagen Resultante",  font=("Consolas",12), fg="white")
    identificador5.place(x=800, y=590, width=400, height=30)

    operaciones.mainloop()

m2()