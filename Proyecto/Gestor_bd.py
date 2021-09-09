import tkinter as tk
from tkinter import ttk
import sqlite3
from sqlite3 import Error
from typing import Text
from rutas import *

class Gestor(tk.Toplevel):
    def __init__(self,master):
        super().__init__(master)
        # Config:
        self.title('Gestionar Tablas')
        self.geometry('400x415')
        self.resizable(width=0, height=0)
        self.iconbitmap(uptpc)
        
        # create a notebook
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, expand=True)

        # create frames
        self.noteCohorte = ttk.Frame(self.notebook, width=400, height=400)
        self.noteTrayecto = ttk.Frame(self.notebook, width=400, height=400)
        self.noteTrimestre = ttk.Frame(self.notebook, width=400, height=400)
        self.noteSeccion = ttk.Frame(self.notebook, width=400, height=400)
        self.noteUnidadCurricular = ttk.Frame(self.notebook, width=400, height=400)

        # create frames
        self.noteCohorte.pack(fill='both', expand=True)
        self.noteTrayecto.pack(fill='both', expand=True)
        self.noteTrimestre.pack(fill='both', expand=True)
        self.noteSeccion.pack(fill='both', expand=True)
        self.noteUnidadCurricular.pack(fill='both', expand=True)

        # add frames to notebook
        self.notebook.add(self.noteCohorte, text='Cohorte')
        self.notebook.add(self.noteTrayecto, text='Trayecto')
        self.notebook.add(self.noteTrimestre, text='Trimestre')
        self.notebook.add(self.noteSeccion, text='seccion')
        self.notebook.add(self.noteUnidadCurricular, text='Unidad Curricular')
        
        # Pantalla Cohorte
        self.frameCohorte = ttk.LabelFrame(self.noteCohorte)
        self.frameCohorte.grid(column=0,row=0,pady=10)

        # Cohorte frame
        self.labelCohorte = ttk.Label(self.frameCohorte,text='Cohorte').grid(column=0,row=0)
        self.entryCohorte = ttk.Entry(self.frameCohorte,width=45)
        self.entryCohorte.grid(column=1,row=0,padx=5,pady=5)
        self.buttonCohorte = ttk.Button(self.frameCohorte, text='Registrar Cohorte').grid(row=1,column=0)

        # Cohorte Tabla
        self.celdasCohorte = ('#1','#2')
        self.treeCohorte = ttk.Treeview(self.noteCohorte,columns = self.celdasCohorte, show='headings')
        self.treeCohorte.grid(column=0,row=1, sticky='nsew')
        self.treeCohorte.heading('#1', text = 'Id')
        self.treeCohorte.heading('#2', text = 'Cohorte')

        # Cohorte Botones
        self.buttonEditarCohorte = ttk.Button(self.noteCohorte,text = 'EDITAR COHORTE', command ='').grid(column=0,row=2, sticky = tk.W + tk.E)
        self.buttonEliminarCohorte = ttk.Button(self.noteCohorte,text = 'ELIMINAR COHORTE', command ='').grid(column=0,row=3,sticky = tk.W + tk.E)		
        
        # Pantalla Trayecto
        self.frameTrayecto = ttk.LabelFrame(self.noteTrayecto)
        self.frameTrayecto.grid(column=0,row=0,pady=10)

        # Trayecto frame
        self.labelCohorte = ttk.Label(self.frameTrayecto,text='Trayecto').grid(column=0,row=0)
        self.entryCohorte = ttk.Entry(self.frameTrayecto,width=45)
        self.entryCohorte.grid(column=1,row=0,padx=5,pady=5)
        self.buttonCohorte = ttk.Button(self.frameTrayecto, text='Registrar Trayecto').grid(row=1,column=0)

        # Trayecto Tabla
        self.celdasTrayecto = ('#1','#2')
        self.treeTrayecto = ttk.Treeview(self.noteTrayecto,columns = self.celdasCohorte, show='headings')
        self.treeTrayecto.grid(column=0,row=1, sticky='nsew')
        self.treeTrayecto.heading('#1', text = 'Id')
        self.treeTrayecto.heading('#2', text = 'Trayecto')

        # Trayecto Botones
        self.buttonEditarTrayecto = ttk.Button(self.noteTrayecto,text = 'EDITAR TRAYECTO', command ='').grid(column=0,row=2, sticky = tk.W + tk.E)
        self.buttonEliminarTrayecto = ttk.Button(self.noteTrayecto,text = 'ELIMINAR TRAYECTO', command ='').grid(column=0,row=3,sticky = tk.W + tk.E)      

        # Pantalla Trimestre
        # Pantalla Seccion
        # Pantalla Unidad Curricular