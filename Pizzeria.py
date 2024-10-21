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

frame1 = tk.Frame(bg="#933b2a", height=500, width=500, border=20, relief="groove")
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

subFrame2 = tk.Frame(frame1, width=400, height=300,bg="white", border="10")
subFrame2.grid(row=1, column=0, padx=(25,25))
subFrame2.grid_propagate(False)

subFrame3 = tk.Frame(frame1, width=400, height=100, highlightbackground="black",  bg="#ffd9d2", border="10")
subFrame3.grid(row=2, column=0, padx=(25,25))
subFrame3.grid_propagate(False)

subLabelSubTotal = tk.Label(subFrame3, text="subTotal", font=("Helvetica", 8, "bold"))
subLabelSubTotal.grid(row=0, column=0)

subLabelDescuento = tk.Label(subFrame3, text="Descuento", font=("Helvetica", 8, "bold"))
subLabelDescuento.grid(row=1, column=0, pady=(5,5))

sublabelTotal= tk.Label(subFrame3, text="Total", font=("Helvetica", 8, "bold") )
sublabelTotal.grid(row=2, column=0)


labelNumTotal = tk.Label(subFrame3, text="$100")
labelDescuento = tk.Label(subFrame3, text="$20")
labelNumSubTotal = tk.Label(subFrame3, text="$80")

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


label7 = tk.Label(frame3, text="\nIngredientes:\n", font=("Helvetica", 16, "bold"), bg="#f16e56")
label7.grid(row=6,column=0)

#Ingredientes usando checkbox
contador=0
def sumarContador(variableCheck):

    #la variable contador ayudara a mantener el control de que sean unicamente 3 checkbuttons
    # se vera mas adelante esta logica
    
    global contador
    if variableCheck.get() == 1:
        contador=1
    else:
        contador=0
    print(contador)


checkbutton1 = tk.Checkbutton(frame3, text="Queso    ", font=("Helvetica", 12, "bold"), bg="#f16e56",
                activebackground="#f16e56", variable=checkVariable1, command=lambda: sumarContador(checkVariable1))
checkbutton1.grid(row=7, column=0)

checkbutton2 = tk.Checkbutton(frame3, text="Pepperoni", font=("Helvetica", 12, "bold"), bg="#f16e56",
                activebackground="#f16e56", variable=checkVariable2, command=lambda: sumarContador(checkVariable2))
checkbutton2.grid(row=8, column=0, padx=(10,0))

checkbutton3 = tk.Checkbutton(frame3, text="Jamon", font=("Helvetica", 12, "bold"), bg="#f16e56",
                activebackground="#f16e56", variable=checkVariable3, command=lambda: sumarContador(checkVariable3))
checkbutton3.grid(row=9, column=0, padx=(0,15))

checkbutton4 = tk.Checkbutton(frame3, text="Pollo", font=("Helvetica", 12, "bold"), bg="#f16e56",
                activebackground="#f16e56", variable=checkVariable4,
                command=lambda: sumarContador(checkVariable4))    
checkbutton4.grid(row=10, column=0, padx=(0, 30))

#ubicacion de los labels de los precios de los ingredientes


label7 = tk.Label(frame3, text="$1.00", font=("Helvetica", 16, "bold"), bg="#f16e56")
label7.grid(row=7,column=5)

label8 = tk.Label(frame3, text="$1.50", font=("Helvetica", 16, "bold"), bg="#f16e56")
label8.grid(row=8,column=5)

label9 = tk.Label(frame3, text="$1.25", font=("Helvetica", 16, "bold"), bg="#f16e56")
label9.grid(row=9,column=5)

label10 = tk.Label(frame3, text="$1.75", font=("Helvetica", 16, "bold"), bg="#f16e56")
label10.grid(row=10,column=5)

rowPedidos=0
columnPedidos=0

checkVariables = [checkVariable1, checkVariable2, checkVariable3, checkVariable4]
checkbotones = [checkbutton1, checkbutton2, checkbutton3, checkbutton4]

total = 0

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

validacion =root.register(limitEntradas(3))

cantPizzas = tk.Entry(frame2, width=3, validate="key", validatecommand=(validacion, '%P'), 
                      bg="light coral", font=("Helvetica", 12, "bold"))
cantPizzas.grid(row=2, column=1)

checkCombo1 = tk.Checkbutton(frame2, text="Combo 1",border=5, relief="ridge", font=("Helvetica", 12, "bold"), bg="light coral", activebackground="#f16e56")
checkCombo1.grid(row=3, column=0, pady=(50,0))

checkCombo2 = tk.Checkbutton(frame2, text="Combo 2",border=5, relief="ridge", font=("Helvetica", 12, "bold"), bg="light coral", activebackground="#f16e56")
checkCombo2.grid(row=3, column=1, pady=(50,0))

buttonAgregar = tk.Button(frame2, text="Agregar", bg="light coral",border=5, relief="ridge", font=("Helvetica", 16, "bold"),
                          activebackground="#f16e56", command=pedidos)
buttonAgregar.grid(row=4, column=1, pady=(20,0))

#Corre en bucle el programa 
root.mainloop()