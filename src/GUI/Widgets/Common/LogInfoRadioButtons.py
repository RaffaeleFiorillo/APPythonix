import customtkinter as ctk
import tkinter as tk
from .CustomRadioButton import CustomRadioButton


class LogInfoRadioButton(ctk.CTkScrollableFrame):
	def __init__(self, app, x, y):
		super().__init__(app, width=100, height=90)
		self._label = ctk.CTkLabel(app, text="Log Information Level", font=("Arial", 11, "bold"))
		self._label.configure(height=20)
		self._label.place(x=x, y=y)
		self._scrollbar.configure(height=30)
		
		self.radio_value_holder = tk.StringVar(value="INFO")
		
		values = ["INFO", "TRACE", "DEBUG", "WARN", "DEPRECATION", "ERROR", "FATAL"]
		[CustomRadioButton(self, i, 0, self.radio_value_holder, v) for i, v in enumerate(values)]
		
		self.place(x=x, y=y+20)
		
	def get_value(self) -> str:
		return self.radio_value_holder.get()

	
"""
	self.info_button = radio_buttons[0]
	self.trace_button = radio_buttons[1]
	self.debug_button = radio_buttons[2]
	self.warn_button = radio_buttons[3]
	self.depr_button = radio_buttons[4]
	self.error_button = radio_buttons[5]
	self.fatal_button = radio_buttons[6]
"""