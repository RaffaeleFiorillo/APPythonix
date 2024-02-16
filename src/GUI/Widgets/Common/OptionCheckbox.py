import customtkinter as ctk
from .InfoHoover import InfoHoover


class OptionCheckbox:
	def __init__(self, app, x, y, label, info):
		self.info_button = InfoHoover(app, x, y, info)
		
		self.checkbox = ctk.CTkCheckBox(app, text=label, checkbox_width=20, checkbox_height=20)
		self.checkbox.place(x=x+12, y=y-70)
		
	def get_value(self) -> bool:
		return self.checkbox.get() == 1
		