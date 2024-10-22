#Pizzeria en python

import tkinter as tk
from PIL import Image, ImageTk

# window

root = tk.Tk("Pizzeria")
root.config(bg="orange", )
root.geometry("3600x1200")
root.title("Voglio la pizza")
root.grid_propagate(False)

# Frames

frame1 = tk.Frame(bg="#d66439", height=500, width=500, border=20, relief="groove")
frame1.grid(row=0, column=0, pady=150, padx=(10,0))
frame1.grid_propagate(False)

frame2 = tk.Frame(bg="#de2605", height=500, width=500, border=20, relief="groove")
frame2.grid(row=0, column=1, pady=150)
frame2.grid_propagate(False)

frame3 = tk.Frame(bg="#f16e56", height=500, width=500, border=20, relief="groove")
frame3.grid(row=0, column=2, pady=150)
frame3.grid_propagate(False)

#LOGICA DEL FRAME #1

subFrame1 = tk.Frame(frame1, width=100, height=50, bg="gray", border=20, relief="sunken")
subFrame1.grid(row=0, column=0, padx=(15,0))

subFrame2 = tk.Frame(frame1, width=400, height=300, highlightbackground="black", highlightthickness=1, bg="white", border="10")
subFrame2.grid(row=1, column=0, padx=(25,25))
subFrame2.grid_propagate(False)

labelFactura = tk.Label(subFrame2, text="Factura", bg="white", font=("Helvetica", 20, "bold"))
labelFactura.grid(row=0, column=0, padx=(140,0))

subFrame3 = tk.Frame(frame1, width=400, height=100, highlightbackground="black", highlightthickness=1,  bg="white", border="10")
subFrame3.grid(row=2, column=0, padx=(25,25))
subFrame3.grid_propagate(False)

subLabelSubTotal = tk.Label(subFrame3, bg="white",text="SubTotal", font=("Helvetica", 12, "bold"))
subLabelSubTotal.grid(row=0, column=0)

subLabelDescuento = tk.Label(subFrame3, bg="white",text="Descuento", font=("Helvetica", 12, "bold"))
subLabelDescuento.grid(row=1, column=0, pady=(5,5))

sublabelTotal= tk.Label(subFrame3, bg="white",text="Total", font=("Helvetica", 12, "bold") )
sublabelTotal.grid(row=2, column=0)


labelNumTotal = tk.Label(subFrame3, text="$100", font=("Helvetica", 12, "bold"))
labelDescuento = tk.Label(subFrame3, text="$20", font=("Helvetica", 12, "bold"))
labelNumSubTotal = tk.Label(subFrame3, text="$80", font=("Helvetica", 12, "bold"))

labelNumTotal.grid(row=0, column=1)
labelDescuento.grid(row=1, column=1)
labelNumSubTotal.grid(row=2, column=1)

#LOGICA DEL FRAME #3


#Radiobuttons

eleccion = tk.IntVar()
eleccion.set(0)


radio1 = tk.Radiobutton(frame3, bg="#f16e56", text="Personal", variable=eleccion, value=10, width=10,
            font=("Helvetica", 16, "bold"), activebackground="#f16e56")

radio2 = tk.Radiobutton(frame3, bg="#f16e56", text="Mediana ", variable=eleccion, value=15, width=10,
            font=("Helvetica", 16, "bold"), activebackground="#f16e56")


radio3 = tk.Radiobutton(frame3, bg="#f16e56", text="Grande   ", variable=eleccion, value=20, width=10,
            font=("Helvetica", 16, "bold"), activebackground="#f16e56")


radio4 = tk.Radiobutton(frame3, bg="#f16e56", text="Familiar  ", variable=eleccion, value=25, width=10,
            font=("Helvetica", 16, "bold"), activebackground="#f16e56")

radio1.grid(row=2, column=0,pady=(15,0))
radio2.grid(row=3, column=0)
radio3.grid(row=4, column=0)
radio4.grid(row=5, column=0)



#labels

checkVariable1=tk.IntVar()
checkVariable2=tk.IntVar()
checkVariable3=tk.IntVar()
checkVariable4=tk.IntVar()
checkVariable5=tk.IntVar()
checkVariable6=tk.IntVar()

label1 = tk.Label(frame3, text="Ordene su pizza:\n", font=("Helvetica", 16, "bold"), bg="#f16e56")
label1.grid(row=0,column=3)

label2 = tk.Label(frame3, text="Tamaño:", font=("Helvetica", 16, "bold"), bg="#f16e56")
label2.grid(row=1,column=0)

label3 = tk.Label(frame3, text="\n$10.00", font=("Helvetica", 16, "bold"), bg="#f16e56")
label3.grid(row=2,column=5)

label4 = tk.Label(frame3, text="$15.00", font=("Helvetica", 16, "bold"), bg="#f16e56")
label4.grid(row=3,column=5)

label5 = tk.Label(frame3, text="$20.00", font=("Helvetica", 16, "bold"), bg="#f16e56")
label5.grid(row=4,column=5)

label6 = tk.Label(frame3, text="$25.00", font=("Helvetica", 16, "bold"), bg="#f16e56")
label6.grid(row=5,column=5)


label7 = tk.Label(frame3, text="Ingredientes:", font=("Helvetica", 16, "bold"), bg="#f16e56")
label7.grid(row=6,column=0, pady=(3,0))

#Ingredientes usando checkbox

#FUNCION PARA CHEQUEAR LOS CHECKKBUTTONS   

checkbutton1 = tk.Checkbutton(frame3, text="Queso    ", font=("Helvetica", 12, "bold"), bg="#f16e56",
                activebackground="#f16e56", variable=checkVariable1, 
                command=lambda: sumarContador(checkVariable1, 3))
checkbutton1.grid(row=7, column=0)

checkbutton2 = tk.Checkbutton(frame3, text="Pepperoni", font=("Helvetica", 12, "bold"), bg="#f16e56",
                activebackground="#f16e56", variable=checkVariable2, 
                command=lambda: sumarContador(checkVariable2, 3))
checkbutton2.grid(row=8, column=0, padx=(10,0))

checkbutton3 = tk.Checkbutton(frame3, text="Jamon", font=("Helvetica", 12, "bold"), bg="#f16e56",
                activebackground="#f16e56", variable=checkVariable3, 
                command=lambda: sumarContador(checkVariable3, 3))
checkbutton3.grid(row=9, column=0, padx=(0,15))

checkbutton4 = tk.Checkbutton(frame3, text="Pollo", font=("Helvetica", 12, "bold"), bg="#f16e56",
                activebackground="#f16e56", variable=checkVariable4,
                command=lambda: sumarContador(checkVariable4, 3))    
checkbutton4.grid(row=10, column=0, padx=(0, 30))

checkbutton5 = tk.Checkbutton(frame3, text="Tocino    ", font=("Helvetica", 12, "bold"), bg="#f16e56",
                activebackground="#f16e56", variable=checkVariable5,
                command=lambda: sumarContador(checkVariable5, 3))    
checkbutton5.grid(row=11, column=0)

checkbutton6 = tk.Checkbutton(frame3, text="Salsa Chipotle", font=("Helvetica", 12, "bold"), bg="#f16e56",
                activebackground="#f16e56", variable=checkVariable6,
                command=lambda: sumarContador(checkVariable6, 3))    
checkbutton6.grid(row=12, column=0, padx=(40,0))

#ubicacion de los labels de los precios de los ingredientes


label7 = tk.Label(frame3, text="$1.00", font=("Helvetica", 16, "bold"), bg="#f16e56")
label7.grid(row=7,column=5)

label8 = tk.Label(frame3, text="$1.50", font=("Helvetica", 16, "bold"), bg="#f16e56")
label8.grid(row=8,column=5)

label9 = tk.Label(frame3, text="$1.25", font=("Helvetica", 16, "bold"), bg="#f16e56")
label9.grid(row=9,column=5)

label10 = tk.Label(frame3, text="$1.75", font=("Helvetica", 16, "bold"), bg="#f16e56")
label10.grid(row=10,column=5)

label11 = tk.Label(frame3, text="$1.10", font=("Helvetica", 16, "bold"), bg="#f16e56")
label11.grid(row=11,column=5)

label12 = tk.Label(frame3, text="$2.75", font=("Helvetica", 16, "bold"), bg="#f16e56")
label12.grid(row=12,column=5)


rowPedidos=0
columnPedidos=0

checkVariables = [checkVariable1, checkVariable2, checkVariable3, checkVariable4, checkVariable5, checkVariable6]
checkBotones = [checkbutton1, checkbutton2, checkbutton3, checkbutton4, checkbutton5, checkbutton6]
contenedor = []

def sumarContador(checkVariable, n):

    #la variable contador ayudara a mantener el control de que sean unicamente 3 checkbuttons
    # se vera mas adelante esta logica
    
    global contador
    global contenedor
    #checkBotones = [checkbutton1, checkbutton2, checkbutton3, checkbutton4]
   
    if(checkVariable.get() == 1 ):
        print(f"Entro boton #{checkVariables.index(checkVariable)+1}")
        contenedor.append(checkBotones[checkVariables.index(checkVariable)])
    else:
        print(f"Se apago boton #{checkVariables.index(checkVariable)+1}")
        contenedor.pop(contenedor.index(checkBotones[checkVariables.index(checkVariable)]))
            

    if(len(contenedor) == n):
        for i in checkBotones:
            if(i not in contenedor):
                i.config(state="disabled")
                
    else:
        for i in checkBotones:
            if(i.config(state="normal") == "normal"):
                print(f"Boton {i}")


def combo1(variableCombo):

    global contenedor

    if variableCombo.get() == 1:

        
        contenedor=[]
        variableCombo2.set(0)

        #Limpiamos los botones para evitar errores

        checkVariable3.set(0)
        checkVariable4.set(0)
        checkVariable5.set(0)

        checkVariable1.set(1)
        sumarContador(checkVariable1, 3)
        checkVariable2.set(1)
        sumarContador(checkVariable2, 3)
        checkVariable6.set(1)
        sumarContador(checkVariable6, 3)

        eleccion.set(20)

    else:

        contenedor=[]

        eleccion.set(0)

        checkVariable1.set(0)
       
        checkVariable2.set(0)
        
        checkVariable6.set(0)

        checkbutton3.config(state="normal")
        checkbutton4.config(state="normal")
        checkbutton5.config(state="normal")

        
def combo2(variableCombo):

    global contenedor

    if variableCombo.get() == 1:

        variableCombo1.set(0)
        contenedor=[]

        #Limpiamos los botones para evitar errores

        checkVariable3.set(0)
        checkVariable4.set(0)
        checkVariable6.set(0)

        checkVariable1.set(1)
        sumarContador(checkVariable1, 3)
        checkVariable2.set(1)
        sumarContador(checkVariable2, 3)
        checkVariable5.set(1)
        sumarContador(checkVariable5, 3)

        eleccion.set(15)

    else:

        contenedor=[]

        eleccion.set(0)

        checkVariable1.set(0)
       
        checkVariable2.set(0)
        
        checkVariable5.set(0)

        checkbutton3.config(state="normal")
        checkbutton4.config(state="normal")
        checkbutton6.config(state="normal")
        

total = 0

#FUNCION PARA LOS PEDIDOS

def pedidos():

    global radios
    global rowPedidos
    global columnPedidos
    global total

    total = eleccion.get()

    pedido=tk.Label(subFrame2, text=f"Pedido#{rowPedidos+1}", font=("Helvetica", 16, "bold"))
    pedido.grid(row=rowPedidos, column=columnPedidos)
    rowPedidos+=1
    totalLabel = tk.Label(subFrame2, text=f'Total={total}', font=("Helvetica", 16, "bold"))
    totalLabel.grid(row=0, column=1, )



#LOGICA DEL FRAME #2


# Cargar imagenes 
image1_path = "combo1.png"
image2_path = "combo2.png"
image1 = Image.open(image1_path)
image2 = Image.open(image2_path)

# Redimensionar la imagen si es necesario
image1 = image1.resize((200, 200))
image2 = image2.resize((200, 200))  

# Convertir la imagen para que Tkinter pueda usarla
tk_image1 = ImageTk.PhotoImage(image1)
tk_image2 = ImageTk.PhotoImage(image2)

# Crear un label y asignar la imagen
labelImagen = tk.Label(frame2, image=tk_image1)
labelImagen.grid(row=0, column=0, padx=(25,0), pady=(5,50))
labelImagen.grid_propagate(False)

labelImagen2 = tk.Label(frame2, image=tk_image2)
labelImagen2.grid(row=0, column=1, padx=(5,0),pady=(5,50))
labelImagen2.grid_propagate(False)


#labelEspacio = tk.Label(frame2, bg="white")
#labelEspacio.grid(row=1, column=0)

labelCantPizzas= tk.Label(frame2, text="Cantidad:", font=("Helvetica", 16, "bold"), 
                          border=1, relief="ridge",bg="light coral")
labelCantPizzas.grid(row=2, column=0)

#FUNCION PARA SOLO PERMITIR ENTEROS DE LONGITUD N 
def limitEntradas(n):
    def validarEntrada(texto):
        # Comprueba que el texto sea numérico y que la longitud no exceda 3 caracteres
        if texto.isdigit() and len(texto) <= n:
            return True
        elif texto == "":  # Permitir borrar todo el texto
            return True
        else:
            return False
    return validarEntrada

validacion =root.register(limitEntradas(1))

cantPizzas = tk.Entry(frame2, width=3, validate="key", validatecommand=(validacion, '%P'), 
                      bg="light coral", font=("Helvetica", 12, "bold"))
cantPizzas.grid(row=2, column=1)

variableCombo1 = tk.IntVar()
variableCombo2 = tk.IntVar()

checkCombo1 = tk.Checkbutton(frame2, text="Combo 1",border=5, 
    relief="ridge", variable=variableCombo1, command=lambda: combo1(variableCombo1), font=("Helvetica", 12, "bold"), bg="light coral", activebackground="#f16e56")
checkCombo1.grid(row=3, column=0, pady=(50,0))

checkCombo2 = tk.Checkbutton(frame2, text="Combo 2",border=5, relief="ridge", 
    font=("Helvetica", 12, "bold"), variable=variableCombo2, command= lambda: combo2(variableCombo2), bg="light coral", activebackground="#f16e56")
checkCombo2.grid(row=3, column=1, pady=(50,0))

buttonAgregar = tk.Button(frame2, text="Agregar", bg="light coral",border=5, relief="ridge", font=("Helvetica", 16, "bold"),
                          activebackground="#f16e56", command=pedidos)
buttonAgregar.grid(row=4, column=1, pady=(20,0))

#Corre en bucle el programa 
root.mainloop()