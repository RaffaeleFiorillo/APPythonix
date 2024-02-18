import customtkinter as ctk
import tkinter as tk


class CustomRadioButton:
	FONT = ("Arial", 10)
	
	def __init__(self, frame, row: int, column: int, value_holder: tk.StringVar, value: str):
		self.trace_button = ctk.CTkRadioButton(frame, text=value, variable=value_holder, value=value,
		                                       radiobutton_height=12, radiobutton_width=12, font=self.FONT)
		self.trace_button.grid(row=row, column=column, padx=0, pady=0)
