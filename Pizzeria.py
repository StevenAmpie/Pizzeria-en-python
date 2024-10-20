#Pizzeria en python

import tkinter as tk

# window

root = tk.Tk("Pizzeria")
root.config(bg="orange", )
root.geometry("3600x1200")

# Frames

frame1 = tk.Frame(bg="gray", height=500, width=500, border=20, relief="groove")
frame1.grid(row=0, column=0, pady=150, padx=(10,0))
frame1.grid_propagate(False)

frame2 = tk.Frame(bg="gray", height=500, width=500, border=20, relief="groove")
frame2.grid(row=0, column=1, pady=150)
frame2.grid_propagate(False)

frame3 = tk.Frame(bg="white", height=500, width=500, border=20, relief="groove")
frame3.grid(row=0, column=2, pady=150)
frame3.grid_propagate(False)

#Radiobuttons

eleccion = tk.IntVar()
eleccion.set(1)

radio1 = tk.Radiobutton(frame3, bg="white", text="Personal", variable=eleccion, value=1, width=10,
 font=("Helvetica", 16, "bold"))

radio2 = tk.Radiobutton(frame3, bg="white", text="Mediana ", variable=eleccion, value=2, width=10,
 font=("Helvetica", 16, "bold"))


radio3 = tk.Radiobutton(frame3, bg="white", text="Grande   ", variable=eleccion, value=3, width=10,
 font=("Helvetica", 16, "bold"))


radio4 = tk.Radiobutton(frame3, bg="white", text="Familiar  ", variable=eleccion, value=4, width=10,
 font=("Helvetica", 16, "bold"))

#labels


label1 = tk.Label(frame3, text="Ordene su pizza\n", font=("Helvetica", 16, "bold"), bg="white")
label1.grid(row=0,column=3)

label2 = tk.Label(frame3, text="Tamaño:", font=("Helvetica", 16, "bold"), bg="white")
label2.grid(row=1,column=0)

label3 = tk.Label(frame3, text="\n$10.00", font=("Helvetica", 16, "bold"), bg="white")
label3.grid(row=2,column=5)

label4 = tk.Label(frame3, text="$15.00", font=("Helvetica", 16, "bold"), bg="white")
label4.grid(row=3,column=5)

label5 = tk.Label(frame3, text="$20.00", font=("Helvetica", 16, "bold"), bg="white")
label5.grid(row=4,column=5)

label6 = tk.Label(frame3, text="$25.00", font=("Helvetica", 16, "bold"), bg="white")
label6.grid(row=5,column=5)


label7 = tk.Label(frame3, text="\nIngredientes:\n", font=("Helvetica", 16, "bold"), bg="white")
label7.grid(row=6,column=0)

#ubicacion en los radio

radio1.grid(row=2, column=0,pady=(15,0))
radio2.grid(row=3, column=0)
radio3.grid(row=4, column=0)
radio4.grid(row=5, column=0)



#Ingredientes usando checkbox

checkbutton1 = tk.Checkbutton(frame3, text="Queso    ", font=("Helvetica", 12, "bold"), bg="white")
checkbutton1.grid(row=7, column=0)

checkbutton2 = tk.Checkbutton(frame3, text="Pepperoni", font=("Helvetica", 12, "bold"), bg="white")
checkbutton2.grid(row=8, column=0, padx=(10,0))

checkbutton3 = tk.Checkbutton(frame3, text="Jamon", font=("Helvetica", 12, "bold"), bg="white")
checkbutton3.grid(row=9, column=0, padx=(0,15))

checkbutton4 = tk.Checkbutton(frame3, text="Pollo", font=("Helvetica", 12, "bold"), bg="white")
checkbutton4.grid(row=10, column=0, padx=(0, 30))

#ubicacion de los labels de los precios de los ingredientes


label7 = tk.Label(frame3, text="$1.00", font=("Helvetica", 16, "bold"), bg="white")
label7.grid(row=7,column=5)

label8 = tk.Label(frame3, text="$1.50", font=("Helvetica", 16, "bold"), bg="white")
label8.grid(row=8,column=5)

label9 = tk.Label(frame3, text="$1.25", font=("Helvetica", 16, "bold"), bg="white")
label9.grid(row=9,column=5)

label10 = tk.Label(frame3, text="$1.75", font=("Helvetica", 16, "bold"), bg="white")
label10.grid(row=10,column=5)

from PIL import Image, ImageTk

# Cargar la imagen usando PIL
image_path = "p.png"
image = Image.open(image_path)

# Redimensionar la imagen si es necesario
image = image.resize((300, 300))  # Ajustar tamaño si es necesario

# Convertir la imagen para que Tkinter pueda usarla
tk_image = ImageTk.PhotoImage(image)

# Crear un label y asignar la imagen
labelImagen = tk.Label(frame2, image=tk_image)
 
labelImagen.grid(row=0, column=0, padx=(60,0))

labelMenu = tk.Label(frame2, text="Ordene su pizza\n", font=("Helvetica", 16, "bold"), bg="white")
labelMenu.grid(row=1,column=0, padx=(30,0), pady=(30,0))


#Corre en bucle el programa 
root.mainloop()