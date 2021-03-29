from tkinter import *
from tkinter.ttk import Notebook
from PIL import Image, ImageTk

def ventanaOperacion(ruta):
    operaciones=Tk()
    ancho_ventana = 830
    alto_ventana = 310
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

    operaciones.mainloop()

ventanaOperacion("Archivos_Prueba/entrada.xml")
