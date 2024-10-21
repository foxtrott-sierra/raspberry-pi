import tkinter as tk
import math

def calculate(operation):
    try:
        if operation == "Addieren":
            resultat = float(entry1.get()) + float(entry2.get())
        elif operation == "Subtrahieren":
            resultat = float(entry1.get()) - float(entry2.get())
        elif operation == "Multiplizieren":
            resultat = float(entry1.get()) * float(entry2.get())
        elif operation == "Dividieren":
            num2 = float(entry2.get())
            if num2 == 0:
                resultat = "Dividieren durch 0 nicht möglich."
            else:
                resultat = float(entry1.get()) / num2
        elif operation == "Wurzel":
            resultat= math.sqrt(float(entry1.get()))
        elif operation =="Potenz":
            resultat = float(entry1.get()) ** float(entry2.get())
        elif operation == "Logarythmus":
            resultat = math.log(float(entry1.get()))
        else:
            resultat = "Ungültige Operation."

        result_label.config(text="Resultat: " + str(resultat))
    except ValueError:
        result_label.config(text="Ungültiger Input.")

root = tk.Tk()
root.title("Erweiterter Rechner")

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=5, pady=5)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)

operationen =[
    "Addieren",
    "Subtrahieren",
    "Multiplizieren",
    "Dividieren",
    "Wurzel",
    "Potenz",
    "Logarythmus"
]

row_val = 2
for operation in operationen:
    operation_button = tk.Button(root, text=operation, command=lambda op=operation: calculate(op))
    operation_button.grid(row=row_val, column=0, columnspan=2, padx=5, pady=5)
    row_val += 1

result_label = tk.Label(root)
result_label.grid(row=row_val, column=0, columnspan=2)

root.mainloop()