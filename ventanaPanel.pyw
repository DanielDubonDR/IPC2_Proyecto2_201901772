from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

lbM1=None
lbM2=None
operaciones=None
dtsPanel=None
lbM3=None
lbM4=None
lbM5=None

def on_clossing():
    operaciones.destroy()
    from menuPrincipal import principal, setPanels
    setPanels(dtsPanel)
    principal()

def graficarMOriginal1(m):
    global lbM2
    imgCargar=Image.open("Imagenes/"+str(m.m1)+".png")
    ancho=imgCargar.size[0]
    alto=imgCargar.size[1]
    if ancho<600 and alto<520:
        imgCargar=ImageTk.PhotoImage(imgCargar)
        lbM2.configure(image=imgCargar)
        lbM2.image=imgCargar
    elif ancho>alto:
        restar=ancho-600
        if (alto-restar)>520:
            restar=alto-520
            imgCargar=imgCargar.resize((ancho-restar,alto-restar))
            imgCargar=ImageTk.PhotoImage(imgCargar)
            lbM2.configure(image=imgCargar)
            lbM2.image=imgCargar
        else:
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
            if (ancho-restar)>600:
                restar=ancho-600
                imgCargar=imgCargar.resize((ancho-restar,alto-restar))
                imgCargar=ImageTk.PhotoImage(imgCargar)
                lbM2.configure(image=imgCargar)
                lbM2.image=imgCargar
            else:
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

def graficarMOriginal(m):
    global lbM1

    imgCargar=Image.open("Imagenes/"+str(m.m1)+"_Original.png")
    ancho=imgCargar.size[0]
    alto=imgCargar.size[1]
    if ancho<600 and alto<520:
        imgCargar=ImageTk.PhotoImage(imgCargar)
        lbM1.configure(image=imgCargar)
        lbM1.image=imgCargar
    elif ancho>alto:
        restar=ancho-600
        if (alto-restar)>520:
            restar=alto-520
            imgCargar=imgCargar.resize((ancho-restar,alto-restar))
            imgCargar=ImageTk.PhotoImage(imgCargar)
            lbM1.configure(image=imgCargar)
            lbM1.image=imgCargar
        else:
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
        if (ancho-restar)>600:
            restar=ancho-600
            imgCargar=imgCargar.resize((ancho-restar,alto-restar))
            imgCargar=ImageTk.PhotoImage(imgCargar)
            lbM1.configure(image=imgCargar)
            lbM1.image=imgCargar
        else:
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

def graficarA(m):
    global lbM3
    imgCargar=Image.open("Imagenes/"+str(m.m1)+".png")
    ancho=imgCargar.size[0]
    alto=imgCargar.size[1]
    if ancho<400 and alto<520:
        imgCargar=ImageTk.PhotoImage(imgCargar)
        lbM3.configure(image=imgCargar)
        lbM3.image=imgCargar
    elif ancho>alto:
        restar=ancho-400
        if (alto-restar)>520:
            restar=alto-520
            imgCargar=imgCargar.resize((ancho-restar,alto-restar))
            imgCargar=ImageTk.PhotoImage(imgCargar)
            lbM3.configure(image=imgCargar)
            lbM3.image=imgCargar
        else:
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
        if (ancho-restar)>400:
            restar=ancho-400
            imgCargar=imgCargar.resize((ancho-restar,alto-restar))
            imgCargar=ImageTk.PhotoImage(imgCargar)
            lbM3.configure(image=imgCargar)
            lbM3.image=imgCargar
        else:
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

def graficarB(m):
    global lbM4
    imgCargar=Image.open("Imagenes/"+str(m.m2)+".png")
    ancho=imgCargar.size[0]
    alto=imgCargar.size[1]
    if ancho<400 and alto<520:
        imgCargar=ImageTk.PhotoImage(imgCargar)
        lbM4.configure(image=imgCargar)
        lbM4.image=imgCargar
    elif ancho>alto:
        restar=ancho-400
        if (alto-restar)>520:
            restar=alto-520
            imgCargar=imgCargar.resize((ancho-restar,alto-restar))
            imgCargar=ImageTk.PhotoImage(imgCargar)
            lbM4.configure(image=imgCargar)
            lbM4.image=imgCargar
        else:
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
        if (ancho-restar)>400:
            restar=ancho-400
            imgCargar=imgCargar.resize((ancho-restar,alto-restar))
            imgCargar=ImageTk.PhotoImage(imgCargar)
            lbM4.configure(image=imgCargar)
            lbM4.image=imgCargar
        else:
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

def graficarC():
    global lbM5
    imgCargar=Image.open("Imagenes/Resultado.png")
    ancho=imgCargar.size[0]
    alto=imgCargar.size[1]
    if ancho<400 and alto<520:
        imgCargar=ImageTk.PhotoImage(imgCargar)
        lbM5.configure(image=imgCargar)
        lbM5.image=imgCargar
    elif ancho>alto:
        restar=ancho-400
        if (alto-restar)>520:
            restar=alto-520
            imgCargar=imgCargar.resize((ancho-restar,alto-restar))
            imgCargar=ImageTk.PhotoImage(imgCargar)
            lbM5.configure(image=imgCargar)
            lbM5.image=imgCargar
        else:
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
        if (ancho-restar)>400:
            restar=ancho-400
            imgCargar=imgCargar.resize((ancho-restar,alto-restar))
            imgCargar=ImageTk.PhotoImage(imgCargar)
            lbM5.configure(image=imgCargar)
            lbM5.image=imgCargar
        else:
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

def m1(dato):
    global lbM1
    global lbM2
    global operaciones
    global dtsPanel
    dtsPanel=dato
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

    lb2=Label(barra1, bg="#273c75", fg="white",text=dato.operacion, font=("Consolas",11), justify=RIGHT)
    lb2.place(x=240, y=20, width=300, height=30)


    lbM1=Label(operaciones, bg="white")
    lbM1.place(x=0, y=70, width=600, height=520)

    lbM2=Label(operaciones, bg="#f5f6fa")
    lbM2.place(x=600, y=70, width=600, height=520)


    identificador1=Label(operaciones, bg="#40739e", text="Imagen Original",  font=("Consolas",12), fg="white")
    identificador1.place(x=0, y=590, width=600, height=30)
    
    identificador2=Label(operaciones, bg="#487eb0", text="Imagen Resultante",  font=("Consolas",12), fg="white")
    identificador2.place(x=600, y=590, width=600, height=30)

    graficarMOriginal(dato)
    graficarMOriginal1(dato)
    operaciones.protocol("WM_DELETE_WINDOW", on_clossing)
    operaciones.mainloop()

def m2(dato):
    global operaciones
    global dtsPanel
    global lbM3
    global lbM4
    global lbM5
    dtsPanel=dato
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

    lb2=Label(barra1, bg="#273c75", fg="white",text=dato.operacion, font=("Consolas",11), justify=RIGHT)
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

    graficarA(dato)
    graficarB(dato)
    graficarC()

    operaciones.protocol("WM_DELETE_WINDOW", on_clossing)
    operaciones.mainloop()
