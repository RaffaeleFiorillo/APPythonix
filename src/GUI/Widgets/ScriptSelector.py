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
		self.script_path_entry = tk.Entry(app, bg="#454545", fg="#AAAAAA", bd=0, font=spe_font, width=spe_width,
		                                  insertbackground="white")
		self.script_path_entry.place(x=x, y=y+spe_label_font[1]*2)
		
		# Browse Button ------------------------------------------------------------------------------------------------
		self.browse_button = ctk.CTkButton(app, text="Browse", command=self._browse_file, width=90, fg_color="#ffca0c",
		                                   text_color="#aa5500", border_width=3, border_color="#aa5500",
		                                   font=("Arial", 20, "bold"))
		self.browse_button.place(x=x+650, y=y+29)
		self.browse_button.bind("<Enter>", self._on_enter)
		self.browse_button.bind("<Leave>", self._on_leave)
	
	def _browse_file(self):
		file_path = filedialog.askopenfilename()
		self.script_path_entry.delete(0, ctk.END)
		self.script_path_entry.insert(0, file_path)
	
	def _on_enter(self, event):
		self.browse_button.configure(fg_color="#aa5500", text_color="#ffca0c", border_color="#ffca0c")
	
	def _on_leave(self, event):
		self.browse_button.configure(fg_color="#ffca0c", text_color="#aa5500", border_color="#aa5500")
		
	def get_value(self):
		return self.script_path_entry.get()
