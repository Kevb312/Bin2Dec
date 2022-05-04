from tkinter import ttk
from tkinter import *
from tkinter import messagebox

class Convertidor:

	def __init__(self, window):

		#Inicializadores
		self.wind = window
		self.wind.title('Conversor binario a decimal')

		#Contenedor frame
		frame = LabelFrame(self.wind, text = 'Ingresar binario')
		frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

		#Name input
		Label(frame, text = 'Número: ').grid(row = 1, column = 0)
		self.name = Entry(frame)
		self.name.focus()
		self.name.grid(row = 1, column = 1)

		#Boton convertir
		ttk.Button(frame, text = 'Convertir', command = self.convertir).grid(row = 3, columnspan = 2, sticky = W + E)

		#Mensajes de salida
		self.message = Label(text = '', fg = 'red')
		self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

		self.message2 = Label(text = '', fg = 'green')
		self.message2.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

	def convertir(self):
		if not self.name.get():
			self.message['text'] = 'El número binario no puede ir vacio'
			print(self.name.get())
			messagebox.showerror('Error', 'El número no puede ir vacio.')

		else:
			numeroBinario = self.name.get()

			if len(numeroBinario) >= 8:
				print("Solo puede introducir 8 caracteres.")
				messagebox.showinfo('Advertencia', 'Solo puede introducir 8 caracteres.')
			else:
				try:
					print(int(numeroBinario,2))
					self.message2['text'] = 'El número en decimal es: {}'.format(int(numeroBinario,2))
					messagebox.showinfo('Éxito', 'Número calculado correctamente.')
				except:
					print("No es un número binario")
					self.message['text'] = 'No es un número binario'
					self.name.focus()
					messagebox.showerror('Error', 'El número introducido no es binario.')

if __name__ == '__main__':
    window = Tk()
    application = Convertidor(window)
    window.mainloop()