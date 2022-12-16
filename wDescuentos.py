import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgBox
import bll.Descuentos as FDescuentos

# TODO editar para descuentos

class Descuento(tk.Toplevel):
    def __init__(self, master = None, desc_id = None):
        super().__init__(master)
        self.master = master
        self.desc_id = desc_id        
        self.title("DESCUENTOS")        
        width=600
        height=140
        screenwidth = master.winfo_screenwidth()
        screenheight = master.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_692=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_692["font"] = ft
        GLabel_692["fg"] = "#333333"
        GLabel_692["justify"] = "right"
        GLabel_692["text"] = "DIAS"
        GLabel_692.place(x=0,y=20,width=200,height=30)

        GLabel_458=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_458["font"] = ft
        GLabel_458["fg"] = "#333333"
        GLabel_458["justify"] = "right"
        GLabel_458["text"] = "DESCUENTO"
        GLabel_458.place(x=0,y=60,width=200,height=30)       
        
        
        GLineEdit_794=tk.Entry(self, name="txtDia")
        GLineEdit_794["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_794["font"] = ft
        GLineEdit_794["fg"] = "#333333"
        GLineEdit_794["justify"] = "center"
        GLineEdit_794["text"] = ""
        GLineEdit_794.place(x=220,y=20,width=320,height=30)

        GLineEdit_522=tk.Entry(self, name="txtDescuento")
        GLineEdit_522["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_522["font"] = ft
        GLineEdit_522["fg"] = "#333333"
        GLineEdit_522["justify"] = "center"
        GLineEdit_522["text"] = ""
        GLineEdit_522.place(x=220,y=60,width=320,height=30)    
                       
        GButton_71=tk.Button(self)
        GButton_71["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_71["font"] = ft
        GButton_71["fg"] = "#000000"
        GButton_71["justify"] = "center"
        GButton_71["text"] = "ACEPTAR"
        GButton_71.place(x=220,y=100,width=150,height=30)
        GButton_71["command"] = self.aceptar
        
        GButton_271=tk.Button(self)
        GButton_271["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_271["font"] = ft
        GButton_271["fg"] = "#000000"
        GButton_271["justify"] = "center"
        GButton_271["text"] = "CANCELAR"
        GButton_271.place(x=390,y=100,width=150,height=30)
        GButton_271["command"] = self.cancelar
        
        if desc_id is not None:
            desc = FDescuentos.obtener_id(desc_id)
            if desc is None:
               tkMsgBox.showerror(self.master.title(), "Se produjo un error al obtener los datos del descuento, reintente nuevamente")
               self.destroy()
            else:                
                GLineEdit_794.insert(0, desc[1])
                GLineEdit_522.insert(0, desc[2])                                         
                
    
    def get_value(self, name):
        return self.nametowidget(name).get()

    def get_index(self, name):
        return self.nametowidget(name).current() + 1  


    def cancelar(self):
        self.destroy()
    
        
    def aceptar(self):
        try:            
            dias = self.get_value("txtDia")
            descuento = self.get_value("txtDescuento")                        
                
            if self.desc_id is None:                                  
                FDescuentos.agregar(dias, descuento)
                tkMsgBox.showinfo(self.master.title(), "Descuento agregado!!!!!!")                
                try:
                    self.master.refrescar()
                except Exception as ex:
                    print(ex)
                self.destroy()  
            else:
                print("Actualizacion de desceunto")
                FDescuentos.actualizar(dias, descuento, self.desc_id)  
                tkMsgBox.showinfo(self.master.title(), "Descuento modificado!!!!!!")                
                self.master.refrescar()
                self.destroy()      
                
                
        except Exception as ex:
            tkMsgBox.showerror(self.master.title(), str(ex))