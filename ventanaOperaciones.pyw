from tkinter import *
from tkinter.ttk import Notebook, Combobox
from PIL import Image, ImageTk
from Estructuras.MOrtogonal import matrizOrtogonal
from Funciones.LeerXML import ExtraerXML
from Funciones.Graficar import graficarM, graficarMOriginalD
from tkinter import messagebox
from Estructuras.ListaSimple import linked_list
from Funciones.Clases import datos as dts
from Funciones.Clases import dtPanel

lista=None
listaCopia=None
combM=None
combOp=None
combOp2=None
lbM1=None
lbM2=None
lbM3=None
lbM4=None
lbM5=None
txtF1=None
txtF2=None
txtF3=None
txtF4=None
txtF5=None
action=None
lbT=None
barra1=None
rt=None
combA=None
combB=None
combOpG=None
preview=None
barra2=None
btn2=None
operaciones=None
xdPanel=dtPanel(0, None, None, None)

def datos(ruta):
    global lista
    extraer=ExtraerXML(ruta)
    extraer.extraerDatos()
    lista=extraer.getLista()

def reset():
    global lista
    global combOp
    extraer=ExtraerXML(rt)
    extraer.extraerDatos()
    lista=extraer.getLista()
    graficarMOriginal1()
    combOp.current(0)


#--------------------------------------------------------------------------COMIENZA TAB1-------------------------------------------------------------- 

def changeHorizontal(aux):
    global xdPanel
    #listaCopia.searchNombre("M1").matriz.append(2,2,"*")
    #listaCopia.searchNombre("M1").matriz.cambiarValor(2,2,"*") 
    matrizAux=matrizOrtogonal()
    filas=int(aux.nFila)
    for i in range(1,filas+1):
        for j in range(1,int(aux.nColumna)+1):
            if aux.matriz.verificarExiste2(i,j):
                nuevo=filas-(i-1)
                matrizAux.append(nuevo,j,"*")
    aux.matriz=matrizAux
    xdPanel=dtPanel(1, combM.get(), None, combOp.get())

def changeVertical(aux): 
    global xdPanel
    matrizAux=matrizOrtogonal()
    filas=int(aux.nFila)
    columnas=int(aux.nColumna)
    for i in range(1,filas+1):
        for j in range(1,columnas+1):
            if aux.matriz.verificarExiste2(i,j):
                nuevo=columnas-(j-1)
                matrizAux.append(i,nuevo,"*")
    aux.matriz=matrizAux
    xdPanel=dtPanel(1, combM.get(), None, combOp.get())

def changeTranspuesta(aux): 
    global xdPanel
    matrizAux=matrizOrtogonal()
    filas=int(aux.nFila)
    columnas=int(aux.nColumna)
    for i in range(1,filas+1):
        for j in range(1,columnas+1):
            if aux.matriz.verificarExiste2(i,j):
                matrizAux.append(j,i,"*")
    aux.matriz=matrizAux
    xdPanel=dtPanel(1, combM.get(), None, combOp.get())

def nombresM():
    laux=[]
    laux.append("Elegir Matriz")
    for i in lista.iterar():
        laux.append(i.dato.nombre)
    return laux

def graficarMOriginal(event):
    global combM
    global combOp
    global lbM1
    lbM2.configure(image="")
    combOp.current(0)
    matriz=combM.get()
    if matriz!="Elegir Matriz":
        graficarM(lista.searchNombre(str(matriz)))
        graficarMOriginalD(lista.searchNombre(str(matriz)))
        #change(lista.searchNombre(str(matriz)))
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
        elif alto>ancho and alto<520:
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
    else:
        lbM1.configure(image="")

def clearTxt1(event):
    txtF1.delete(0, END)

def clearTxt2(event):
    txtF2.delete(0, END)

def clearTxt3(event):
    txtF3.delete(0, END)

def clearTxt4(event):
    txtF4.delete(0, END)

def clearTxt5(event):
    txtF5.delete(0, END)

def destruirComponentesLimpiarZona():
    txtF1.destroy()
    txtF2.destroy()
    txtF3.destroy()
    txtF4.destroy()
    lbT.destroy()
    action.destroy()

def destruirComponentesTRec():
    txtF1.destroy()
    txtF2.destroy()
    txtF3.destroy()
    action.destroy()
    
def destruirComponentesAddLnHV():
    txtF1.destroy()
    txtF2.destroy()
    txtF3.destroy()
    action.destroy()

def componentesLimpiarZona():
    global txtF1
    global txtF2
    global txtF3
    global txtF4
    global lbT
    global action

    txtF1=Entry(barra1, font=("Consolas",10), justify=CENTER)
    txtF1.insert(0,"Fila")
    txtF1.place(x=750, y=24, width=48, height=26)
    txtF1.bind("<Button-1>", clearTxt1)

    txtF2=Entry(barra1, font=("Consolas",8), justify=CENTER)
    txtF2.insert(0,"Columna")
    txtF2.place(x=802, y=24, width=48, height=26)
    txtF2.bind("<Button-1>", clearTxt2)

    lbT=Label(barra1, bg="#273c75", fg="white",text="hasta", font=("Consolas",11))
    lbT.place(x=853, y=24, width=50, height=26)

    txtF3=Entry(barra1, font=("Consolas",10), justify=CENTER)
    txtF3.insert(0,"Fila")
    txtF3.place(x=908, y=24, width=48, height=26)
    txtF3.bind("<Button-1>", clearTxt3)

    txtF4=Entry(barra1, font=("Consolas",8), justify=CENTER)
    txtF4.insert(0,"Columna")
    txtF4.place(x=961, y=24, width=48, height=26)
    txtF4.bind("<Button-1>", clearTxt4)

    action=Button(barra1, text="Limpiar", font=("Consolas",11), bg="#006266", fg="white", command=limpiarZona)
    action.place(x=1025, y=24, width=75, height=28)

def componentesAddRec():
    global txtF1
    global txtF2
    global txtF3
    global txtF4
    global lbT
    global action

    txtF1=Entry(barra1, font=("Consolas",10), justify=CENTER)
    txtF1.insert(0,"Fila")
    txtF1.place(x=750, y=24, width=54, height=26)
    txtF1.bind("<Button-1>", clearTxt1)

    txtF2=Entry(barra1, font=("Consolas",10), justify=CENTER)
    txtF2.insert(0,"Columna")
    txtF2.place(x=812, y=24, width=54, height=26)
    txtF2.bind("<Button-1>", clearTxt2)

    lbT=Label(barra1, bg="#273c75", fg="white",text="Dimensiones", font=("Consolas",8))
    lbT.place(x=905, y=6, width=80, height=22)

    txtF3=Entry(barra1, font=("Consolas",10), justify=CENTER)
    txtF3.insert(0,"Alto")
    txtF3.place(x=890, y=24, width=54, height=26)
    txtF3.bind("<Button-1>", clearTxt3)

    txtF4=Entry(barra1, font=("Consolas",10), justify=CENTER)
    txtF4.insert(0,"Ancho")
    txtF4.place(x=951, y=24, width=54, height=26)
    txtF4.bind("<Button-1>", clearTxt4)

    action=Button(barra1, text="Insertar", font=("Consolas",11), bg="#006266", fg="white", command=addRec)
    action.place(x=1025, y=24, width=75, height=28)
    
def componentesAddTRec():
    global txtF1
    global txtF2
    global txtF3
    global action

    txtF1=Entry(barra1, font=("Consolas",10), justify=CENTER)
    txtF1.insert(0,"Fila")
    txtF1.place(x=800, y=24, width=54, height=26)
    txtF1.bind("<Button-1>", clearTxt1)

    txtF2=Entry(barra1, font=("Consolas",10), justify=CENTER)
    txtF2.insert(0,"Columna")
    txtF2.place(x=862, y=24, width=54, height=26)
    txtF2.bind("<Button-1>", clearTxt2)

    txtF3=Entry(barra1, font=("Consolas",10), justify=CENTER)
    txtF3.insert(0,"Tamaño")
    txtF3.place(x=930, y=24, width=54, height=26)
    txtF3.bind("<Button-1>", clearTxt3)

    action=Button(barra1, text="Insertar", font=("Consolas",11), bg="#006266", fg="white", command=addTRec)
    action.place(x=1025, y=24, width=75, height=28)

def componentesAddLnH():
    global txtF1
    global txtF2
    global txtF3
    global txtF4
    global lbT
    global action

    txtF1=Entry(barra1, font=("Consolas",10), justify=CENTER)
    txtF1.insert(0,"Fila")
    txtF1.place(x=770, y=24, width=55, height=26)
    txtF1.bind("<Button-1>", clearTxt1)

    txtF2=Entry(barra1, font=("Consolas",10), justify=CENTER)
    txtF2.insert(0,"Columna")
    txtF2.place(x=835, y=24, width=55, height=26)
    txtF2.bind("<Button-1>", clearTxt2)

    txtF3=Entry(barra1, font=("Consolas",10), justify=CENTER)
    txtF3.insert(0,"No. elementos")
    txtF3.place(x=900, y=24, width=100, height=26)
    txtF3.bind("<Button-1>", clearTxt3)

    action=Button(barra1, text="Agregar", font=("Consolas",11), bg="#006266", fg="white", command=addLnH)
    action.place(x=1025, y=24, width=75, height=28)

def componentesAddLnV():
    global txtF1
    global txtF2
    global txtF3
    global txtF4
    global lbT
    global action

    txtF1=Entry(barra1, font=("Consolas",10), justify=CENTER)
    txtF1.insert(0,"Fila")
    txtF1.place(x=770, y=24, width=55, height=26)
    txtF1.bind("<Button-1>", clearTxt1)

    txtF2=Entry(barra1, font=("Consolas",10), justify=CENTER)
    txtF2.insert(0,"Columna")
    txtF2.place(x=835, y=24, width=55, height=26)
    txtF2.bind("<Button-1>", clearTxt2)

    txtF3=Entry(barra1, font=("Consolas",10), justify=CENTER)
    txtF3.insert(0,"No. elementos")
    txtF3.place(x=900, y=24, width=100, height=26)
    txtF3.bind("<Button-1>", clearTxt3)

    action=Button(barra1, text="Agregar", font=("Consolas",11), bg="#006266", fg="white", command=addLnV)
    action.place(x=1025, y=24, width=75, height=28)

def limpiarZona():
    global xdPanel
    f1=txtF1.get()
    c1=txtF2.get()
    f2=txtF3.get()
    c2=txtF4.get()
    if f1.isnumeric() and f2.isnumeric() and c1.isnumeric() and c2.isnumeric():
        for i in range(int(f1),int(f2)+1):
            for j in range(int(c1),int(c2)+1):
                if lista.searchNombre(combM.get()).matriz.verificarExiste(i,j):
                    lista.searchNombre(combM.get()).matriz.cambiarValor(i,j,"-")
        graficarEnM2(combM.get())
    else:
        messagebox.showerror("Error","Formato incorrecto")
    xdPanel=dtPanel(1, combM.get(), None, combOp.get())
    combOp.current(0)
    destruirComponentesLimpiarZona()

def addLnH():
    global xdPanel
    f1=txtF1.get()
    c1=txtF2.get()
    c2=txtF3.get()
    if f1.isnumeric() and c1.isnumeric() and c2.isnumeric():
        for j in range(int(c1),int(c1)+int(c2)):
            if lista.searchNombre(combM.get()).matriz.verificarExiste(int(f1),j):
                lista.searchNombre(combM.get()).matriz.cambiarValor(int(f1),j,"*")
            else:
                lista.searchNombre(combM.get()).matriz.append(int(f1),j,"*")
        graficarEnM2(combM.get())
    else:
        messagebox.showerror("Error","Formato incorrecto")
    xdPanel=dtPanel(1, combM.get(), None, combOp.get())
    combOp.current(0)
    destruirComponentesAddLnHV()

def addLnV():
    global xdPanel
    f1=txtF1.get()
    c1=txtF2.get()
    c2=txtF3.get()
    if f1.isnumeric() and c1.isnumeric() and c2.isnumeric():
        for f in range(int(f1),int(f1)+int(c2)):
            if lista.searchNombre(combM.get()).matriz.verificarExiste(f,int(c1)):
                lista.searchNombre(combM.get()).matriz.cambiarValor(f,int(c1),"*")
            else:
                lista.searchNombre(combM.get()).matriz.append(f,int(c1),"*")
        graficarEnM2(combM.get())
    else:
        messagebox.showerror("Error","Formato incorrecto")
    xdPanel=dtPanel(1, combM.get(), None, combOp.get())
    combOp.current(0)
    destruirComponentesAddLnHV()

def addRec():
    global xdPanel
    f1=txtF1.get()
    c1=txtF2.get()
    alto=txtF3.get()
    ancho=txtF4.get()
    if f1.isnumeric() and c1.isnumeric() and alto.isnumeric() and ancho.isnumeric():
        for i in range(int(f1),int(f1)+int(alto)):
            for j in range(int(c1),int(c1)+int(ancho)):
                if lista.searchNombre(combM.get()).matriz.verificarExiste(i,j):
                    lista.searchNombre(combM.get()).matriz.cambiarValor(i,j,"*")
                else:
                    lista.searchNombre(combM.get()).matriz.append(i,j,"*")
        graficarEnM2(combM.get())
    else:
        messagebox.showerror("Error","Formato incorrecto")
    xdPanel=dtPanel(1, combM.get(), None, combOp.get())
    combOp.current(0)
    destruirComponentesLimpiarZona()

def addTRec():
    global xdPanel
    f1=txtF1.get()
    c1=txtF2.get()
    alto=txtF3.get()
    if f1.isnumeric() and c1.isnumeric() and alto.isnumeric():
        for i in range(int(f1),int(f1)+int(alto)):
            for j in range(int(c1),int(c1)+i-1):
                if lista.searchNombre(combM.get()).matriz.verificarExiste(i,j):
                    lista.searchNombre(combM.get()).matriz.cambiarValor(i,j,"*")
                else:
                    lista.searchNombre(combM.get()).matriz.append(i,j,"*")
        graficarEnM2(combM.get())
    else:
        messagebox.showerror("Error","Formato incorrecto")
    xdPanel=dtPanel(1, combM.get(), None, combOp.get())
    combOp.current(0)
    destruirComponentesTRec()

def graficarMOriginal1():
    global combM
    global lbM1
    global lbM2
    lbM2.configure(image="")
    clear()
    matriz=combM.get()
    if matriz!="Elegir Matriz":
        graficarM(lista.searchNombre(str(matriz)))
        #change(lista.searchNombre(str(matriz)))
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
        elif alto>ancho and alto<520:
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

def graficarMModificada(event):
    global combOp
    global combM
    global lbM2
    matriz=combM.get()
    operacion=combOp.get()
    if matriz!="Elegir Matriz" and operacion!="Elegir Operación":
        if operacion=="Rotación horizontal":
            changeHorizontal(lista.searchNombre(str(matriz)))
            graficarEnM2(matriz)
        elif operacion=="Rotación vertical":
            changeVertical(lista.searchNombre(str(matriz)))
            graficarEnM2(matriz)
        elif operacion=="Transpuesta":
            changeTranspuesta(lista.searchNombre(str(matriz)))
            graficarEnM2(matriz)
        elif operacion=="Limpiar zona":
            componentesLimpiarZona()
        elif operacion=="Agregar línea horizontal":
            componentesAddLnH()
        elif operacion=="Agregar línea vertical":
            componentesAddLnV()
        elif operacion=="Agregar rectángulo":
            componentesAddRec()
        elif operacion=="Agregar triángulo rectángulo":
            componentesAddTRec()
    else:
        messagebox.showerror("Error","No ha seleccionado ninguna matriz")
        combOp.current(0)

def graficarEnM2(matriz):
    graficarM(lista.searchNombre(str(matriz)))
    imgCargar=Image.open("Imagenes/"+str(matriz)+".png")
    ancho=imgCargar.size[0]
    alto=imgCargar.size[1]
    if ancho<600 and alto<520:
        imgCargar=ImageTk.PhotoImage(imgCargar)
        lbM2.configure(image=imgCargar)
        lbM2.image=imgCargar
    elif ancho>alto:
        restar=ancho-600
        imgCargar=imgCargar.resize((ancho-restar,alto-restar))
        imgCargar=ImageTk.PhotoImage(imgCargar)
        lbM2.configure(image=imgCargar)
        lbM2.image=imgCargar
    elif alto>ancho and alto<520:
        restar=ancho-600
        imgCargar=imgCargar.resize((ancho-restar,alto-restar))
        imgCargar=ImageTk.PhotoImage(imgCargar)
        lbM2.configure(image=imgCargar)
        lbM2.image=imgCargar
    elif alto>ancho:
        restar=alto-520
        imgCargar=imgCargar.resize((ancho-restar,alto-restar))
        imgCargar=ImageTk.PhotoImage(imgCargar)
        lbM2.configure(image=imgCargar)
        lbM2.image=imgCargar
    elif alto==ancho and  ancho>alto:
        restar=ancho-600
        imgCargar=imgCargar.resize((ancho-restar,alto-restar))
        imgCargar=ImageTk.PhotoImage(imgCargar)
        lbM2.configure(image=imgCargar)
        lbM2.image=imgCargar
    elif alto==ancho and  alto>ancho:
        restar=alto-520
        imgCargar=imgCargar.resize((ancho-restar,alto-restar))
        imgCargar=ImageTk.PhotoImage(imgCargar)
        lbM2.configure(image=imgCargar)
        lbM2.image=imgCargar

def clear():
    eleccion=combOp.get()
    if eleccion=="Limpiar zona":
        destruirComponentesLimpiarZona()
    elif eleccion=="Agregar línea horizontal":
        destruirComponentesAddLnHV()
    elif eleccion=="Agregar línea vertical":
        destruirComponentesAddLnHV()
    elif eleccion=="Agregar rectángulo":
        destruirComponentesLimpiarZona()
    elif eleccion=="Agregar triángulo rectángulo":
        destruirComponentesTRec()

#--------------------------------------------------------------------------FIN TAB1-------------------------------------------------------------- 


#------------------------------------------------------------------------INICIO TAB2--------------------------------------------------------------
def tipoGuardado():
    laux=[]
    laux.append("Elegir Opción")
    laux.append("Guardar como nueva imagen")
    for i in lista.iterar():
        laux.append(str("Sustituir en ")+str(i.dato.nombre))
    return laux

def graficarA(event):
    global combA
    global lbM3
    combOp2.current(0)
    lbM5.configure(image="")
    matriz=combA.get()
    if matriz!="Elegir Matriz":
        graficarM(lista.searchNombre(str(matriz)))
        #change(lista.searchNombre(str(matriz)))
        imgCargar=Image.open("Imagenes/"+str(matriz)+".png")
        ancho=imgCargar.size[0]
        alto=imgCargar.size[1]
        if ancho<400 and alto<520:
            imgCargar=ImageTk.PhotoImage(imgCargar)
            lbM3.configure(image=imgCargar)
            lbM3.image=imgCargar
        elif ancho>alto:
            restar=ancho-400
            imgCargar=imgCargar.resize((ancho-restar,alto-restar))
            imgCargar=ImageTk.PhotoImage(imgCargar)
            lbM3.configure(image=imgCargar)
            lbM3.image=imgCargar
        elif alto>ancho and alto<520:
            restar=ancho-400
            imgCargar=imgCargar.resize((ancho-restar,alto-restar))
            imgCargar=ImageTk.PhotoImage(imgCargar)
            lbM3.configure(image=imgCargar)
            lbM3.image=imgCargar
        elif alto>ancho:
            restar=alto-520
            imgCargar=imgCargar.resize((ancho-restar,alto-restar))
            imgCargar=ImageTk.PhotoImage(imgCargar)
            lbM3.configure(image=imgCargar)
            lbM3.image=imgCargar
        elif alto==ancho and  ancho>alto:
            restar=ancho-400
            imgCargar=imgCargar.resize((ancho-restar,alto-restar))
            imgCargar=ImageTk.PhotoImage(imgCargar)
            lbM3.configure(image=imgCargar)
            lbM3.image=imgCargar
        elif alto==ancho and  alto>ancho:
            restar=alto-520
            imgCargar=imgCargar.resize((ancho-restar,alto-restar))
            imgCargar=ImageTk.PhotoImage(imgCargar)
            lbM3.configure(image=imgCargar)
            lbM3.image=imgCargar
    else:
        lbM3.configure(image="")

def graficarB(event):
    global combB
    global lbM4
    combOp2.current(0)
    lbM5.configure(image="")
    matriz=combB.get()
    if matriz!="Elegir Matriz":
        graficarM(lista.searchNombre(str(matriz)))
        #change(lista.searchNombre(str(matriz)))
        imgCargar=Image.open("Imagenes/"+str(matriz)+".png")
        ancho=imgCargar.size[0]
        alto=imgCargar.size[1]
        if ancho<400 and alto<520:
            imgCargar=ImageTk.PhotoImage(imgCargar)
            lbM4.configure(image=imgCargar)
            lbM4.image=imgCargar
        elif ancho>alto:
            restar=ancho-400
            imgCargar=imgCargar.resize((ancho-restar,alto-restar))
            imgCargar=ImageTk.PhotoImage(imgCargar)
            lbM4.configure(image=imgCargar)
            lbM4.image=imgCargar
        elif alto>ancho and alto<520:
            restar=ancho-400
            imgCargar=imgCargar.resize((ancho-restar,alto-restar))
            imgCargar=ImageTk.PhotoImage(imgCargar)
            lbM4.configure(image=imgCargar)
            lbM4.image=imgCargar
        elif alto>ancho:
            restar=alto-520
            imgCargar=imgCargar.resize((ancho-restar,alto-restar))
            imgCargar=ImageTk.PhotoImage(imgCargar)
            lbM4.configure(image=imgCargar)
            lbM4.image=imgCargar
        elif alto==ancho and  ancho>alto:
            restar=ancho-400
            imgCargar=imgCargar.resize((ancho-restar,alto-restar))
            imgCargar=ImageTk.PhotoImage(imgCargar)
            lbM4.configure(image=imgCargar)
            lbM4.image=imgCargar
        elif alto==ancho and  alto>ancho:
            restar=alto-520
            imgCargar=imgCargar.resize((ancho-restar,alto-restar))
            imgCargar=ImageTk.PhotoImage(imgCargar)
            lbM4.configure(image=imgCargar)
            lbM4.image=imgCargar
    else:
        lbM4.configure(image="")

def graficarResultado(matriz):
    global lbM5
    graficarM(matriz)
    imgCargar=Image.open("Imagenes/Resultado.png")
    ancho=imgCargar.size[0]
    alto=imgCargar.size[1]
    if ancho<400 and alto<520:
        imgCargar=ImageTk.PhotoImage(imgCargar)
        lbM5.configure(image=imgCargar)
        lbM5.image=imgCargar
    elif ancho>alto:
        restar=ancho-400
        imgCargar=imgCargar.resize((ancho-restar,alto-restar))
        imgCargar=ImageTk.PhotoImage(imgCargar)
        lbM5.configure(image=imgCargar)
        lbM5.image=imgCargar
    elif alto>ancho and alto<520:
        restar=ancho-400
        imgCargar=imgCargar.resize((ancho-restar,alto-restar))
        imgCargar=ImageTk.PhotoImage(imgCargar)
        lbM5.configure(image=imgCargar)
        lbM5.image=imgCargar
    elif alto>ancho:
        restar=alto-520
        imgCargar=imgCargar.resize((ancho-restar,alto-restar))
        imgCargar=ImageTk.PhotoImage(imgCargar)
        lbM5.configure(image=imgCargar)
        lbM5.image=imgCargar
    elif alto==ancho and  ancho>alto:
        restar=ancho-400
        imgCargar=imgCargar.resize((ancho-restar,alto-restar))
        imgCargar=ImageTk.PhotoImage(imgCargar)
        lbM5.configure(image=imgCargar)
        lbM5.image=imgCargar
    elif alto==ancho and  alto>ancho:
        restar=alto-520
        imgCargar=imgCargar.resize((ancho-restar,alto-restar))
        imgCargar=ImageTk.PhotoImage(imgCargar)
        lbM5.configure(image=imgCargar)
        lbM5.image=imgCargar

def resultado2img(event):
    global lbM5
    matrizA1=combA.get()
    matrizB1=combB.get()
    operacion=combOp2.get()
    if matrizA1!="Elegir Matriz" and matrizB1!="Elegir Matriz":
        if operacion=="Unión A, B":
            unionAB(lista.searchNombre(str(matrizA1)), lista.searchNombre(str(matrizB1)))
        elif operacion=="Intersección A, B":
            interseccionAB(lista.searchNombre(str(matrizA1)), lista.searchNombre(str(matrizB1)))
        elif operacion=="Diferencia A, B":
            diferenciaAB(lista.searchNombre(str(matrizA1)), lista.searchNombre(str(matrizB1)))
        elif operacion=="Diferencia simétrica A, B":
            diferenciaSimetricaAB(lista.searchNombre(str(matrizA1)), lista.searchNombre(str(matrizB1)))
    else:
        messagebox.showerror("Error","No han las matrices a operar")
        combOp2.current(0)

def unionAB(A,B):
    global preview
    nFilas=0
    nColumnas=0
    Maux=matrizOrtogonal()
    if int(A.nFila)>int(B.nFila):
        nFilas=int(A.nFila)
    elif int(A.nFila)==int(B.nFila):
        nFilas=int(A.nFila)
    else:
        nFilas=int(B.nFila)
    
    if int(A.nColumna)>int(B.nColumna):
        nColumnas=int(A.nColumna)
    elif int(A.nColumna)==int(B.nColumna):
        nColumnas=int(A.nColumna)
    else:
        nColumnas=int(B.nColumna)

    for i in range (1, nFilas+1):
        for j in range (1, nColumnas+1):
            if A.matriz.verificarExiste2(i,j) and B.matriz.verificarExiste2(i,j):
                Maux.append(i,j,"*")
            elif A.matriz.verificarExiste2(i,j):
                Maux.append(i,j,"*")
            elif B.matriz.verificarExiste2(i,j):
                Maux.append(i,j,"*")
    
    aux=dts(0,"Resultado",nFilas,nColumnas,Maux)
    preview=aux
    graficarResultado(aux)

def interseccionAB(A,B):
    global preview
    nFilas=0
    nColumnas=0
    Maux=matrizOrtogonal()
    if int(A.nFila)>int(B.nFila):
        nFilas=int(A.nFila)
    elif int(A.nFila)==int(B.nFila):
        nFilas=int(A.nFila)
    else:
        nFilas=int(B.nFila)
    
    if int(A.nColumna)>int(B.nColumna):
        nColumnas=int(A.nColumna)
    elif int(A.nColumna)==int(B.nColumna):
        nColumnas=int(A.nColumna)
    else:
        nColumnas=int(B.nColumna)

    for i in range (1, nFilas+1):
        for j in range (1, nColumnas+1):
            if A.matriz.verificarExiste2(i,j) and B.matriz.verificarExiste2(i,j):
                Maux.append(i,j,"*")
    
    aux=dts(0,"Resultado",nFilas,nColumnas,Maux)
    preview=aux
    graficarResultado(aux)

def diferenciaAB(A,B):
    global preview
    nFilas=0
    nColumnas=0
    Maux=matrizOrtogonal()
    if int(A.nFila)>int(B.nFila):
        nFilas=int(A.nFila)
    elif int(A.nFila)==int(B.nFila):
        nFilas=int(A.nFila)
    else:
        nFilas=int(B.nFila)
    
    if int(A.nColumna)>int(B.nColumna):
        nColumnas=int(A.nColumna)
    elif int(A.nColumna)==int(B.nColumna):
        nColumnas=int(A.nColumna)
    else:
        nColumnas=int(B.nColumna)

    for copia in A.matriz.iterarFilasNodos():
        Maux.append(copia.fila, copia.columna, copia.dato)

    for copia in B.matriz.iterarFilasNodos():
        if Maux.verificarExiste2(copia.fila, copia.columna):
            Maux.cambiarValor(copia.fila, copia.columna, "-")
    
    aux=dts(0,"Resultado",nFilas,nColumnas,Maux)
    preview=aux
    graficarResultado(aux)

def diferenciaSimetricaAB(A,B):
    global preview
    nFilas=0
    nColumnas=0
    Maux=matrizOrtogonal()
    if int(A.nFila)>int(B.nFila):
        nFilas=int(A.nFila)
    elif int(A.nFila)==int(B.nFila):
        nFilas=int(A.nFila)
    else:
        nFilas=int(B.nFila)
    
    if int(A.nColumna)>int(B.nColumna):
        nColumnas=int(A.nColumna)
    elif int(A.nColumna)==int(B.nColumna):
        nColumnas=int(A.nColumna)
    else:
        nColumnas=int(B.nColumna)

    for copia in A.matriz.iterarFilasNodos():
        Maux.append(copia.fila, copia.columna, copia.dato)

    for copia in B.matriz.iterarFilasNodos():
        if Maux.verificarExiste2(copia.fila, copia.columna):
            Maux.cambiarValor(copia.fila, copia.columna, "-")
        else:
            Maux.append(copia.fila, copia.columna, "*")
    aux=dts(0,"Resultado",nFilas,nColumnas,Maux)
    preview=aux
    graficarResultado(aux)

def opcionesGuardado(event):
    global combOpG
    global txtF5
    global btn2
    opcion=combOpG.get()
    o=combOp2.get()
    if opcion!="Elegir Opción" and o!="Elegir Operación":
        if opcion=="Guardar como nueva imagen":

            txtF5=Entry(barra2, font=("Consolas",9), justify=CENTER)
            txtF5.insert(0,"Ingresar nombre")
            txtF5.place(x=941, y=24, width=110, height=26)
            txtF5.bind("<Button-1>", clearTxt5)

            btn2=Button(barra2, text="Guardar", font=("Consolas",11), bg="#006266", fg="white", command=guardar)
            btn2.place(x=1061, y=24, width=75, height=28)

        if "Sustituir" in opcion:
            aux=opcion.replace("Sustituir en ","")
            id=lista.searchNombre(aux).id
            aux2=dts(id,aux,preview.nFila,preview.nColumna,preview.matriz)
            lista.modificar(aux,aux2)
            messagebox.showinfo("Proceso exitoso","Se ha sobreescrito la matriz")
            combOpG.current(0)
    else:
        messagebox.showerror("Error","No se ha elegido una operación")
    
def guardar():
    global combA
    global combB
    encontrado=False
    for buscar in lista.iterar():
        if buscar.dato.nombre==txtF5.get():
            encontrado=True
            
    if encontrado:
        messagebox.showerror("Error","Ya existe una imagen con el mismo nombre")
    else:
        aux2=dts(0,txtF5.get(),preview.nFila,preview.nColumna,preview.matriz)
        lista.append(aux2)
        messagebox.showinfo("Proceso exitoso","Imagen guardada")
        combA["values"]=(nombresM())
        combB["values"]=(nombresM())
        combM["values"]=(nombresM())
        txtF5.destroy()
        btn2.destroy()
        combOpG.current(0)

#--------------------------------------------------------------------------FIN TAB2-------------------------------------------------------------- 

def on_clossing():
    operaciones.destroy()
    from menuPrincipal import principal, setPanels, setRutas
    setRutas(rt)
    setPanels(xdPanel)
    principal()

def ventanaOperacion(ruta):
    global combM
    global lbM1
    global combOp
    global combA
    global combB
    global lbM2
    global lbM3
    global lbM4
    global lbM5
    global rt
    global barra1
    global barra2
    global combOp2
    global combOpG
    global operaciones
    datos(ruta)
    rt=ruta
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

    barra2=Frame(tab2, bg="#273c75")
    barra2.place(x=0, y=0, width=1200, height=70)

    lb1=Label(barra1, bg="#273c75", fg="white",text="Matriz:", font=("Consolas",12))
    lb1.place(x=10, y=5, width=60, height=30)

    combM=Combobox(barra1, width="20", state="readonly", font=("Consolas",10))
    combM["values"]=(nombresM())
    combM.place(x=10, y=35)
    combM.current(0)
    combM.bind("<<ComboboxSelected>>", graficarMOriginal)

    combA=Combobox(barra2, width="20", state="readonly", font=("Consolas",10))
    combA["values"]=(nombresM())
    combA.place(x=10, y=35)
    combA.current(0)
    combA.bind("<<ComboboxSelected>>", graficarA)

    combB=Combobox(barra2, width="20", state="readonly", font=("Consolas",10))
    combB["values"]=(nombresM())
    combB.place(x=200, y=35)
    combB.current(0)
    combB.bind("<<ComboboxSelected>>", graficarB)

    lb2=Label(barra1, bg="#273c75", fg="white",text="Operaciones:", font=("Consolas",12))
    lb2.place(x=200, y=5, width=115, height=30)

    combOp=Combobox(barra1, width="25", state="readonly", font=("Consolas",10), postcommand=graficarMOriginal1)
    combOp["values"]=("Elegir Operación","Rotación horizontal","Rotación vertical","Transpuesta","Limpiar zona","Agregar línea horizontal","Agregar línea vertical","Agregar rectángulo","Agregar triángulo rectángulo")
    combOp.place(x=200, y=35)
    combOp.current(0)
    combOp.bind("<<ComboboxSelected>>", graficarMModificada)

    combOp2=Combobox(barra2, width="25", state="readonly", font=("Consolas",10))
    combOp2["values"]=("Elegir Operación","Unión A, B","Intersección A, B","Diferencia A, B","Diferencia simétrica A, B")
    combOp2.place(x=390, y=35)
    combOp2.current(0)
    combOp2.bind("<<ComboboxSelected>>", resultado2img)

    combOpG=Combobox(barra2, width="25", state="readonly", font=("Consolas",10))
    combOpG["values"]=tipoGuardado()
    combOpG.place(x=610, y=35)
    combOpG.current(0)
    combOpG.bind("<<ComboboxSelected>>", opcionesGuardado)

    lb3=Label(barra2, bg="#273c75", fg="white",text="Imagen A:", font=("Consolas",12))
    lb3.place(x=10, y=5, width=80, height=30)

    lb4=Label(barra2, bg="#273c75", fg="white",text="Imagen B:", font=("Consolas",12))
    lb4.place(x=200, y=5, width=85, height=30)

    lb5=Label(barra2, bg="#273c75", fg="white",text="Operaciones:", font=("Consolas",12))
    lb5.place(x=390, y=5, width=115, height=30)

    lb6=Label(barra2, bg="#273c75", fg="white",text="Guardar:", font=("Consolas",12))
    lb6.place(x=610, y=5, width=75, height=30)

    lbM1=Label(tab1, bg="white")
    lbM1.place(x=0, y=70, width=600, height=520)

    lbM2=Label(tab1, bg="#f5f6fa")
    lbM2.place(x=600, y=70, width=600, height=520)

    lbM3=Label(tab2, bg="white")
    lbM3.place(x=0, y=70, width=400, height=520)

    lbM4=Label(tab2, bg="#f5f6fa")
    lbM4.place(x=400, y=70, width=400, height=520)

    lbM5=Label(tab2, bg="#f1f2f6")
    lbM5.place(x=800, y=70, width=400, height=520)

    identificador1=Label(tab1, bg="#40739e", text="Imagen Original",  font=("Consolas",12), fg="white")
    identificador1.place(x=0, y=590, width=600, height=30)
    
    identificador2=Label(tab1, bg="#487eb0", text="Imagen Modificada",  font=("Consolas",12), fg="white")
    identificador2.place(x=600, y=590, width=600, height=30)

    identificador3=Label(tab2, bg="#273c75", text="Imagen A",  font=("Consolas",12), fg="white")
    identificador3.place(x=0, y=590, width=400, height=30)
    
    identificador4=Label(tab2, bg="#40739e", text="Imagen B",  font=("Consolas",12), fg="white")
    identificador4.place(x=400, y=590, width=400, height=30)
    
    identificador5=Label(tab2, bg="#487eb0", text="Imagen resultante",  font=("Consolas",12), fg="white")
    identificador5.place(x=800, y=590, width=400, height=30)

    resetear=Button(tab1, text="Reset", font=("Consolas",11), bg="#006266", fg="white", command=reset)
    resetear.place(x=1110, y=24, width=65, height=28)

    operaciones.protocol("WM_DELETE_WINDOW", on_clossing)
    operaciones.mainloop()

'''
rutasss=linked_list()
rutasss.append("Archivos_Prueba/entrada.xml")
ventanaOperacion(rutasss)
'''