import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledText

def send_melding(event=None):
    melding = entry_user.get()
    if melding.strip():  # Sjekk at meldingen ikke er tom
        # 1. Lås opp boksen så vi kan skrive til den
        chat_history.config(state="normal")
        
        # 2. Legg til brukernavn med farge ("user_tag") og selve meldingen
        chat_history.insert(END, "Deg: ", "user_tag")
        chat_history.insert(END, f"{melding}\n")
        
        # 3. Simuler et enkelt svar fra boten
        chat_history.insert(END, "Bot: ", "bot_tag")
        chat_history.insert(END, "Dette er et automatisk svar.\n\n")
        
        # 4. Lås boksen igjen og rull til bunnen
        chat_history.config(state="disabled")
        chat_history.see(END)
        
        # 5. Tøm inntastingsfeltet
        entry_user.delete(0, END)

window = ttk.Window(themename="minty")
window.geometry("500x500")
window.title("Min Chat Bot")

# --- Chat-historikk (Text-widget) ---
chat_history = ScrolledText(window, padding=10, height=15, state="disabled")
chat_history.pack(fill=BOTH, expand=True, padx=10, pady=10)

# Definer stiler (Tags)
chat_history.tag_configure("user_tag", foreground="#28a745", font=("Helvetica", 10, "bold"))
chat_history.tag_configure("bot_tag", foreground="#17a2b8", font=("Helvetica", 10, "bold"))

# --- Inntastingsfelt nederst ---
frame_input = ttk.Frame(window, padding=10)
frame_input.pack(fill=X)

entry_user = ttk.Entry(frame_input)
entry_user.pack(side=LEFT, fill=X, expand=True, padx=(0, 10))
# Gjør at man kan trykke "Enter" for å sende
entry_user.bind("<Return>", send_melding)

btn_send = ttk.Button(frame_input, text="Send", command=send_melding, bootstyle=SUCCESS)
btn_send.pack(side=RIGHT)

window.mainloop()