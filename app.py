import tkinter as tk

def saludar():
    label.config(text="Hola, " + entry.get())

app = tk.Tk()
app.title("Mi App")

label = tk.Label(app, text="Ingrese su nombre:")
label.pack()

entry = tk.Entry(app)
entry.pack()

button = tk.Button(app, text="Saludar", command=saludar)
button.pack()

app.mainloop()
