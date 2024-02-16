import customtkinter as ctk
import tkinter as tk
import src.Utils as U


class ConversionButton:
	def __init__(self, app, x, y, convertion_function):
		self.width, self.height = 200, 60
		
		# Button Border ------------------------------------------------------------------------------------------------
		self.canvas = tk.Canvas(background="#00ffff")
		self.canvas.place(x=x+80, y=y+85, width=self.width+70, height=self.height+35)
		
		# Button -------------------------------------------------------------------------------------------------------
		conv_b_font = ("Arial", 30, "bold")
		self.conversion_button = ctk.CTkButton(app, text="CREATE", font=conv_b_font,
		                                       command=convertion_function,
		                                       width=self.width, height=self.height)
		self.conversion_button.place(x=x, y=y)
