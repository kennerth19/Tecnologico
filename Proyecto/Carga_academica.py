import tkinter as tk
from tkinter import Toplevel, ttk
from tkinter import messagebox
import sqlite3
from sqlite3 import Error
from rutas import *

class CargaAcademica(tk.Toplevel):
	def __init__(self,master = None):
		super().__init__(master)
		# Config:
		self.title('Carga Académica')
		self.geometry('920x600')
		self.resizable(width=0,height=0)
		self.iconbitmap(uptpc)
		# Menu:
		self.menubar = tk.Menu(self)
		self.filemenu1 = tk.Menu(self.menubar, tearoff=0)
		self.filemenu1.add_command(label="Añadir Unidad Curricular", command='')
		self.filemenu1.add_command(label="Editar Unidad Curricular", command='')
		self.filemenu1.add_command(label="Eliminar Unidad Curricular",command='')
		self.menubar.add_cascade(label="Gestionar Unidades Curriculares", menu=self.filemenu1)
		self.filemenu2 = tk.Menu(self.menubar, tearoff=0)
		self.filemenu2.add_command(label="Manual")
		self.menubar.add_cascade(label="Ayuda", menu=self.filemenu2)
		self.config(menu=self.menubar)
		# Frame:
		self.Frame = ttk.Labelframe(self)
		self.Frame.grid(column=0,row=0,pady=30,padx=10)
		self.LabelCargaAcademica = ttk.Label(self, text='CARGA ARCADÉMICA',font=('Helvetica',14)).place(x=370,y=5)
		self.LabelNombreApellido = ttk.Label(self.Frame, text='Nombre y Apellido:',font=('Helvetica',11)).grid(column=0,row=0 ,padx=5,pady=5)
		self.EntryNombreApellido = ttk.Entry(self.Frame,width=45)
		self.EntryNombreApellido.grid(column=1,row=0,padx=5,pady=5)
		self.LabelCedula = ttk.Label(self.Frame,text='Cédula de Identidad N°:',font=('Helvetica',11)).grid(column=2,row=0,padx=5)
		self.EntryCedula = ttk.Entry(self.Frame,width=45)
		self.EntryCedula.grid(column=3,row=0,padx=5,pady=5)
		self.LabelCategoria = ttk.Label(self.Frame,text='Categoría:',font=('Helvetica',11)).grid(column=0,row=1,padx=5,pady=5)
		self.EntryCategoria = ttk.Entry(self.Frame,width=45)
		self.EntryCategoria.grid(column=1,row=1,padx=5,pady=5)
		self.LabelDecicacion = ttk.Label(self.Frame, text='Dedicación:',font=('Helvetica',11)).grid(column=2,row=1,padx=5,pady=5)
		self.EntryDedicacion = ttk.Entry(self.Frame,width=45)
		self.EntryDedicacion.grid(column=3,row=1,padx=5,pady=5)
		self.LabelTPregrado = ttk.Label(self.Frame,text='Título de Pre-Grado:',font=('Helvetica',11)).grid(column=0,row=2,padx=5,pady=5)
		self.EntryTPregado = ttk.Entry(self.Frame,width=45)
		self.EntryTPregado.grid(column=1,row=2,padx=5,pady=5)
		self.LabelTPosgrado = ttk.Label(self.Frame, text='Título de Post-Grado:',font=('Helvetica',11)).grid(column=2,row=2,padx=5,pady=5)
		self.EntryTPosgrado = ttk.Entry(self.Frame,width=45)
		self.EntryTPosgrado.grid(column=3,row=2,padx=5,pady=5)
		self.LabelDescargaAcademica = ttk.Label(self.Frame, text='Descarga Académica:',font=('Helvetica',11)).grid(column=0,row=3,padx=5,pady=5)
		self.DescargaAcademica = tk.StringVar()
		self.RadioDescargaSi = ttk.Radiobutton(self.Frame, text='Si', value='Si',variable=self.DescargaAcademica).grid(column=1,row=3,padx=5,pady=5)
		self.RadioDescargaNo = ttk.Radiobutton(self.Frame, text='No', value='No',variable=self.DescargaAcademica).grid(column=2,row=3,padx=5,pady=5)
		self.LabelCondicionLaboral = ttk.Label(self.Frame, text='Condición Laboral:',font=('Helvetica',11)).grid(column=0,row=4,padx=5,pady=5)
		self.CondicionLaboral = tk.StringVar()
		self.RadioCondicionO = ttk.Radiobutton(self.Frame, text='Ordinario', value='Ordinario',variable=self.CondicionLaboral).grid(column=1,row=4,padx=5,pady=5)
		self.RadioCondicionC = ttk.Radiobutton(self.Frame, text='Contratado', value='Contratado',variable=self.CondicionLaboral).grid(column=2,row=4,padx=5,pady=5)
		self.LabelRazon = ttk.Label(self.Frame,text='Razón de la descarga:',font=('Helvetica',11)).grid(column=0,row=5,padx=5,pady=5)
		self.EntryRazon = ttk.Entry(self.Frame,width=45)
		self.EntryRazon.grid(column=1,row=5,padx=5,pady=5)
		self.LabelLapso = ttk.Label(self.Frame,text='Lapso Académico:',font=('Helvetica',11)).grid(column=2,row=5,padx=5,pady=5)
		self.EntryLapso = ttk.Entry(self.Frame,width=45)
		self.EntryLapso.grid(column=3,row=5,padx=5,pady=5)        
		self.ButtonRegistrar = ttk.Button(self.Frame,text = 'REGISTRAR DOCENTE', command = self.RegistrarDocente).grid(column=0,row=6,sticky = tk.W + tk.E ,padx=5,pady=5)
		# Treeview:
		self.celdas = ('#1','#2','#3','#4')
		self.tree = ttk.Treeview(self, columns = self.celdas, show='headings')
		self.tree.grid(column=0,row=1, sticky='nsew',padx=5)
		self.tree.heading('#1', text = 'Id')
		self.tree.heading('#2', text = 'Nombre y Apellido')
		self.tree.heading('#3', text = 'Cedula')
		self.tree.heading('#4', text = 'Lapso Académico')
		# # Button:
		self.buttonEd = ttk.Button(self,text = 'EDITAR DOCENTE', command = self.editar).grid(column=0,row=2, sticky = tk.W + tk.E, padx=5)
		self.buttonEl = ttk.Button(self,text = 'ELIMINAR CODENTE', command =self.eliminar).grid(column=0,row=3,sticky = tk.W + tk.E, padx=5)

		self.MostrarDatos()

	def limpiarTabla(self):
		self.DeleteChildren = self.tree.get_children()
		for element in self.DeleteChildren:
			self.tree.delete(element)

	def LimpiarCeldas(self):
		self.EntryNombreApellido.delete(0, tk.END)
		self.EntryCedula.delete(0, tk.END)
		self.EntryCategoria.delete(0, tk.END)
		self.EntryDedicacion.delete(0, tk.END)
		self.EntryTPregado.delete(0, tk.END)
		self.EntryTPosgrado.delete(0, tk.END)
		self.DescargaAcademica.set(0)
		self.CondicionLaboral.set(0)
		self.EntryRazon.delete(0, tk.END)
		self.EntryLapso.delete(0, tk.END)

	def ValidarCeldas(self):
		return len(self.EntryNombreApellido.get()) != 0 and len(self.EntryCedula.get()) != 0 and len(self.EntryCategoria.get()) != 0 and len(self.EntryDedicacion.get()) != 0 and len(self.EntryTPregado.get()) != 0 and len(self.EntryTPosgrado.get()) != 0 and len(self.DescargaAcademica.get()) != 0 and len(self.CondicionLaboral.get()) != 0 and len(self.EntryRazon.get()) != 0 and len(self.EntryLapso.get())      

	def conexion(self,query,parametros = ()):
		try:
			self.con = sqlite3.connect(baseDedatos)
			self.cursor = self.con.cursor()
			self.cursor.execute(query,parametros)
			self.con.commit()
			return self.cursor
		except Error:
			print(Error)

	def TraerDatos(self,query):
		self.mostrar = self.conexion(query)
		self.rows = self.mostrar.fetchall()
		return self.rows

	def MostrarDatos(self):
		self.limpiarTabla()
		self.rows = self.TraerDatos("SELECT Id,NombreApellido,Cedula,LapsoAcademico FROM docente")
		for row in self.rows:
			self.tree.insert('',tk.END,values=row)

	def RegistrarDocente(self):
		if self.ValidarCeldas():
			self.query = 'INSERT INTO docente VALUES (NULL,?,?,?,?,?,?,?,?,?,?)'
			self.parametros = (self.EntryNombreApellido.get(),self.EntryCedula.get(),self.EntryCategoria.get(),self.EntryDedicacion.get(),self.EntryTPregado.get(),self.EntryTPosgrado.get(),self.DescargaAcademica.get(), self.CondicionLaboral.get(), self.EntryRazon.get(), self.EntryLapso.get())
			self.conexion(self.query,self.parametros)
			self.MostrarDatos()
			self.LimpiarCeldas()
			messagebox.showinfo(title='Info', message='Docente Registrado.')
		else:
			messagebox.showwarning(title='Warning', message='Introduzca un valor.')
	
	def selecionarFila(self):
		self.item = self.tree.focus()
		self.data = self.tree.item(self.item)
		self.id = self.data['values'][0]
		return self.id

	def eliminar(self):
		if self.tree.selection():
			if messagebox.askyesno('Delete','¿Desea eliminar al docente selecionado?'):
				self.query = 'DELETE FROM docente WHERE Id = ?'
				self.parametros = self.selecionarFila()
				self.conexion(self.query, (self.parametros,))
				self.MostrarDatos()
				messagebox.showinfo(title='Info', message='Docente eliminado correctamente.')
			else:
				self.MostrarDatos()
		else:
			messagebox.showwarning(title='Wanning', message='Seleccione un docente a eliminar.')

	def editar(self):
		if self.tree.selection():
			if messagebox.askyesno('Edit','¿Desea editar al docente selecionado?'):
				self.seleccion = self.selecionarFila()
				
				self.new = Toplevel()
				self.new.title('Editar Docente')
				self.new.geometry('400x400')
				self.new.resizable(width=0,height=0)
				self.new.iconbitmap(uptpc)
				
				

				self.new.mainloop()		
			else:
				self.MostrarDatos()		
		else: 
			messagebox.showwarning(title='Wanning', message='Seleccione un docente a editar.')