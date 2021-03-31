from tkinter import *
from tkinter.ttk import Notebook, Combobox
from PIL import Image, ImageTk
from Estructuras.MOrtogonal import matrizOrtogonal
from Funciones.LeerXML import ExtraerXML
from Funciones.Graficar import graficarM

lista=None
combM=None
lbM1=None

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

def graficarMOriginal(event):
    global combM
    global lbM1
    matriz=combM.get()
    if matriz!="Elegir Matriz":
        graficarM(lista.searchNombre(str(matriz)))
        imgCargar=Image.open("Imagenes/"+str(matriz)+".png")
        ancho=imgCargar.size[0]
        alto=imgCargar.size[1]
        if ancho<600 and alto<520:
            imgCargar=ImageTk.PhotoImage(imgCargar)
            lbM1.configure(image=imgCargar)
            lbM1.image=imgCargar
        elif ancho>alto:
            restar=ancho-600
            imgCargar=imgCargar.resize((ancho-restar,alto-restar))
            imgCargar=ImageTk.PhotoImage(imgCargar)
            lbM1.configure(image=imgCargar)
            lbM1.image=imgCargar
        elif alto>ancho:
            restar=alto-520
            imgCargar=imgCargar.resize((ancho-restar,alto-restar))
            imgCargar=ImageTk.PhotoImage(imgCargar)
            lbM1.configure(image=imgCargar)
            lbM1.image=imgCargar
        elif alto==ancho and  ancho>alto:
            restar=ancho-600
            imgCargar=imgCargar.resize((ancho-restar,alto-restar))
            imgCargar=ImageTk.PhotoImage(imgCargar)
            lbM1.configure(image=imgCargar)
            lbM1.image=imgCargar
        elif alto==ancho and  alto>ancho:
            restar=alto-520
            imgCargar=imgCargar.resize((ancho-restar,alto-restar))
            imgCargar=ImageTk.PhotoImage(imgCargar)
            lbM1.configure(image=imgCargar)
            lbM1.image=imgCargar


def ventanaOperacion(ruta):
    global combM
    global lbM1

    datos(ruta)
    operaciones=Tk()
    ancho_ventana = 1200
    alto_ventana = 645
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
    barra1.place(x=0, y=0, width=1200, height=70)

    lb1=Label(barra1, bg="#273c75", fg="white",text="Matriz:", font=("Consolas",12))
    lb1.place(x=10, y=5, width=60, height=30)

    combM=Combobox(barra1, width="20", state="readonly", font=("Consolas",10))
    combM["values"]=(nombresM())
    combM.place(x=10, y=35)
    combM.current(0)
    combM.bind("<<ComboboxSelected>>", graficarMOriginal)

    lb2=Label(barra1, bg="#273c75", fg="white",text="Operaciones:", font=("Consolas",12))
    lb2.place(x=200, y=5, width=115, height=30)

    combOp=Combobox(barra1, width="20", state="readonly", font=("Consolas",10))
    combOp["values"]=("Elegir Operación","Rotación horizontal","Rotación vertical","Traspuesta","Limpiar zona","Agregar línea horizontal","Agregar linea vertical","Agregar rectángulo","Agregar triangulo rectangulo")
    combOp.place(x=200, y=35)
    combOp.current(0)

    lbM1=Label(tab1, bg="white")
    lbM1.place(x=0, y=70, width=600, height=520)

    lbM2=Label(tab1, bg="#f5f6fa")
    lbM2.place(x=600, y=70, width=600, height=520)

    identificador1=Label(tab1, bg="#40739e", text="Matriz Original",  font=("Consolas",12), fg="white")
    identificador1.place(x=0, y=590, width=600, height=30)
    
    identificador2=Label(tab1, bg="#487eb0", text="Matriz Modificada",  font=("Consolas",12), fg="white")
    identificador2.place(x=600, y=590, width=600, height=30)


    operaciones.mainloop()

ventanaOperacion("Archivos_Prueba/entrada.xml")
