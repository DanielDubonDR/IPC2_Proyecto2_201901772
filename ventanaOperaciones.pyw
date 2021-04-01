from tkinter import *
from tkinter.ttk import Notebook, Combobox
from PIL import Image, ImageTk
from Estructuras.MOrtogonal import matrizOrtogonal
from Funciones.LeerXML import ExtraerXML
from Funciones.Graficar import graficarM
from tkinter import messagebox

lista=None
listaCopia=None
combM=None
combOp=None
lbM1=None
lbM2=None
txtF1=None
txtF2=None
txtF3=None
txtF4=None
action=None
lbT=None
barra1=None
rt=""

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

def changeHorizontal(aux):
    #listaCopia.searchNombre("M1").matriz.append(2,2,"*")
    #listaCopia.searchNombre("M1").matriz.cambiarValor(2,2,"*") 
    matrizAux=matrizOrtogonal()
    filas=int(aux.nFila)
    for i in range(1,filas+1):
        for j in range(1,int(aux.nColumna)+1):
            if aux.matriz.verificarExiste(i,j):
                nuevo=filas-(i-1)
                matrizAux.append(nuevo,j,"*")
    aux.matriz=matrizAux

def changeVertical(aux): 
    matrizAux=matrizOrtogonal()
    filas=int(aux.nFila)
    columnas=int(aux.nColumna)
    for i in range(1,filas+1):
        for j in range(1,columnas+1):
            if aux.matriz.verificarExiste(i,j):
                nuevo=columnas-(j-1)
                matrizAux.append(i,nuevo,"*")
    aux.matriz=matrizAux

def changeTranspuesta(aux): 
    matrizAux=matrizOrtogonal()
    filas=int(aux.nFila)
    columnas=int(aux.nColumna)
    for i in range(1,filas+1):
        for j in range(1,columnas+1):
            if aux.matriz.verificarExiste(i,j):
                matrizAux.append(j,i,"*")
    aux.matriz=matrizAux

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

def destruirComponentes():
    txtF1.destroy()
    txtF2.destroy()
    txtF3.destroy()
    txtF4.destroy()
    lbT.destroy()
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
    txtF2.place(x=832, y=24, width=55, height=26)
    txtF2.bind("<Button-1>", clearTxt2)

    lbT=Label(barra1, bg="#273c75", fg="white",text="hasta", font=("Consolas",11))
    lbT.place(x=892, y=24, width=50, height=26)

    txtF3=Entry(barra1, font=("Consolas",10), justify=CENTER)
    txtF3.insert(0,"Columna")
    txtF3.place(x=948, y=24, width=55, height=26)
    txtF3.bind("<Button-1>", clearTxt3)

    action=Button(barra1, text="Agregar", font=("Consolas",11), bg="#006266", fg="white", command=addLnH)
    action.place(x=1025, y=24, width=75, height=28)

def limpiarZona():
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
    combOp.current(0)
    destruirComponentes()

def addLnH():
    f1=txtF1.get()
    c1=txtF2.get()
    c2=txtF3.get()
    if f1.isnumeric() and c1.isnumeric() and c2.isnumeric():
        for j in range(int(c1),int(c2)+1):
            if lista.searchNombre(combM.get()).matriz.verificarExiste(int(f1),j):
                lista.searchNombre(combM.get()).matriz.cambiarValor(int(f1),j,"*")
            else:
                lista.searchNombre(combM.get()).matriz.append(int(f1),j,"*")
        graficarEnM2(combM.get())
    else:
        messagebox.showerror("Error","Formato incorrecto")
    combOp.current(0)
    txtF1.destroy()
    txtF2.destroy()
    txtF3.destroy()
    lbT.destroy()
    action.destroy()

def graficarMOriginal1():
    global combM
    global lbM1
    global lbM2
    lbM2.configure(image="")
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


def ventanaOperacion(ruta):
    global combM
    global lbM1
    global combOp
    global lbM2
    global rt
    global barra1
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

    lb1=Label(barra1, bg="#273c75", fg="white",text="Matriz:", font=("Consolas",12))
    lb1.place(x=10, y=5, width=60, height=30)

    combM=Combobox(barra1, width="20", state="readonly", font=("Consolas",10))
    combM["values"]=(nombresM())
    combM.place(x=10, y=35)
    combM.current(0)
    combM.bind("<<ComboboxSelected>>", graficarMOriginal)

    lb2=Label(barra1, bg="#273c75", fg="white",text="Operaciones:", font=("Consolas",12))
    lb2.place(x=200, y=5, width=115, height=30)

    combOp=Combobox(barra1, width="20", state="readonly", font=("Consolas",10), postcommand=graficarMOriginal1)
    combOp["values"]=("Elegir Operación","Rotación horizontal","Rotación vertical","Transpuesta","Limpiar zona","Agregar línea horizontal","Agregar linea vertical","Agregar rectángulo","Agregar triangulo rectangulo")
    combOp.place(x=200, y=35)
    combOp.current(0)
    combOp.bind("<<ComboboxSelected>>", graficarMModificada)

    lbM1=Label(tab1, bg="white")
    lbM1.place(x=0, y=70, width=600, height=520)

    lbM2=Label(tab1, bg="#f5f6fa")
    lbM2.place(x=600, y=70, width=600, height=520)

    identificador1=Label(tab1, bg="#40739e", text="Imagen Original",  font=("Consolas",12), fg="white")
    identificador1.place(x=0, y=590, width=600, height=30)
    
    identificador2=Label(tab1, bg="#487eb0", text="Imagen Modificada",  font=("Consolas",12), fg="white")
    identificador2.place(x=600, y=590, width=600, height=30)

    resetear=Button(tab1, text="Reset", font=("Consolas",11), bg="#006266", fg="white", command=reset)
    resetear.place(x=1110, y=24, width=65, height=28)

    operaciones.mainloop()

ventanaOperacion("Archivos_Prueba/entrada.xml")
