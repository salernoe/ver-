import tkinter as tk
import tkinter.font as tkFont
import bll.usuarios as user
from wPerfilCRUD import Perfil  


class Client(tk.Toplevel):
    def __init__(self, master = None, user_id = None):
        super().__init__(master)
        self.master = master  
        self.user_id = user_id      
        self.title("USER")        
        width=240
        height=180
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GButton_561=tk.Button(self)
        GButton_561["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_561["font"] = ft
        GButton_561["fg"] = "#000000"
        GButton_561["justify"] = "center"
        GButton_561["text"] = "EDITAR PERFIL"
        GButton_561.place(x=20,y=20,width=200,height=30)
        GButton_561["command"] = self.GButton_561_command

        GButton_269=tk.Button(self)
        GButton_269["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_269["font"] = ft
        GButton_269["fg"] = "#000000"
        GButton_269["justify"] = "center"
        GButton_269["text"] = "RESERVAS"
        GButton_269.place(x=20,y=70,width=200,height=30)
        GButton_269["command"] = self.GButton_269_command

        GButton_811=tk.Button(self)
        GButton_811["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_811["font"] = ft
        GButton_811["fg"] = "#000000"
        GButton_811["justify"] = "center"
        GButton_811["text"] = "SALIR"
        GButton_811.place(x=20,y=120,width=200,height=30)
        GButton_811["command"] = self.salir

    def GButton_561_command(self):
        print(self.user_id)
        Perfil.editar(self, Client.get_id(self))


    def GButton_269_command(self):
        print("command")


    def salir(self):
        self.destroy()
    
    def get_id(self):
        return self.user_id
        
    
