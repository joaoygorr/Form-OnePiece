# Importando Tkinter 
from cgitb import text
from tkinter import *
from tkinter import font 

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

window.mainloop()