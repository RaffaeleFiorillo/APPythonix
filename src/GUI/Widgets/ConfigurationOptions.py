import platform
import tkinter as tk
import src.GUI.Widgets.Common as C


class ConfigurationOptions:
	def __init__(self, app, x, y):
		self.width, self.height = 200, 200
		
		self.canvas = tk.Canvas(background="black")
		self.canvas.place(x=-5, y=y, width=570, height=360)
		
		# Create widgets to put inside the frame
		label_font = ("Arial", 20, "bold")
		label1 = tk.Label(app, text="Configurations", font=label_font, fg="black", bg="white")
		label1.place(x=x+180, y=y-20)
		
		# Text Inputs --------------------------------------------------------------------------------------------------
		name_input_info = "The name of the .exe/.app file. If left empty, the name will be the same as the script's."
		self.app_name_input = C.TextInput(app, "Executable Name", x+20, y+25, name_input_info)
		self.app_name_input.te_label.place(y=y-10)
		
		icon_input_info = "The path to the .ico file that will be used as the icon of the .exe/.app." \
		                  "\nBy default uses the pyinstaller default icon."
		self.app_icon_dir_input = C.TextInput(app, "Executable Icon", x+20, y+78, icon_input_info,
		                                      enable_browsing=True, is_file_browsing=True)
		
		n_dir_info = "You can select a new location in case you want the .exe/.app file to be created somewhere else." \
                     "\nBy default, the file is created in the same folder as the script."
		self.app_new_dir_input = C.TextInput(app, "Move to Different Folder:", x+20, y+130, n_dir_info,
		                                     enable_browsing=True, is_optional=True)
		
		# Checkboxes ---------------------------------------------------------------------------------------------------
		one_file_info = "The executable/app is created in the form of a single file."
		self.one_file_checkbox = C.OptionCheckbox(app, x+20, y+200, "One File", one_file_info)
		
		no_console_info = "There will be no console (prompt) window upon execution."
		self.no_console_checkbox = C.OptionCheckbox(app, x+20, y+240, "No Console", no_console_info)
		self.no_console_checkbox.info_button.button.place(y=y+250)
		
		if platform.system() == "Windows":
			admin_only_info = "Administrator privileges are required upon execution (Windows only)"
			self.admin_only_checkbox = C.OptionCheckbox(app, x + 20, y + 280, "Admin Only", admin_only_info)
			self.admin_only_checkbox.info_button.button.place(y=y + 300)
		
		delete_specs_info = "Deletes the 'specs' file after the conversion of the script has completed."
		self.delete_specs_checkbox = C.OptionCheckbox(app, x+150, y+200, "Delete specs (File)", delete_specs_info)
		self.delete_specs_checkbox.info_button.button.place(x=x+180)
		
		"""delete_dist_info = "Deletes the 'dist' folder after the conversion of the script has completed."
		self.delete_dist_checkbox = C.OptionCheckbox(app, x+150, y+240, "Delete dist (Folder)", delete_dist_info)
		self.delete_dist_checkbox.info_button.button.place(x=x+180, y=y+250)
		
		delete_build_info = "Deletes the 'build' folder after the conversion of the script has completed."
		self.delete_build_checkbox = C.OptionCheckbox(app, x+150, y+280, "Delete build (Folder)", delete_build_info)
		self.delete_build_checkbox.info_button.button.place(x=x+180, y=y+300)"""
		
	def get_configurations(self) -> {str: object}:
		return {
			"file_name": self.app_name_input.get_value(),
			"icon_path": self.app_icon_dir_input.get_value(),
			"new_path": self.app_new_dir_input.get_value(),
			"one_file": self.one_file_checkbox.get_value(),
			"no_console": self.no_console_checkbox.get_value(),
			"admin_only": False if platform.system() != "Windows" else self.admin_only_checkbox.get_value(),
			"del_specs": self.delete_specs_checkbox.get_value(),
			"del_dist": True,  # self.delete_dist_checkbox.get_value(),
			"del_build": True,  # self.delete_build_checkbox.get_value(),
			"file_extension": "exe" if platform.system() == "Windows" else "app"
		}
		