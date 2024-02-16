# APPythonix
A tool designed to convert Python scripts to .exe files (Windows) or .app (Mac). It comes with a simple, compact and modern looking GUI.

# Features:
 - Converts a python project into an exe/app file;
 - You can choose to delete unecessary files created during the process of conversion, automatically, after the conversion is over (You can select which file to keep or not) ;
 - Multiple ways to create the executable:
     - As a compact single file or with all dependencies separated;
     - with/without console attached;
     - Require admin privileges for execution (Windows only);
 - You can choose where to create the executable (the directory of the script is the default);

# Important Notes:
APPythonix is built using the Pyinstaller tool. For this reason, it comes with the same limitations. If you find yourself unable to use this tool, you can explore the Pyinstaller documentation in order to find a solution.
APPythonix is meant to be a simple and compact tool to use in the vast majority of cases, therefore it does not provide the full range of solutions and features available in Pyinstaller.  Future version of APPythonix will try to provide more complete solutions and will be evolving along side with Pyinstaller.

# Concept Design
The image bellow represents the *concept desingn* that I created as a guide for APPythonix. The frameworks used to create it may turn the final product very different. Maybe some day I will be able to accurately replicate the desing.
![GUI demo](https://github.com/RaffaeleFiorillo/APPythonix/assets/75253335/d59a921e-c893-4d96-a19f-f53f9d1a5e48)

# Tools and Frameworks:
 - [Pyinstaller](https://github.com/pyinstaller/pyinstaller): For the creation of the .exe/.app files based on python code;
 - [Tkinter](https://github.com/topics/tkinter-python): For the GUI;
 - [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter): For the GUI (more specifically, to create a more modern-appearing GUI);
