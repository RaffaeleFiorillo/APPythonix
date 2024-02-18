import customtkinter as ctk
from tkinter import messagebox
import os
from src.GUI import Widgets as W
from src.Utils.ScriptToExeConversion import create_executable_from_script
import src.Utils.Validations as V


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # App Appearance -----------------------------------------------------------------------------------------------
        self.geometry("900x450")  # The app has a width of 1100pixels and a height of 600 pixels
        self.resizable(width=False, height=False)  # the app is not resizable
        self.iconbitmap("assets/APPythonix.ico")   # setting the icon of the window
        self.title("APPythonix (Beta)")            # name of the App
        self.configure(background="black")         # background color
        
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
        messagebox.showerror("Error", message)
    
    def _valid_configurations(self, config) -> bool:
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
    
    @staticmethod
    def _get_user_confirmation(confirmation_message):
        return messagebox.askyesno("Confirmation", f"{confirmation_message}.\n Are you sure you want to proceed?")
    
    def _obtain_all_necessary_user_confirmation(self, config) -> bool:
        if not config["one_file"] and os.path.exists(f"{config['destination_folder']}/{config['file_name']}"):
            message = "You are creating the app in the form of a folder (*.exe/.app* + dependencies).\n" \
                      "A folder with the same name already exists in the destination directory.\n" \
                      "To avoid conflicts, the existing folder will be deleted and replaced by the new one"
            if not self._get_user_confirmation(message):
                return False
        return True
    
    def _get_configurations(self):
        # 1st-> Group the configurations dispersed from all the widgets of in one dictionary
        config = self.configuration_options.get_configurations()
        
        # 2nd-> Make adjustments to the data and prepare it for use
        config["script_path"] = self.script_selector.get_value()
        script_folder = os.path.dirname(config["script_path"])
        if config["file_name"] == "":
            _, file_name = os.path.split(config["script_path"])
            config["file_name"] = file_name.split('.')[0]  # script name without the extension
            
        config["script_folder"] = script_folder
        config["destination_folder"] = config["new_path"] if config["new_path"] != "" else script_folder
        
        # 3rd-> Return the configurations
        return config
    
    def _convert_script(self):
        # 1st-> Obtain the configuration provided by the user to create the App
        config = self._get_configurations()
        
        # 2nd-> Validate that everything is correct with the configuration and avoid any potential conflict
        if not self._valid_configurations(config) or not self._obtain_all_necessary_user_confirmation(config):
            return None
        
        # 3rd-> Create the App
        try:
            create_executable_from_script(config)
        except Exception as e:
            self._show_error_popup(str(e))
