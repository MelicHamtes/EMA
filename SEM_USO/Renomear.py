from tkinter import *

import tkinter

top = Tk()

mb =  Menubutton ( top, text = "condiments", relief = RAISED )
mb.grid()
mb.menu  =  Menu ( mb, tearoff = 0 )
mb["menu"]  =  mb.menu
    
mayoVar  = IntVar()
ketchVar = IntVar()

mb.menu.add_command( label = "mayo" )
mb.menu.add_command ( label = "ketchup")

mb.pack()
top.mainloop()

self.bt1 = tkinter.Button(self.janela_deck, text='Criar Deck', command=self.janela_adicionar_decks)
self.bt1.place(x=20,y=10)

self.bt2 = tkinter.Button(self.janela_deck, text='Abrir Deck', command=self.janela_abrir_decks)
self.bt2.place(x=20,y=55)

self.bt3 = tkinter.Button(self.janela_deck, text='Editar cards', command=self.janela_editar_decks)
self.bt3.place(x=97,y=10)

self.bt4 = tkinter.Button(self.janela_deck, text='Deletar deck', command=self.janela_deletar_decks)
self.bt4.place(x=95,y=55)