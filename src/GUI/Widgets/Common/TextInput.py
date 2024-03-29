import tkinter as tk
import customtkinter as ctk
from customtkinter import filedialog
from .InfoHoover import InfoHoover
from .FolderBrowser import FolderBrowser
from .EraseEntryButton import EraseEntryButton


class TextInput:
	def __init__(self, container, label, x, y, info, is_optional=False, enable_browsing=False, is_file_browsing=False):
		self.te_width = 56
		
		# Script Path (Directory) Entry aka -> spe ---------------------------------------------------------------------
		te_label_font = ("Arial", 12, "bold")
		self.te_label = ctk.CTkLabel(container, text=label, font=te_label_font, bg_color="black")
		
		# Text Input Area (te) -----------------------------------------------------------------------------------------
		te_font = ("Arial", 12, "bold")
		self.text_entry = tk.Entry(container, bg="#454545", fg="white", bd=0, font=te_font, width=self.te_width,
		                           insertbackground="white")
		self.text_entry.place(x=x, y=y+23)
		
		# Buttons ------------------------------------------------------------------------------------------------------
		if enable_browsing:
			browsing_function = self.browse_file if is_file_browsing else self.browse_folder
			self.browse_button = FolderBrowser(container, x+433, y, browsing_function)
		self.erase_button = EraseEntryButton(container, x + 460, y, self.erase_entry)
		self.info_button = InfoHoover(container, x+485, y, info)
		
		# Making the Widget Optional -----------------------------------------------------------------------------------
		if is_optional:
			self.toggle_button = ctk.CTkSwitch(container, text="", width=15, height=10, switch_width=25, switch_height=10,
			                                   command=self.toggle_widget_state)
			self.toggle_button.place(x=x-5, y=y-53)
			self.te_label.place(x=x+33, y=y-58)
			self.toggle_widget_state()  # the optional widget is by default disabled
		else:
			self.toggle_button = None
			self.te_label.place(x=x+10, y=y-45)

	def browse_file(self):
		file_path = filedialog.askopenfilename()
		self.text_entry.delete(0, ctk.END)
		self.text_entry.insert(0, file_path)
		
	def browse_folder(self):
		folder_path = filedialog.askdirectory()
		self.text_entry.delete(0, tk.END)
		self.text_entry.insert(0, folder_path)
		
	def toggle_widget_state(self):
		if self.toggle_button.get() == 0:
			self.text_entry.config(state="disabled", disabledbackground="#222222")
			self.browse_button.disable()
			self.erase_button.disable()
		else:
			self.text_entry.config(state="normal", disabledbackground="")
			self.browse_button.enable()
			self.erase_button.enable()
	
	def erase_entry(self):
		self.text_entry.delete(0, tk.END)
	
	def get_value(self):
		if self.toggle_button is not None:
				if self.toggle_button.get() == 0:
					return ""
		return self.text_entry.get()
