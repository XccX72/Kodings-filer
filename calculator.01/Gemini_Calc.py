import tkinter as tk
import ttkbootstrap as ttk
import keyboard as kb

# --- GLOBALE VARIABLER ---
første_tall = 0
valgt_operasjon = ""

# --- FUNKSJONER ---

def siffre(tall):
    # Legger til tallet i displayet
    gjeldende = svar_label.cget("text")
    svar_label.config(text=str(gjeldende) + str(tall))

def sett_operasjon(op):
    global første_tall, valgt_operasjon
    try:
        # Lagre tallet som står i displayet nå
        første_tall = float(svar_label.cget("text"))
        valgt_operasjon = op
        # Tøm displayet så vi kan skrive inn tall nummer to
        svar_label.config(text="")
    except ValueError:
        pass # Gjør ingenting hvis displayet er tomt

def beregn_svar():
    global første_tall, valgt_operasjon
    try:
        andre_tall = float(svar_label.cget("text"))
        
        if valgt_operasjon == "+":
            resultat = første_tall + andre_tall
        elif valgt_operasjon == "-":
            resultat = første_tall - andre_tall
        elif valgt_operasjon == "*":
            resultat = første_tall * andre_tall
        elif valgt_operasjon == "/":
            resultat = første_tall / andre_tall if andre_tall != 0 else "Error"
            
        svar_label.config(text=str(resultat))
    except ValueError:
        svar_label.config(text="Error")

def clear_display():
    svar_label.config(text="")

# ... (Vindu-oppsett som før) ...
window = ttk.Window(themename="minty")
window.state("zoomed")

# --- OPPDATERT LAYOUT ---

# 4 Regnearter (Bruker nå sett_operasjon)
Regneart_frame = ttk.Frame(window)
Regneart_frame.grid(column=0, row=1, padx=10, pady=10)

ttk.Button(Regneart_frame, text="+", command=lambda: sett_operasjon("+")).pack(fill="x", pady=2)
ttk.Button(Regneart_frame, text="-", command=lambda: sett_operasjon("-")).pack(fill="x", pady=2)
ttk.Button(Regneart_frame, text="*", command=lambda: sett_operasjon("*")).pack(fill="x", pady=2)
ttk.Button(Regneart_frame, text="/", command=lambda: sett_operasjon("/")).pack(fill="x", pady=2)

# Siffre (0-9)
siffre_frame = ttk.Frame(window)
siffre_frame.grid(column=1, row=1)

for i in range(1, 10):
    ttk.Button(siffre_frame, text=str(i), command=lambda x=i: siffre(x)).pack(fill="x")
ttk.Button(siffre_frame, text="0", command=lambda: siffre(0)).pack(fill="x")

# Svar og Clear (Kolonne 3)
svar_frame = ttk.Frame(window)
svar_frame.grid(column=3, row=1, padx=10, pady=10)

# "Likhetstegnet" kjører nå beregn_svar
Equal_btn = ttk.Button(svar_frame, text=" = ", bootstyle="success", command=beregn_svar)
Equal_btn.pack(fill="x", pady=5)

Clear_btn = ttk.Button(svar_frame, text=" C ", bootstyle="danger", command=clear_display)
Clear_btn.pack(fill="x", pady=5)

svar_label = ttk.Label(svar_frame, text="", bootstyle="inverse-primary", padding=20)
svar_label.pack(fill="x")

window.mainloop()