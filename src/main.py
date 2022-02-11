# Importando Tkinter, Tkcalendar e db
from tkinter import *
from turtle import update
from tkcalendar import DateEntry
from tkinter import messagebox
from tkinter import ttk
from view import *

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

frame_down = Frame(window, width=310, height=403, bg=co1, relief="flat")
frame_down.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_right = Frame(window, width=588, height=403, bg=co1, relief="flat")
frame_right.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

# Label Cima
app_name = Label(frame_up, text="Formulário Piece", anchor=NW, font=("Ivy 13 bold"), bg=co2, fg=co1, relief="flat")
app_name.place(x=86, y=15)

# Váriavel global
global tree


# Função Inserir 
def insert(): 
    saga = e_saga.get()
    arco = e_arco.get()
    ep = e_ep.get()
    desc = e_desc.get()
    filler = e_filler.get()
    data = e_date.get()
    
    lista = [saga, arco, ep, filler, data, desc]

    if saga == "": 
        messagebox.showerror("Erro", "Saga não pode ser em branco")
    else:
        insert_info(lista)
        messagebox.showinfo("Sucesso", "Dados inseridos com sucesso")
        
        saga = e_saga.delete(0, "end")      
        arco = e_arco.delete(0, "end")
        ep = e_ep.delete(0, "end")
        desc = e_desc.delete(0, "end")
        filler = e_filler.delete(0, "end")
        data = e_date.delete(0, "end")
        
    for widget in frame_right.winfo_children(): 
        widget.destroy()
    show()

# Função Atualizar
def atualizar(): 
    try: 
        treev_dados = tree.focus()
        treev_dic = tree.item(treev_dados)
        tree_list = treev_dic["values"]
        
        valor = tree_list[0]
        
        saga = e_saga.delete(0, "end")      
        arco = e_arco.delete(0, "end")
        ep = e_ep.delete(0, "end")
        desc = e_desc.delete(0, "end")
        filler = e_filler.delete(0, "end")
        data = e_date.delete(0, "end")
        
        saga = e_saga.insert(0, tree_list[1])      
        arco = e_arco.insert(0, tree_list[2])
        ep = e_ep.insert(0, tree_list[3])
        desc = e_desc.insert(0, tree_list[6])
        filler = e_filler.insert(0, tree_list[4])
        data = e_date.insert(0, tree_list[5])
        
        def update(): 
            saga = e_saga.get()
            arco = e_arco.get()
            ep = e_ep.get()
            desc = e_desc.get()
            filler = e_filler.get()
            data = e_date.get()
            
            lista = [saga, arco, ep, filler, data, desc]

            if saga == "": 
                messagebox.showerror("Erro", "Saga não pode ser em branco")
            else:
                update_info(lista)
                messagebox.showinfo("Sucesso", "Dados atualizados com sucesso")
                
                saga = e_saga.delete(0, "end")      
                arco = e_arco.delete(0, "end")
                ep = e_ep.delete(0, "end")
                desc = e_desc.delete(0, "end")
                filler = e_filler.delete(0, "end")
                data = e_date.delete(0, "end")
                
            for widget in frame_right.winfo_children(): 
                widget.destroy()
                
        # Botão Confirmar
        b_confirmar = Button(frame_down, command=update, text="Confirmar", width=10, font=("Ivy 10 bold"), bg=co2, fg=co1, relief="raised", overrelief="ridge")
        b_confirmar.place(x=109, y=320)
    
        show()

    except IndexError: 
        messagebox.showerror("Erro", "Selecione algum dado na tabela!")   
    
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
e_ep = Entry(frame_down, width=45, justify="left", relief="solid", )
e_ep.place(x=13, y=160)

# Informação Extra
l_desc = Label(frame_down, text="Informação Extra:", anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4, relief="flat")
l_desc.place(x=10, y=195)
e_desc = Entry(frame_down, width=45, justify="left", relief="solid")
e_desc.place(x=13, y=220)

# Fillers
l_filler = Label(frame_down, text="Filler:", anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4, relief="flat")
l_filler.place(x=170, y=255)
e_filler = ttk.Combobox(frame_down, values=("Não", "Sim") , width=15, state="readonly")
e_filler.set("Não")
e_filler.place(x=173, y=280)

# Data que assistiu
l_date = Label(frame_down, text="Quando Assistiu:", anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4, relief="flat")
l_date.place(x=10, y=255)
e_date = DateEntry(frame_down, width=15, background=co3 , foreground="white", borderwidth=2)
e_date.place(x=13, y=280)

# Botão Inserir 
b_inserir = Button(frame_down, command=insert, text="Inserir", width=10, font=("Ivy 10 bold"), bg=co6, fg=co1, relief="raised", overrelief="ridge")
b_inserir.place(x=13, y=350)

# Botão Atualizar 
b_editar = Button(frame_down, command=atualizar, text="Editar", width=10, font=("Ivy 10 bold"), bg=co2, fg=co1, relief="raised", overrelief="ridge")
b_editar.place(x=109, y=350)

# Botão Deletar 
b_deletar = Button(frame_down, text="Deletar", width=10, font=("Ivy 10 bold"), bg=co7, fg=co1, relief="raised", overrelief="ridge")
b_deletar.place(x=205, y=350)

# Frame Direita
def show(): 
    global tree
    
    lista = show_information()
    tabela_head = ['ID', 'Saga', 'Arcos', 'Episódios', 'Filler', 'Data', 'Descrição']

    # criando a tabela
    tree = ttk.Treeview(frame_right, selectmode="extended", columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_right, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frame_right, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_right.grid_rowconfigure(0, weight=12)


    hd=["center","center","center","center","center","center","center"]
    h=[30,170,140,80,55,85,155]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n], anchor=hd[n])
        
        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)

show()
window.mainloop()
