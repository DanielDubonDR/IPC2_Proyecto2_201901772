from tkinter import *
from tkinter.ttk import Notebook, Combobox
from PIL import Image, ImageTk
from Estructuras.MOrtogonal import matrizOrtogonal
from Funciones.LeerXML import ExtraerXML
from Funciones.Graficar import graficarM

lista=None

def datos(ruta):
    global lista
    extraer=ExtraerXML(ruta)
    extraer.extraerDatos()
    lista=extraer.getLista()

def nombresM():
    laux=[]
    laux.append("Elegir Matriz")
    for i in lista.iterar():
        laux.append(i.dato.nombre)
    return laux

def ventanaOperacion(ruta):
    datos(ruta)
    operaciones=Tk()
    ancho_ventana = 900
    alto_ventana = 600
    x_ventana = operaciones.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = operaciones.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)

    operaciones.geometry(posicion)
    operaciones.resizable(0,0)
    operaciones.title("Operaciones")
    operaciones.config(bg="white")

    tabControl=Notebook(operaciones)
    tab1=Frame(tabControl, bg="white")
    tab2=Frame(tabControl, bg="white")
    tabControl.add(tab1, text="Operaciones sobre una imagen")
    tabControl.add(tab2, text="Operaciones sobre dos imagenes")
    tabControl.pack(expand=1, fill="both")

    barra1=Frame(tab1, bg="#273c75")
    barra1.place(x=0, y=0, width=900, height=70)

    lb1=Label(barra1, bg="#273c75", fg="white",text="Matriz:", font=("Consolas",12))
    lb1.place(x=10, y=5, width=60, height=30)

    combM=Combobox(barra1, width="20", state="readonly", font=("Consolas",10))
    combM["values"]=(nombresM())
    combM.place(x=10, y=35)
    combM.current(0)

    lb2=Label(barra1, bg="#273c75", fg="white",text="Operaciones:", font=("Consolas",12))
    lb2.place(x=200, y=5, width=115, height=30)

    combOp=Combobox(barra1, width="20", state="readonly", font=("Consolas",10))
    combOp["values"]=("Elegir Operación","Rotación horizontal","Rotación vertical","Traspuesta","Limpiar zona","Agregar línea horizontal","Agregar linea vertical","Agregar rectángulo","Agregar triangulo rectangulo")
    combOp.place(x=200, y=35)
    combOp.current(0)

    lbM1=Label(tab1)
    lbM1.place(x=0, y=70, width=500, height=500)

    operaciones.mainloop()

ventanaOperacion("Archivos_Prueba/entrada.xml")
