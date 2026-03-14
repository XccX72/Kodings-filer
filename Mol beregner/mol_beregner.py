import tkinter as tk
from tkinter import ttk
import tkinter.font as tkf
import pandas as pd


df = pd.read_csv("Mol beregner/grunnstoffer.csv")

#Funksjoner -----------------------------------------------------------------------------------------
mol = 6.022e23

def beregner_partikkler():
    #antall partikler for i mol
    i = float(skrive.get())
    p = mol * i
    resultat_label.config(text= f"Partikler = {p :.2e}")

def beregn_mol():
    # antall mol for i partikler
    i = float(skrive.get())
    m = i/mol
    resultat_label.config(text = f"Mol = {m:.4f}")

def hvilket_grunnstoff():
    i = int(info_entry.get())
    resultat = df[df['Atomnummer'] == i]

    if not resultat.empty:
        navn = resultat['Navn'].values[0]
        masse = resultat['Molarmasse'].values[0]
        symbol = resultat['Symbol'].values[0]
        Elektronegativitet = resultat['Elektronegativitet'].values[0]
        info_text = (f"Navn: {navn}\nSymbol : {symbol} \nMolarMasse : {masse}\nElektronegativitet : {Elektronegativitet}")
        info_Label.config(text = info_text)    
    else:
        info_Label.config(text = f"Fant ikke atomnummeret :(")

def finn_gram():
    antall_mol = int(hvilken_funksjon.get())
    hvilket_grunnstoff_funksjoner_bla = int(hvilket_grunnstoff_funksjoner.get())
    

window = tk.Tk()
#main shit -------------------------------------------------------------------------------------------------
window.title("Mol Beregninger")

window.geometry("1060x1060")

#Font del / tittel --------------------------------------------------------------------------------------------
font_a = tkf.Font(
    family = "Helvetica",
    size = 15
    )

tittel = tk.Label(
    window,
    text = "Mol Beregninger",
    font = ("Helvetica", 30)
)
tittel.grid(
    column= 0,
    row = 0,
    padx = 10,
    pady = 10,  
    columnspan= 2  
    )

# Funksjonenen  partikkler---------------------------------------------------------------------------------------
partikkler_knapp = tk.Button(
    window,
    text = "Partikkel Beregner",
    font= font_a,
    bg = "lightblue",
    command = beregner_partikkler
    )
partikkler_knapp.grid(
    column = 0,
    row = 2,
    padx = 20,
    pady = 20,
    ipadx = 15, 
    ipady= 50
)
# Funksjonenen  mol-------------------------------------------------------------------------------------------------------

mol_knapp = tk.Button(
    window,
    text = "Mol",
    font= font_a,
    bg = "lightblue", 
    command = beregn_mol
)
mol_knapp.grid(
    column = 1,
    row = 2,
    padx = 20,
    pady = 20,
    ipadx = 75, 
    ipady= 50
)

skrive = tk.Entry(
    window, 
    bg = "lightblue"
)
skrive.grid(
    column = 0,
    row = 1,
    padx = 200,
    pady = 20,
    columnspan= 2
)

resultat_label = tk.Label(
    window, 
    text="Resultat vises her: Partikler/Mol", 
    font=("Helvetica", 18), 
    fg="black",
    bg = "lightblue"
    )
resultat_label.grid(
    column=0, 
    row=3, 
    columnspan=2, 
    pady=20)

# grunnstoff info---------------------------------------------------------------------------------------------------
grunnstoff = tk.Button(
    window, 
    text = "Grunnstoff",
    font= font_a,
    bg = "lightblue", 
    command = hvilket_grunnstoff
)
grunnstoff.grid(
    column = 2,
    row = 2, 
    pady = 20, 
    padx = 20, 
    ipadx = 50, 
    ipady = 50
)

info_entry = tk.Entry(
    window, 
    bg = "lightblue"
    )
info_entry.grid(
    column = 2, 
    row = 1, 
    pady = 20, 
    padx = 20
)
info_Label = tk.Label(
    window, 
    text="Resultat vises her: Grunnstoff Info", 
    font=("Helvetica", 18), 
    fg="black",
    bg = "lightblue"
)
info_Label.grid(
    column = 2, 
    row = 3, 
    pady = 20, 
    padx = 20
)

# ---------------------------------------------------------------------------------------------
#For å finne gram eller antall mol ved hjelp av molarmasse

hvilken_funksjon = ttk.Combobox(window, values=["H", "He", "Li", "Be"])
hvilken_funksjon.grid(
    column= 0,
    row = 4, 
    pady = (20, 0), 
    padx = 20
)
hvilket_grunnstoff_funksjoner = tk.Entry(
    window, 
    bg = "lightblue"
)
hvilket_grunnstoff_funksjoner.grid(
    padx = 20,
    pady = (0, 20), 
    column = 0,
    row = 5
)
hvilken_funksjon_label = tk.Label(
    window, 
    text = "Resultat Her", 
    font = font_a, 
    bg = "lightblue"
)
hvilken_funksjon_label.grid(
    column= 0, 
    row = 6, 
    pady = 20, 
    padx = 20
)

window.mainloop()