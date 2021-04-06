from tkinter import *
from tkinter import messagebox
import os

info=None
ayuda=None
doc=None

def verInfo():
    info.destroy()
    doc.place(x=270, y=210, width=300, height=28)
    texto="Nombre: Daniel Reginaldo Dubón Rodríguez \nCarné: 201901772 \nCurso: Introducción a la Programación y Computación 2, Sección \"A\" \nCarrera: Ingenieria en Ciencias y Sistemas \nSemetre: Quinto"
    lb1=Label(ayuda, bg="#353b48", fg="white",text=texto, font=("Consolas",11), justify=LEFT)
    lb1.place(x=120, y=40, width=600, height=130)

def abrir():
    path=os.getcwd()+"/Documentacion/201901772-Ensayo.pdf"
    os.startfile(path)

def ventanaHelp():
    global info
    global ayuda
    global doc
    ayuda=Tk()
    ancho_ventana = 830
    alto_ventana = 310
    x_ventana = ayuda.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = ayuda.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)

    ayuda.geometry(posicion)
    ayuda.resizable(0,0)
    ayuda.title("Ayuda")
    ayuda.config(bg="white")

    info=Button(ayuda, text="Ver información del estudiante", font=("Consolas",11), bg="#273c75", fg="white", command=verInfo)
    info.place(x=270, y=100, width=300, height=28)

    doc=Button(ayuda, text="Ver documentación", font=("Consolas",11), bg="#273c75", fg="white", command=abrir)
    doc.place(x=270, y=150, width=300, height=28)

    ayuda.mainloop()