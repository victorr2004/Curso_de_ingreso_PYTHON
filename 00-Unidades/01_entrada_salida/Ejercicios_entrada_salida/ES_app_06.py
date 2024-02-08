import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: entrada_salida_06
---
Enunciado:
Al presionar el botón  'Sumar', se deberán obtener los valores contenidos en las cajas de texto (txt_operador_A y txt_operador_B), transformarlos en números enteros, realizar la suma y luego mostrar el resultado de la operación utilizando el Dialog Alert. 
Ej: "El resultado de la sumas es: 755" 
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Operador A")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_operador_a = customtkinter.CTkEntry(master=self)
        self.txt_operador_a.grid(row=0, column=1)
        
        self.label2 = customtkinter.CTkLabel(master=self, text="Operador B")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_operador_b = customtkinter.CTkEntry(master=self)
        self.txt_operador_b.grid(row=1, column=1)
        
        self.btn_sumar = customtkinter.CTkButton(master=self, text="Sumar", command=self.btn_sumar_on_click)
        self.btn_sumar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_sumar_on_click(self):
        operando1_str = self.txt_operador_a.get()
        operando2_str = self.txt_operador_b.get()

        operando1 = int(operando1_str)
        operando2 = int(operando2_str)

        resultado = operando1 + operando2

       
        alert("saludo", "la suma entre " + operando1_str + " y " + operando2_str + " es igual a: " + str(resultado))


     
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()