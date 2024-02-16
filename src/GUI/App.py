import customtkinter as ctk
from tkinter import messagebox
from src.GUI import Widgets as W
from src.Utils.ScriptToExeConversion import create_executable_from_script
import src.Utils.Validations as V


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # App Appearance -----------------------------------------------------------------------------------------------
        self.geometry("900x450")  # The app has a width of 1100pixels and a height of 600 pixels
        self.resizable(width=False, height=False)  # the app is not resizable
        self.iconbitmap("assets/APPythonix.ico")  # setting the icon of the window
        self.title("APPythonix (Beta)")
        self.configure(background="black")
        
        # Elements for Selecting Python Script -------------------------------------------------------------------------
        self.script_selector = W.ScriptSelector(self, 100, 15)
        
        # Elements for App/Exe Configuration ---------------------------------------------------------------------------
        self.configuration_options = W.ConfigurationOptions(self, 10, 130)
        
        # Elements for Info --------------------------------------------------------------------------------------------
        self.info_display = W.InfoDisplay(self, 580, 130)
        
        # Conversion Button (the main button) --------------------------------------------------------------------------
        W.ConversionButton(self, 360, 380, self._convert_script)

    @staticmethod
    def _show_error_popup(message):
        # ctk.CTk().withdraw()  # Hide the main window
        messagebox.showerror("Error", message)
    
    def _valid_configurations(self, config):
        print(config)
        if not V.is_valid_python_script_path(config["script_path"]):
            self._show_error_popup("Invalid python script path. Either the script doesn't exist or it isn't a .py file")
            return False
        if not V.is_valid_file_name(config["file_name"]):
            self._show_error_popup("Invalid Executable Name!")
            return False
        if not V.is_valid_icon_image_path(config["icon_path"]):
            self._show_error_popup("Invalid icon image path. Either the image doesn't exist or it isn't a .ico file.")
            return False
        if not V.is_valid_new_path(config["new_path"]):
            self._show_error_popup("Invalid path. Either the path doesn't exist or it isn't available.")
            return False
        return True
        
    def _convert_script(self):
        config = self.configuration_options.get_configurations()
        config["script_path"] = self.script_selector.get_value()
        
        if self._valid_configurations(config):
            try:
                create_executable_from_script(config)
            except Exception as e:
                print(f"Exception occurred: {str(e)}")
