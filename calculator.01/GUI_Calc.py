import tkinter as tk
import ttkbootstrap as ttk
import keyboard as kb




def check_key():
    if kb.is_pressed("Escape"):
        destroy_window()
    else:
        window.after(100, check_key)
        
def destroy_window():
    window.destroy()

def pluss():
    pass

def minus():
    pass

def ganging():
    pass

def deling():
    pass

def siffre(tall):
    gjeldende = svar_label.cget("text")
    if gjeldende is None:
        gjeldende = ""
    svar_label.config(text = str(gjeldende) + str(tall))

def spesielltegn_pi_func():
    pi = 3.141592653589793238462643383279
    svar_label.config(text = pi)

def spesielltegn_e_func():
    e = 2.7182818284590
    svar_label.config(text = e)

#----------------------------------------------------
#Vindu
#----------------------------------------------------

window = ttk.Window(themename = "minty")
window.title("Calc")
window.state("zoomed")

#Overskrift
Overskrift_frame = ttk.Frame(
    window, 
    cursor= "hand2"
)
Overskrift_frame.grid(
    column= 0, 
    row= 0, 
    padx= 10, 
    pady= 10, 
    columnspan= 4
)
Overskrift_Label = ttk.Label(
    Overskrift_frame, 
    text = "Calculator", 
    bootstyle= "inverser-primary", 
    padding= 10, 
)
Overskrift_Label.pack()

#4 Regnearter
Regneart_frame = ttk.Frame(
    window, 
    cursor = "hand2"
)
Regneart_frame.grid(
    column= 0, 
    row = 1, 
    padx= 10, 
    pady = 10
)
Regneart_Pluss = ttk.Button(
    Regneart_frame, 
    text = "Plus", 
    command = pluss, 
    padding= 10, 
    
)
Regneart_Pluss.pack(fill = "x")

Regneart_Minus = ttk.Button(
    Regneart_frame, 
    text= "Minus", 
    command= minus, 
    padding= 10, 
    
)
Regneart_Minus.pack(fill = "x")

Regneart_Ganging = ttk.Button(
    Regneart_frame, 
    text = "Time", 
    command = ganging, 
    padding= 10, 
)
Regneart_Ganging.pack(fill = "x")

Regneart_Deling = ttk.Button(
    Regneart_frame, 
    text = "Divide", 
    command = deling, 
    padding= 10, 
)
Regneart_Deling.pack(fill = "x")

#Siffre
siffre_frame = ttk.Frame(
    window, 
    cursor= "hand2"
)
siffre_frame.grid(
    column= 1, 
    row = 1
)

for i in range(10):
    siffre_1_9 = ttk.Button(
        siffre_frame, 
        text = str(i), 
        command = lambda x = i: (siffre(x))
    )
    siffre_1_9.pack(fill = "x")

siffre_0 = ttk.Button(
    siffre_frame, 
    text = "0", 
    padding= 10, 
    command= lambda: siffre(0)
)
siffre_0.pack(fill = "x")

#SpesiellTegn
spesielltegn_frame = ttk.Frame(
    window, 
    cursor= "hand2"
)
spesielltegn_frame.grid(
    column = 2, 
    row = 1, 
    padx= 10, 
    pady = 10
)

spesielltegn_pi = ttk.Button(
    spesielltegn_frame, 
    text = "Pi", 
    command = spesielltegn_pi_func, 
    padding = 10
)
spesielltegn_pi.pack(fill = "x")

spesielltegn_e = ttk.Button(
    spesielltegn_frame, 
    text = "e", 
    padding = 10, 
    command = spesielltegn_e_func
)
spesielltegn_e.pack(fill = "x")

#Svar_Boks

svar_frame = ttk.Frame(
    window, 
    cursor= "hand2", 
)
svar_frame.grid(
    column = 3, 
    row = 1, 
    padx = 10, 
    pady = 10
)

svar_label_text = ttk.Label(
    svar_frame, 
    text = "Equal/=", 
    bootstyle= "inverser-primary", 
    padding= 10
)
svar_label_text.pack()
svar_label = ttk.Label(
    svar_frame, 
    text = None,
    bootstyle= "inverser-primary", 
    padding= 10 
)
svar_label.pack()

check_key()
window.mainloop()