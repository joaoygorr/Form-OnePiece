# Importando Tkinter e Tkcalendar
from tkinter import *
from tkcalendar import Calendar, DateEntry
from tkinter import ttk

################# cores ###############
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

# Criação da janela e suas configurações
window = Tk()
window.title("")
window.geometry("1043x453")
window.configure(background=co9)
window.resizable(width=FALSE, height=FALSE)

# Dividindo janela 
frame_up = Frame(window, width=310, height=50, bg=co2, relief="flat")
frame_up.grid(row=0, column=0)

frame_down = Frame(window, width=310, height=400, bg=co1, relief="flat")
frame_down.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_right = Frame(window, width=588, height=400, bg=co1, relief="flat")
frame_right.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

# Label Cima
app_name = Label(frame_up, text="Formulário Piece", anchor=NW, font=("Ivy 13 bold"), bg=co2, fg=co1, relief="flat")
app_name.place(x=86, y=15)

# Configurando frame baixo
# Saga
l_saga = Label(frame_down, text="Saga:", anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4, relief="flat")
l_saga.place(x=10, y=15)
e_saga = Entry(frame_down, width=45, justify="left", relief="solid")
e_saga.place(x=13, y=40)

# Arcos
l_arco = Label(frame_down, text="Arcos:", anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4, relief="flat")
l_arco.place(x=10, y=75)
e_arco = Entry(frame_down, width=45, justify="left", relief="solid")
e_arco.place(x=13, y=100)

# Episódios
l_ep = Label(frame_down, text="Episódio:", anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4, relief="flat")
l_ep.place(x=10, y=135)
e_ep = Entry(frame_down, width=45, justify="left", relief="solid")
e_ep.place(x=13, y=160)

# Informação Extra
l_desc = Label(frame_down, text="Informação Extra:", anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4, relief="flat")
l_desc.place(x=10, y=195)
e_desc = Entry(frame_down, width=45, justify="left", relief="solid")
e_desc.place(x=13, y=220)

# # Fillers
l_filler = Label(frame_down, text="Filler:", anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4, relief="flat")
l_filler.place(x=165, y=255)
e_filler = ttk.Combobox(frame_down, values=("Não", "Sim") , width=15, state="readonly")
e_filler.set("Não")
e_filler.place(x=167, y=280)

# # Data que assistiu
l_date = Label(frame_down, text="Quando Assistiu:", anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4, relief="flat")
l_date.place(x=10, y=255)
e_date = DateEntry(frame_down, width=15, background=co3 , foreground="white", borderwidth=2)
e_date.place(x=13, y=280)

window.mainloop()
