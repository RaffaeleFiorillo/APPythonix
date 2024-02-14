import tkinter as tk
import customtkinter as ctk
from customtkinter import filedialog


class ScriptSelector:
	def __init__(self, app, x, y):
		# Script Path (Directory) Entry aka -> spe ---------------------------------------------------------------------
		spe_label_font = ("Arial", 22, "bold")
		self.spe_label = ctk.CTkLabel(app, text="Select Your Python Script:", font=spe_label_font)
		self.spe_label.place(x=x, y=y)
		
		spe_font = ("Arial", 20)
		spe_width = 55  #
		self.script_path_entry = tk.Entry(app, bg="#454545", fg="#AAAAAA", bd=0, font=spe_font, width=spe_width)
		self.script_path_entry.place(x=x, y=y+spe_label_font[1]*2)
		
		# Browse Button ------------------------------------------------------------------------------------------------
		self.browse_button = ctk.CTkButton(app, text="Browse", command=self.browse_file, width=90)
		self.browse_button.place(x=x+650, y=y+32.4)
	
	def browse_file(self):
		file_path = filedialog.askopenfilename()
		self.script_path_entry.delete(0, ctk.END)
		self.script_path_entry.insert(0, file_path)
