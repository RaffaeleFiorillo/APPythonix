import customtkinter as ctk
from src.GUI import Widgets as W


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # App Appearance -----------------------------------------------------------------------------------------------
        self.geometry("900x450")  # The app has a width of 1100pixels and a height of 600 pixels
        self.resizable(width=False, height=False)  # the app is not resizable
        self.iconbitmap("assets/APPythonix.ico")  # setting the icon of the window
        self.title("APPythonix (Beta)")
        
        # Elements for Selecting Python Script -------------------------------------------------------------------------
        self.grid_columnconfigure(0, weight=1)
        self.script_selector = W.ScriptSelector(self, 100, 15)
        
        # Elements for App/Exe Configuration ---------------------------------------------------------------------------
        
        # Elements for Info --------------------------------------------------------------------------------------------
        pass
