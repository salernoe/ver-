import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgBox
import bll.usuarios as user
import bll.TIPO as rol

class Registro(tk.Toplevel):
    def __init__(self, master = None, isAdmin = False, user_id = None):
        super().__init__(master)
        self.master = master
        self.user_id = user_id        
        self.title("REGISTRO")        
        width=600
        height=380
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
        GLabel_692["text"] = "APELLIDO"
        GLabel_692.place(x=0,y=20,width=200,height=30)

        GLabel_458=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_458["font"] = ft
        GLabel_458["fg"] = "#333333"
        GLabel_458["justify"] = "right"
        GLabel_458["text"] = "NOMBRE"
        GLabel_458.place(x=0,y=60,width=200,height=30)
        
        GLabel_693=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_693["font"] = ft
        GLabel_693["fg"] = "#333333"
        GLabel_693["justify"] = "right"
        GLabel_693["text"] = "DNI"
        GLabel_693.place(x=0,y=100,width=200,height=30)        
       
        GLabel_338=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_338["font"] = ft
        GLabel_338["fg"] = "#333333"
        GLabel_338["justify"] = "right"
        GLabel_338["text"] = "E-MAIL"
        GLabel_338.place(x=0,y=140,width=200,height=30)

        GLabel_251=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_251["font"] = ft
        GLabel_251["fg"] = "#333333"
        GLabel_251["justify"] = "right"
        GLabel_251["text"] = "USUARIO"
        GLabel_251.place(x=0,y=180,width=200,height=30)

        GLabel_219=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_219["font"] = ft
        GLabel_219["fg"] = "#333333"
        GLabel_219["justify"] = "right"
        GLabel_219["text"] = "CONTRASEÑA"
        GLabel_219.place(x=0,y=220,width=200,height=30)

        GLineEdit_794=tk.Entry(self, name="txtApellido")
        GLineEdit_794["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_794["font"] = ft
        GLineEdit_794["fg"] = "#333333"
        GLineEdit_794["justify"] = "center"
        GLineEdit_794["text"] = ""
        GLineEdit_794.place(x=220,y=20,width=320,height=30)

        GLineEdit_522=tk.Entry(self, name="txtNombre")
        GLineEdit_522["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_522["font"] = ft
        GLineEdit_522["fg"] = "#333333"
        GLineEdit_522["justify"] = "center"
        GLineEdit_522["text"] = ""
        GLineEdit_522.place(x=220,y=60,width=320,height=30)
        
        GLineEdit_211=tk.Entry(self, name="txtDni")
        GLineEdit_211["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_211["font"] = ft
        GLineEdit_211["fg"] = "#333333"
        GLineEdit_211["justify"] = "center"
        GLineEdit_211["text"] = ""
        GLineEdit_211.place(x=220,y=100,width=320,height=30)

        GLineEdit_570=tk.Entry(self, name="txtEmail")
        GLineEdit_570["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_570["font"] = ft
        GLineEdit_570["fg"] = "#333333"
        GLineEdit_570["justify"] = "center"
        GLineEdit_570["text"] = ""
        GLineEdit_570.place(x=220,y=140,width=320,height=30)

        GLineEdit_690=tk.Entry(self, name="txtUsuario")
        GLineEdit_690["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_690["font"] = ft
        GLineEdit_690["fg"] = "#333333"
        GLineEdit_690["justify"] = "center"
        GLineEdit_690["text"] = ""
        GLineEdit_690.place(x=220,y=180,width=320,height=30)

        GLineEdit_43=tk.Entry(self, name="txtContraseña")
        GLineEdit_43["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_43["font"] = ft
        GLineEdit_43["fg"] = "#333333"
        GLineEdit_43["justify"] = "center"
        GLineEdit_43["text"] = ""
        GLineEdit_43.place(x=220,y=220,width=320,height=30)
        GLineEdit_43["show"] = "*"

        GLineEdit_210=tk.Entry(self, name="txtConfirmacion")
        GLineEdit_210["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_210["font"] = ft
        GLineEdit_210["fg"] = "#333333"
        GLineEdit_210["justify"] = "center"
        GLineEdit_210["text"] = ""
        GLineEdit_210.place(x=220,y=260,width=320,height=30)
        GLineEdit_210["show"] = "*"
        

        GLabel_170=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_170["font"] = ft
        GLabel_170["fg"] = "#333333"
        GLabel_170["justify"] = "right"
        GLabel_170["text"] = "CONFIRMAR CONTRASEÑA"
        GLabel_170.place(x=0,y=260,width=200,height=30)
        
        GLabel_975=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_975["font"] = ft
        GLabel_975["fg"] = "#333333"
        GLabel_975["justify"] = "right"
        GLabel_975["text"] = "TIPO"
        GLabel_975.place(x=0,y=300,width=320,height=30)
        
        roles = dict(rol.listar())
        if isAdmin:
            cb_roles = ttk.Combobox(self, state="readonly", values=list(roles.values()), name="cbRoles")
        else:
            cb_roles = ttk.Combobox(self, state="disabled", values=list(roles.values()), name="cbRoles")
            cb_roles.set(roles[3])
        cb_roles.place(x=220,y=300,width=320,height=30)
        
        GButton_71=tk.Button(self)
        GButton_71["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_71["font"] = ft
        GButton_71["fg"] = "#000000"
        GButton_71["justify"] = "center"
        GButton_71["text"] = "ACEPTAR"
        GButton_71.place(x=220,y=340,width=150,height=30)
        GButton_71["command"] = self.aceptar
        
        GButton_271=tk.Button(self)
        GButton_271["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_271["font"] = ft
        GButton_271["fg"] = "#000000"
        GButton_271["justify"] = "center"
        GButton_271["text"] = "CANCELAR"
        GButton_271.place(x=390,y=340,width=150,height=30)
        GButton_271["command"] = self.cancelar
        
        if user_id is not None:
            usuario = user.obtener_id(user_id)
            if usuario is None:
               tkMsgBox.showerror(self.master.title(), "Se produjo un error al obtener los datos del usuario, reintente nuevamente")
               self.destroy()
            else:                
                GLineEdit_794.insert(0, usuario[1])
                GLineEdit_522.insert(0, usuario[2])
                GLineEdit_211.insert(0, usuario[3])
                GLineEdit_570.insert(0, usuario[4])
                GLineEdit_690.insert(0, usuario[5])
                GLineEdit_690 ["state"] = "disabled"                              
                cb_roles.set(usuario[7])
    
    def get_value(self, name):
        return self.nametowidget(name).get()

    def get_index(self, name):
        return self.nametowidget(name).current() + 1  


    def cancelar(self):
        self.destroy()
    
        
    def aceptar(self):
        try:            
            apellido = self.get_value("txtApellido")
            nombre = self.get_value("txtNombre")                        
            dni = self.get_value("txtDni")
            email = self.get_value("txtEmail")            
            usuario = self.get_value("txtUsuario")
            contrasenia = self.get_value("txtContraseña")            
            confirmacion = self.get_value("txtConfirmacion")
            rol_id = self.get_index("cbRoles")

            if self.user_id is None:
                if not user.existe(usuario):
                    if contrasenia == confirmacion:                    
                        user.agregar(apellido, nombre, dni, email, usuario, contrasenia, rol_id)
                        tkMsgBox.showinfo(self.master.title(), "Registro agregado!!!!!!")                
                        try:
                            self.master.refrescar()
                        except Exception as ex:
                            print(ex)
                        self.destroy()
                    else:
                        tkMsgBox.showwarning(self.master.title(), "Las contraseñas no coiciden")                 
                else:
                    tkMsgBox.showwarning(self.master.title(), "Usuario existente en nuestros registros")                
            else:
                print("Actualizacion de usuario")
                user.actualizar(self.user_id, apellido, nombre, dni, email, contrasenia, rol_id)  # TODO ver el tema de la contraseña
                tkMsgBox.showinfo(self.master.title(), "Registro modificado!!!!!!")                
                self.master.refrescar()
                self.destroy()      
                
                
        except Exception as ex:
            tkMsgBox.showerror(self.master.title(), str(ex))
            
            

