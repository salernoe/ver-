from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
import tkinter.messagebox as tkMsgBox
import bll.usuarios as user
from wRegistro import Registro

class Ucrud(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)        
        self.master = master
        self.select_id = -1        
        self.title("USUARIOS")        
        width=800
        height=400
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_464=Label(self)
        ft = tkFont.Font(family='Times',size=15)
        GLabel_464["font"] = ft
        GLabel_464["fg"] = "#333333"
        GLabel_464["justify"] = "center"
        GLabel_464["text"] = "USUARIOS"
        GLabel_464.place(x= 350,y=10,width=100,height=40)

        tv = ttk.Treeview(self, columns=("USUARIO", "APELLIDO", "NOMBRE", "EMAIL", "RID"), name="tvUsuarios")
        tv.column("#0", width=78)
        tv.column("USUARIO", width=100, anchor=CENTER)
        tv.column("APELLIDO", width=150, anchor=CENTER)
        tv.column("NOMBRE", width=150, anchor=CENTER)
        tv.column("EMAIL", width=150, anchor=CENTER)
        tv.column("RID", width=120, anchor=CENTER)

        tv.heading("#0", text="ID", anchor=CENTER)
        tv.heading("USUARIO", text="USUSARIO", anchor=CENTER)
        tv.heading("APELLIDO", text="APELLIDO", anchor=CENTER)
        tv.heading("NOMBRE", text="NOMBRE", anchor=CENTER)
        tv.heading("EMAIL", text="EMAIL", anchor=CENTER)
        tv.heading("RID", text="TIPO", anchor=CENTER)
        tv.bind("<<TreeviewSelect>>", self.obtener_fila)
        tv.place(x=10,y=50,width=780,height=300)          
        
        self.refrescar()

        ft = tkFont.Font(family='Times',size=10)
        btn_agregar = Button(self)
        btn_agregar["bg"] = "#f0f0f0"        
        btn_agregar["font"] = ft
        btn_agregar["fg"] = "#000000"
        btn_agregar["justify"] = "center"
        btn_agregar["text"] = "REGISTRAR"
        btn_agregar.place(x=360,y=360,width=100,height=30)
        btn_agregar["command"] = self.agregar

        btn_editar = Button(self)
        btn_editar["bg"] = "#f0f0f0"        
        btn_editar["font"] = ft
        btn_editar["fg"] = "#000000"
        btn_editar["justify"] = "center"
        btn_editar["text"] = "EDITAR"
        btn_editar.place(x=470,y=360,width=100,height=30)
        btn_editar["command"] = self.editar
        
        btn_eliminar = Button(self)
        btn_eliminar["bg"] = "#f0f0f0"        
        btn_eliminar["font"] = ft
        btn_eliminar["fg"] = "#000000"
        btn_eliminar["justify"] = "center"
        btn_eliminar["text"] = "ELIMINAR"
        btn_eliminar.place(x=580,y=360,width=100,height=30)
        btn_eliminar["command"] = self.eliminar
        
        btn_salir = Button(self)
        btn_salir["bg"] = "#f0f0f0"        
        btn_salir["font"] = ft
        btn_salir["fg"] = "#000000"
        btn_salir["justify"] = "center"
        btn_salir["text"] = "SALIR"
        btn_salir.place(x=690,y=360,width=100,height=30)
        btn_salir["command"] = self.salir
        
    def obtener_fila(self, event):
        tvUsuarios = self.nametowidget("tvUsuarios")
        current_item = tvUsuarios.focus()
        if current_item:
            data = tvUsuarios.item(current_item)
            self.select_id = int(data["text"])
        else:
            self.select_id = -1

    def agregar(self):
        Registro(self, True)

    def editar(self): 
        Registro(self, True, self.select_id)

    def eliminar(self):
        answer =  tkMsgBox.askokcancel(self.master.master.title(), "¿Está seguro de eliminar este registro?")   
        if answer:
            user.eliminar(self.select_id)
            self.refrescar()
            
    def salir(self):
        self.destroy()
    
    def refrescar(self):        
        tvUsuarios = self.nametowidget("tvUsuarios")
        for record in tvUsuarios.get_children():
            tvUsuarios.delete(record)
        usuarios = user.listar()
        for USUARIO in usuarios:
            tvUsuarios.insert("", END, text=USUARIO[0], values=(USUARIO[5], USUARIO[1], USUARIO[2], USUARIO[4], USUARIO[7])) 