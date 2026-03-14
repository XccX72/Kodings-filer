import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledText

window = ttk.Window(themename="minty")
window.geometry("500x500")
window.title("Chat Bot")

window.columnconfigure(0, weight=1)

frame_user = ttk.Frame(
    window, 
    cursor= "hand2", 
)
frame_user.grid(
    column = 0, 
    row = 0, 
    sticky= "nsew", 
    padx= 10, 
    pady = 10
)

label_user = ttk.Label(
    frame_user, 
    text = "Skriv noe inn!", 
    font = 20
)
label_user.pack(anchor= "center")

entry_user = ttk.Entry(
    frame_user
)
entry_user.pack(anchor= "center")


button_user = ttk.Button(
    frame_user,
    text = "Send inn!", 
)
button_user.pack(anchor="center")

text = ScrolledText(
    frame_user, 
    autohide= False
)
text.pack(
    anchor= "center", 
    padx = 10, 
    pady = 10, 
    fill= "both", 
    expand= True
)


text_user = ttk.Text
window.mainloop()