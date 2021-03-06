from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from ventanaOperaciones import ventanaOperacion
from Estructuras.ListaSimple import linked_list
from ventanaAyuda import ventanaHelp
from Funciones.Clases import dtPanel, reporte
from ventanaPanel import m1, m2
from Funciones.LeerXML import ExtraerXML
import datetime as datetime
from Funciones.ReportarLogs import reporte1, reporte2
from tkinter import messagebox
#--------------------------------------------VARIABLES GLOBALES-------------------------------------------------
listaRutas=linked_list()
listaLogs=None
listaDatos=None
menu=None
Panels=dtPanel(0, None, None, None)
xs = datetime.datetime.now()
fecha=str(xs.strftime("%d"))+str("/")+str(xs.strftime("%m"))+str("/")+str(xs.strftime("%Y"))







#----------------------------------------------MENU PRINCIPAL-------------------------------------------------

def cargarArchivo():
    global listaRutas
    ruta=""
    ruta =  askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.xml*"), ("all files", "*.*")))
    if ruta!="":
        listaRutas.append(ruta)
        messagebox.showinfo("Success","Archivo cargado")

def ventanaOp():
    cont=0
    for i in listaRutas.iterar():
        cont+=1
    if cont==0:
        messagebox.showerror("Error","No se cargó ningún archivo")
    else:
        menu.destroy()
        ventanaOperacion(listaRutas)

def ventanaPanel():
    if Panels.id==0:
        messagebox.showerror("Error","No se ha realizado ninguna operación aún")
    elif Panels.id==1:
        menu.destroy()
        m1(Panels)
    elif Panels.id==2:
        menu.destroy()
        m2(Panels)

def setPanels(aux):
    global Panels
    Panels=aux

def setRutas(rt):
    global listaRutas
    listaRutas=rt

def setLogs(rt):
    global listaLogs
    listaLogs=rt

def getHora():
    x = datetime.datetime.now()
    hora=str(x.strftime("%H"))+str(":")+str(x.strftime("%M"))+str(":")+str(x.strftime("%S"))
    return hora

def datos():
    global listaDatos
    extraer=ExtraerXML(listaRutas)
    extraer.extraerDatos()
    listaDatos=extraer.getLista()

def actualizar():
    global listaLogs
    listaLogs=linked_list()
    for i in listaDatos.iterar():
        cont=0
        for j in i.dato.matriz.iterarFilasNodos():
            if j.dato=="*":
                cont+=1
        vacios=(int(i.dato.nFila)*int(i.dato.nColumna))-cont
        #dsasd=reporte(1,i.dato.nombre,cont,vacios,fecha,getHora,None, None)
        #print(dsasd)
        listaLogs.append(reporte(1,i.dato.nombre,cont,vacios,fecha,getHora(),None, None))

def reportar():
    cont=0
    for i in listaRutas.iterar():
        cont+=1
    if cont==0:
        messagebox.showerror("Error","No se cargó ningún archivo")
    else:
        if listaLogs==None:
            datos()
            actualizar()
            reporte1(listaLogs)
        else:
            reporte2(listaLogs)

def principal():
    global menu
    menu=Tk()

    ancho_ventana = 830
    alto_ventana = 310
    x_ventana = menu.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = menu.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)

    menu.geometry(posicion)
    menu.resizable(0,0)
    menu.title("Menú Principal")
    menu.config(bg="white")

    lb1=Label(menu, text="Bienvenido", bg="white", font=("Forte",35))
    lb1.place(x=80, y=25, width=220, height=60)

    imgCargar=Image.open('Resources/cg.png')
    imgCargar=imgCargar.resize((100,100),Image.ANTIALIAS)
    imgCargar=ImageTk.PhotoImage(imgCargar)
    btnCargar=Button(menu, image=imgCargar, bg="white", command=cargarArchivo)
    btnCargar.place(x=80, y=120)

    imgOp=Image.open('Resources/ventas.png')
    imgOp=imgOp.resize((100,100),Image.ANTIALIAS)
    imgOp=ImageTk.PhotoImage(imgOp)
    btnOp=Button(menu, image=imgOp, bg="white", command=ventanaOp)
    btnOp.place(x=220, y=120)

    imgReporte=Image.open('Resources/reporte.png')
    imgReporte=imgReporte.resize((100,100),Image.ANTIALIAS)
    imgReporte=ImageTk.PhotoImage(imgReporte)
    btnReporte=Button(menu, image=imgReporte, bg="white", command=reportar)
    btnReporte.place(x=360, y=120)

    imgAyuda=Image.open('Resources/i.png')
    imgAyuda=imgAyuda.resize((100,100),Image.ANTIALIAS)
    imgAyuda=ImageTk.PhotoImage(imgAyuda)
    btnAyuda=Button(menu, image=imgAyuda, bg="white", command=ventanaHelp)
    btnAyuda.place(x=500, y=120)

    imgPanel=Image.open('Resources/lista.png')
    imgPanel=imgPanel.resize((100,100),Image.ANTIALIAS)
    imgPanel=ImageTk.PhotoImage(imgPanel)
    btnPanel=Button(menu, image=imgPanel, bg="white", command=ventanaPanel)
    btnPanel.place(x=640, y=120)

    lb2=Label(menu, text="Cargar Archivo", bg="white", font=("Consolas",9))
    lb2.place(x=80, y=230, width=100, height=30)

    lb3=Label(menu, text="Operaciones", bg="white", font=("Consolas",9))
    lb3.place(x=220, y=230, width=100, height=30)

    lb4=Label(menu, text="Reportes", bg="white", font=("Consolas",9))
    lb4.place(x=360, y=230, width=100, height=30)

    lb5=Label(menu, text="Ayuda", bg="white", font=("Consolas",9))
    lb5.place(x=500, y=230, width=100, height=30)

    lb6=Label(menu, text="Panel", bg="white", font=("Consolas",9))
    lb6.place(x=640, y=230, width=100, height=30)

    menu.mainloop()

if __name__=="__main__":
    principal()