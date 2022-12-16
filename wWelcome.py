import tkinter as tk
import tkinter.font as tkFont
from wLogin import Login
from dal.db import Db

class Welcome:
    def __init__(self, root):
        self.root = root        
        root.title("WELCOME TO CINEMAR")        
        width=500
        height=100
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_898=tk.Button(root)
        GButton_898["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=18)
        GButton_898["font"] = ft
        GButton_898["fg"] = "#000000"
        GButton_898["justify"] = "center"
        GButton_898["text"] = "BIENVENIDOS A CINEMAR"
        GButton_898.place(x=0,y=0,width=500,height=100)
        GButton_898["command"] = self.abrir_login
        
    def abrir_login(self):
        Login(self.root)        
    
if __name__ == "__main__":
    Db.crear_tablas()
    Db.poblar_tablas() 
    root = tk.Tk()
    root.iconbitmap(default="cinemark.ico")    
    app = Welcome(root)    
    root.mainloop()
    


