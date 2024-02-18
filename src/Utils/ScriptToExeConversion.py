import os
import shutil as shut
import subprocess

"""os.chdir(script_folder)  # Change to the script directory
os.system(command)  # Execute the command"""


def delete_existing_app(file_name, destination_folder, file_extension, new_app_is_file):
	# 1st-> Getting the app path in order to find out if an app with the same name already exists.
	app_path = os.path.join(destination_folder, f"{file_name}")
	app_path += f".{file_extension}" if new_app_is_file else ""
	
	print(f"Searching existing app in: {destination_folder}")
	# 2nd-> Delete the old (existing) version of the app, if it exists
	if os.path.exists(app_path):
		os.remove(app_path) if new_app_is_file else shut.rmtree(app_path)
		print("############ Existing app Deleted #############")
	else:
		print(f"######## {file_name}.{file_extension} doesn't exist in destination folder ########")


# -------------------------------------------- Managing Other Files ----------------------------------------------------
def manage_file(file_name, is_delete, source_folder, destination_folder):
	if is_delete:
		os.remove(f"{destination_folder}/{file_name}.spec")
		print("########## Specs (File) Deleted ############")
		return None
	
	# there is no need to move the file if the source folder is the same as the destination folder
	if source_folder == destination_folder:
		return None
	
	try:
		shut.move(f"{source_folder}/{file_name}.spec", destination_folder)
		print("########### Specs (File) Moved #############")
	except Exception as e:
		print(f"Error moving *{source_folder}/{file_name}.spec* folder: {str(e)}")


def manage_folder(folder_name, is_delete, source_folder, destination_folder):
	if is_delete:
		shut.rmtree(f"{destination_folder}/{folder_name.lower()}")
		print(f"######### {folder_name} (Folder) Deleted ############")
		return None
	
	# there is no need to move the folder if the source folder is the same as the destination folder
	if source_folder == destination_folder:
		return None
	
	try:
		shut.move(source_folder, destination_folder)
		print(f"########## {folder_name} (Folder) Moved #############")
	except Exception as e:
		print(f"Error moving {folder_name} folder: {str(e)}")


# delete the unnecessary files created in the previous step
def manage_other_files(conf, script_folder, destination_folder):
	print("############### Managing Other Files ###############")
	if conf["del_specs"]:
		os.remove(f"{destination_folder}/{conf['file_name']}.spec")
		print("########## Specs (File) Deleted ############")
	manage_folder("Dist", conf["del_dist"], script_folder, destination_folder)
	manage_folder("temp_files", True, script_folder, destination_folder)
	print("################# Other Files Managed #################")


# ---------------------------------------- Creation of the executable --------------------------------------------------
def create_executable(conf, destination_folder, file_extension):
	print("############### Creating File ###############")
	# 1st-> The parameters to provide in order to create the app according to the user's configurations
	parameters = create_parameters_from_configurations(conf, destination_folder)
	command = " ".join(parameters)
	
	# 2nd-> Use pyinstaller to create the app
	try:
		print(command)
		subprocess.call(f"python -m PyInstaller {command}")
	# An Error should occur saying that the output directory is not empty. This only happens when the app/exe is created
	# without the option --onefile. It is nothing to worry about and is managed later on in this function
	except FileNotFoundError:
		print("Some Problem with Un-existing files was avoided.")
		# Later versions may have to manage some special cases. Right such cases have not yet risen
		pass
	
	# 3rd-> Move the app in the destination folder specified by the user (by default is the script's folder)
	# If the app is created as one file, the app is a file
	if conf["one_file"]:
		app_path = f"{destination_folder}/dist/{conf['file_name']}.{file_extension}"
	# In this case, the app is a folder with executable + dependencies, created in the dist path
	else:
		app_path = f"{destination_folder}/dist/{conf['file_name']}"
	shut.move(app_path, destination_folder)
	
	print("############### File Created ###############")


def create_parameters_from_configurations(conf, destination_folder):
	print("############ Creating Parameters ############")
	parameters = []
	
	if conf["file_name"] != "":
		parameters.append(f'--name="{conf["file_name"]}"')
	else:
		script_folder, script_name = os.path.split(conf["script_path"])
		parameters.append(f"--name={script_name.split('.')[0]}")
	
	# Defining the Icon image
	parameters.append(f'--icon="{os.path.normpath(conf["icon_path"])}"') if conf["icon_path"] != "" else None
	# Making the executable come in the form of one_file or one file and the required dependencies
	parameters.append("--onefile") if conf["one_file"] else None
	# Defining if the executable comes with a prompt console or not
	parameters.append("--noconsole") if conf["no_console"] else None
	# Defining if a user should upgrade to administrator upon execution
	parameters.append("--uac-admin") if conf["admin_only"] else None
	# Delete the build folder after the process has finished if the user wants so
	parameters.append("--clean") if conf["del_build"] else None
	# Trigger a necessary error to avoid some problems
	parameters.append("-y") if conf["del_dist"] and conf["one_file"] else None
	
	workpath = os.path.normpath(f"{destination_folder}/temp_files")
	parameters.append(f'--workpath="{workpath}"')
	distpath = os.path.normpath(f"{destination_folder}/dist")
	parameters.append(f'--distpath="{distpath}"')
	specpath = os.path.normpath(f"{destination_folder}")
	parameters.append(f'--specpath="{specpath}"')
	
	parameters.append(f'"{os.path.normpath(conf["script_path"])}"')
	
	print("############ Parameters Created ############")
	return parameters


# ----------------------------------------------- Main Function --------------------------------------------------------
def create_executable_from_script(conf):
	print("############### Conversion has Started ###############")
	# 1st-> Making sure there is not an existing file in same folder where the .exe/.app will be created
	delete_existing_app(conf["file_name"], conf["destination_folder"], conf["file_extension"], conf["one_file"])
	
	# 2nd-> Converting the .py script into a .exe/.app file
	create_executable(conf, conf["destination_folder"], conf["file_extension"])
	
	# 3rd-> Deleting files created during the conversion process (only the ones chosen by the user)
	manage_other_files(conf, conf["script_folder"], conf["destination_folder"])
	
	print("########## Conversion Successfully Completed ##########\n")

# ----------------------------------------- Configuration Description --------------------------------------------------
# The parameter *conf* contains all the necessary data to build the app according to the user configurations in the GUI.
# It comes as a dictionary with the following structure:

# 'file_name': str,      -> Name of the .exe/.app file (The extension is not included)
# 'file_extension': str, -> Extension of the executable file (.exe for Windows and .app for Mac)

# 'script_path': str,        -> Absolute path to the python script to be converted
# 'script_folder': str,      -> Absolute path to the folder where the python script is located
# 'destination_folder': str, -> Absolute path to the folder where the user wants the app to be created
# 'icon_path': str,          -> Absolute path to the .ico file to be used as the app's icon image

# 'one_file': bool,   -> Defines if the app should be created as a folder[executable+dependencies] or unique file
# 'no_console': bool, -> Defines if the app should have its command prompt attached upon execution
# 'admin_only': bool, -> Defines if the app should ask for Elevation to Admin upon execution (Windows only)

# 'del_specs': bool, -> Flag to know if the user wants the .specs file to be deleted after creating the app
# 'del_dist': bool,  -> Flag to know if the user wants the dist folder to be deleted after creating the app
# 'del_build': bool  -> Flag to know if the user wants the build folder to be deleted after creating the app
