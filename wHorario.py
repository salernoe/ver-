import tkinter as tk
import tkinter.font as tkFont

class Horario(tk.Toplevel):
    def _init_(self, master = None, hid =  None):
        super()._init_(master)
        self.master = master
        self.hid = hid
        #setting title
        self.title("Registro de Horario")
        #setting window size
        width=597
        height=329
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GListBox_450=tk.Listbox(self)
        GListBox_450["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_450["font"] = ft
        GListBox_450["fg"] = "#333333"
        GListBox_450["justify"] = "center"
        GListBox_450.place(x=10,y=40,width=572,height=233)

        GLabel_241=tk.Label(self)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_241["font"] = ft
        GLabel_241["fg"] = "#333333"
        GLabel_241["justify"] = "center"
        GLabel_241["text"] = "HORARIOS"
        GLabel_241.place(x=260,y=10,width=70,height=25)

        GButton_537=tk.Button(self)
        GButton_537["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_537["font"] = ft
        GButton_537["fg"] = "#000000"
        GButton_537["justify"] = "center"
        GButton_537["text"] = "REGISTRAR"
        GButton_537.place(x=270,y=290,width=70,height=25)
        GButton_537["command"] = self.registrar

        GButton_592=tk.Button(self)
        GButton_592["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_592["font"] = ft
        GButton_592["fg"] = "#000000"
        GButton_592["justify"] = "center"
        GButton_592["text"] = "EDITAR"
        GButton_592.place(x=350,y=290,width=70,height=25)
        GButton_592["command"] = self.editar

        GButton_824=tk.Button(self)
        GButton_824["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_824["font"] = ft
        GButton_824["fg"] = "#000000"
        GButton_824["justify"] = "center"
        GButton_824["text"] = "ELIMINAR"
        GButton_824.place(x=430,y=290,width=70,height=25)
        GButton_824["command"] = self.eliminar

        GButton_162=tk.Button(self)
        GButton_162["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_162["font"] = ft
        GButton_162["fg"] = "#000000"
        GButton_162["justify"] = "center"
        GButton_162["text"] = "SALIR"
        GButton_162.place(x=510,y=290,width=70,height=25)
        GButton_162["command"] = self.salir

    def registrar(self):
        print("command")


    def editar(self):
        print("command")


    def eliminar(self):
        print("command")


    def salir(self):
        print("command")


    def get_value(self, name):
        return self.nametowidget(name).get()