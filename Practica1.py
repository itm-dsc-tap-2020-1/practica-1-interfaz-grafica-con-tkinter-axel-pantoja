import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox

def impExtras():
    a=opcion_1.get()
    b=opcion_2.get()
    c=opcion_3.get()
    d=opcion.get()
    e=objVida.get()
    x=0
    y=0
    z=0
    x1="NO"
    x2="NO"
    x3="NO"
    if a != 0 : 
        x=1 
        x1="SI"
    if b != 0: 
        x=1  
        x2="SI"
    if c != 0: 
        x=1  
        x3="SI"
    if d ==1 or d ==2 or d ==3 : y=1
    if e !="": z=1
    if d==1: es="Soltero"
    elif d==2: es="Casado"
    elif d==3: es="Viudo"
    if x and y and z ==1:
        mBox.showinfo(message=("PASATIEMPOS: \nLeer: " + x1 +"\nPeliculas: "+ x2 +"\nRedes Sociales: "+ x3 +"\nESTADO CIVIL: "+ es+"\nOBJETIVO DE VIDA: "+ e ),title="Datos extras")
    else : mBox.showinfo(message=("Campos incompletos"),title="Error")
def impDatos():
    a=nombre.get()
    b=apeP.get()
    c=apeM.get()
    d=direc.get()
    e=col.get()
    f=ciudad.get()
    g=mun.get()
    x=0
    y=0
    z=0
    x1=0
    y1=0
    z1=0
    x2=0
    if a != "" : x=1
    if b != "": y=1
    if c != "": z=1
    if d != "": x1=1
    if e != "": y1=1
    if f != "": z1=1
    if g != "": x2=1
    if x and y and z and x1 and y1 and z1 and x2 ==1:
        mBox.showinfo(message=("NOMBRE: "+a+"\nAPELLIDO P: "+ b+"\nAPELLIDO M: "+c+"\nDIRECCION: "+d+"\nCOLONIA: "+e+"\nCIUDAD: "+f+"\nMUNICIPIO: "+g),title="Datos personales")
    else : mBox.showinfo(message=("Campos incompletos"),title="Error")
def funcion_salir():
    ventana.quit()
    ventana.destroy()
    exit()
def impG():
    a=opcion_1.get()
    b=opcion_2.get()
    c=opcion_3.get()
    d=opcion.get()
    e=objVida.get()
    x=0
    y=0
    z=0
    x1="NO"
    x2="NO"
    x3="NO"
    if a != 0 : 
        x=1 
        x1="SI"
    if b != 0: 
        x=1  
        x2="SI"
    if c != 0: 
        x=1  
        x3="SI"
    if d ==1 or d ==2 or d ==3 : y=1
    if e !="": z=1
    if d==1: es="Soltero"
    elif d==2: es="Casado"
    elif d==3: es="Viudo"
    a=nombre.get()
    b=apeP.get()
    c=apeM.get()
    d=direc.get()
    ee=col.get()
    f=ciudad.get()
    g=mun.get()
    xx=0
    yy=0
    zz=0
    xx1=0
    yy1=0
    zz1=0
    xx2=0
    if a != "" : xx=1
    if b != "": yy=1
    if c != "": zz=1
    if d != "": xx1=1
    if e != "": yy1=1
    if f != "": zz1=1
    if g != "": xx2=1
    if xx and yy and zz and x and y and z and xx1 and yy1 and zz1 and xx2 ==1:
        mBox.showinfo(message=("NOMBRE: "+a+"\nAPELLIDO P: "+ b+"\nAPELLIDO M: "+c+"\nDIRECCION: "+d+"\nCOLONIA: "+ee+"\nCIUDAD: "+f+"\nMUNICIPIO: "+g+"\nPASATIEMPOS: \nLeer: " + x1 +"\nPeliculas: "+ x2 +"\nRedes Sociales: "+ x3 +"\nESTADO CIVIL: "+ es+"\nOBJETIVO DE VIDA: "+ e  ),title="Datos generales")
    else : mBox.showinfo(message=("Campos incompletos"),title="Error")
def acer():
    mBox.showinfo(message="Sistema creado para la practica 1 \nFebrero 2020 \nAxel Leonardo Pantoja Alfaro",title="Información")

ventana=tk.Tk()
ventana.title("Sistema Escolar")
barra_menu=Menu(ventana)
ventana.config(menu=barra_menu)
opciones_menu=Menu(barra_menu)
opciones_menu.add_command(label="Imprimir",command=impG)
opciones_menu.add_separator()
opciones_menu.add_command(label="Salir",command=funcion_salir)
barra_menu.add_cascade(label="Sistema", menu=opciones_menu)
menu_ayuda=Menu(barra_menu,tearoff=0)
menu_ayuda.add_command(label="Acerca de",command=acer)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)
tabControl=ttk.Notebook(ventana)
tab1=ttk.Frame(tabControl)
tabControl.add(tab1,text='Datos Personales')
tabControl.grid(column=0,row=0)
tab2=ttk.Frame(tabControl)
tabControl.add(tab2,text='Extras')
ttk.Label(tab1, text="Nombre").grid(column=0,row=1)
nombre=tk.StringVar()
nombreCapturado=ttk.Entry(tab1, width=12, textvariable=nombre)
nombreCapturado.grid(column=1,row=1)
ttk.Label(tab1, text="Apellido Paterno").grid(column=0,row=2)
apeP=tk.StringVar()
apePCapturado=ttk.Entry(tab1, width=12, textvariable=apeP)
apePCapturado.grid(column=1,row=2)
ttk.Label(tab1, text="Apellido Materno").grid(column=0,row=3)
apeM=tk.StringVar()
apeMCapturado=ttk.Entry(tab1, width=12, textvariable=apeM)
apeMCapturado.grid(column=1,row=3)
ttk.Label(tab1, text="Direccion").grid(column=0,row=4)
direc=tk.StringVar()
direcCapturado=ttk.Entry(tab1, width=12, textvariable=direc)
direcCapturado.grid(column=1,row=4)
ttk.Label(tab1, text="Colonia:").grid(column=0,row=5)
col=tk.StringVar()
colSeleccionado=ttk.Combobox(tab1, width=12, textvariable=col)
colSeleccionado['values']=("Centro","Obrera","Americas")
colSeleccionado.grid(column=1, row=5)
ttk.Label(tab1, text="Ciudad:").grid(column=0,row=6)
ciudad=tk.StringVar()
ciuSeleccionado=ttk.Combobox(tab1, width=12, textvariable=ciudad)
ciuSeleccionado['values']=("Morelia","Leon","Monterrey")
ciuSeleccionado.grid(column=1, row=6)
ttk.Label(tab1, text="Municipio:").grid(column=0,row=7)
mun=tk.StringVar()
munSeleccionado=ttk.Combobox(tab1, width=12, textvariable=mun)
munSeleccionado['values']=("Charo","Zinapecuaro","Apatzingan")
munSeleccionado.grid(column=1, row=7)
accion=ttk.Button(tab1,text="Imprimir",command=impDatos)
accion.grid(column=2,row=8)
ttk.Label(tab2, text="Pasatiempos").grid(column=0,row=0)
opcion_1=tk.IntVar()
casilla_1=tk.Checkbutton(tab2, text="Leer", variable=opcion_1)
casilla_1.grid(column=0,row=1,sticky=tk.W)
opcion_2=tk.IntVar()
casilla_2=tk.Checkbutton(tab2, text="Peliculas", variable=opcion_2)
casilla_2.grid(column=1,row=1,sticky=tk.W)
opcion_3=tk.IntVar()
casilla_3=tk.Checkbutton(tab2, text="Redes Sociales", variable=opcion_3)
casilla_3.grid(column=2,row=1,sticky=tk.W)
ttk.Label(tab2, text="Estado Civil").grid(column=0,row=2)
opcion=tk.IntVar()
radio1=tk.Radiobutton(tab2,text="Soltero",variable=opcion,value=1)
radio1.grid(column=0,row=3,sticky=tk.W)
radio2=tk.Radiobutton(tab2,text="Casado",variable=opcion,value=2)
radio2.grid(column=1,row=3,sticky=tk.W)
radio3=tk.Radiobutton(tab2,text="Viudo",variable=opcion,value=3)
radio3.grid(column=2,row=3,sticky=tk.W)
ttk.Label(tab2, text="Objetivo de vida").grid(column=0,row=4)
objVida=ttk.Entry(tab2, width=16,validate="key")
objVida.grid(column=0,row=5)
accion2=ttk.Button(tab2,text="Imprimir",command=impExtras)
accion2.grid(column=2,row=6)
ventana.mainloop()