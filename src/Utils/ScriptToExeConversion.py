import os
import platform
import shutil as shut
import PyInstaller.__main__ as PyinstallerApplier


def delete_existing_executable(file_name, destination_folder, file_extension):
	file_path = os.path.join(destination_folder, f"{file_name}.{file_extension}")
	
	# delete the old version of the .exe/.app if it exists
	if os.path.exists(file_path):
		os.remove(f'{destination_folder}/{file_name}.{file_extension}')
		print("\n ############ Existing .exe/.app Deleted #############\n")
	else:
		print(f"\n ######## {file_name}.{file_extension} doesn't exist in destination folder ######## \n")


# -------------------------------------------- Managing Other Files ----------------------------------------------------
def manage_file(file_name, is_delete, source_folder, destination_folder):
	if is_delete:
		os.remove(f"{source_folder}/{file_name}.spec")
		print("\n ########## Specs (File) Deleted ############\n")
		return None
	
	# there is no need to move the file if the source folder is the same as the destination folder
	if source_folder == destination_folder:
		return None
	
	try:
		shut.move(f"{source_folder}/{file_name}.spec", destination_folder)
		print("\n ########### Specs (File) Moved #############\n")
	except Exception as e:
		print(f"Error moving *{source_folder}/{file_name}.spec* folder: {str(e)}")


def manage_folder(folder_name, is_delete, source_folder, destination_folder):
	if is_delete:
		shut.rmtree(f"{source_folder}/{folder_name.lower()}")
		print(f"\n ######### {folder_name} (Folder) Deleted ############\n")
		return None
	
	# there is no need to move the folder if the source folder is the same as the destination folder
	if source_folder == destination_folder:
		return None
	
	try:
		shut.move(source_folder, destination_folder)
		print(f"\n ########## {folder_name} (Folder) Moved #############\n")
	except Exception as e:
		print(f"Error moving {folder_name} folder: {str(e)}")


# delete the unnecessary files created in the previous step
def manage_other_files(conf, script_folder, destination_folder):
	print("\n ############### Managing Other Files ###############\n")
	manage_file(conf['file_name'], conf["del_specs"], script_folder, destination_folder)
	manage_folder("Dist", conf["del_dist"], script_folder, destination_folder)
	manage_folder("Build", conf["del_build"], script_folder, destination_folder)
	print("\n ############### Other Files Managed ###############\n")


# ---------------------------------------- Creation of the executable --------------------------------------------------
def create_executable(conf, script_folder, destination_folder, file_extension):
	print("\n ############### Creating File ###############\n")
	parameters = create_parameters_from_configurations(conf)
	
	# PyinstallerApplier.run(parameters)
	
	# Move .exe/.app file from where it is to destination folder
	exe_app_file_path = f"{script_folder}/dist/{conf['file_name']}.{file_extension}"
	shut.move(exe_app_file_path, destination_folder)
	
	print("\n ############### File Created ###############\n")


def create_parameters_from_configurations(conf):
	print("\n ############ Creating Parameters ############\n")
	parameters = [conf["script_path"]]
	
	if conf["file_name"] != "":
		parameters.append(f"--name={conf['file_name']}")
	else:
		script_folder, script_name = os.path.split(conf["script_path"])
		parameters.append(f"--name={script_name}")
	
	# Defining the Icon image
	parameters.append(f"--icon={conf['icon_path']}") if conf["icon_path"] != "" else None
	# Making the executable come in the form of one_file or one file and the required dependencies
	parameters.append("--onefile") if conf["one_file"] else None
	# Defining if the executable comes with a prompt console or not
	parameters.append("--noconsole") if conf["no_console"] else None
	# Defining if a user should upgrade to administrator upon execution
	parameters.append("--uac-admin") if conf["admin_only"] else None
	
	print("\n ############ Parameters Created ############\n")
	print(parameters)
	return parameters


# ----------------------------------------------- Main Function --------------------------------------------------------
# conf = {
# 'script_path': str,
# 'file_name': str, 'icon_path': str, 'new_path': str,
# 'one_file': bool, 'no_console': bool, 'admin_only': bool,
# 'del_specs': bool, 'del_dist': bool, 'del_build': bool
# }
def create_executable_from_script(conf):
	print("\n ############### Conversion has Started ###############\n")
	script_folder = os.path.dirname(conf["script_path"])
	destination_folder = conf["new_path"] if conf["new_path"] != "" else script_folder
	file_extension = "exe" if platform.system() == "Windows" else "app"
	
	# 1st-> Making sure there is not an existing file in same folder where the .exe/.app will be created
	# delete_existing_executable(conf["file_name"], destination_folder, file_extension)
	
	# 2nd-> Converting the .py script into a .exe/.app file
	create_executable(conf, script_folder, destination_folder, file_extension)  # create the new version of the game
	
	# 3rd-> Deleting files created during the conversion process (only the ones chosen by the user)
	# manage_other_files(conf, script_folder, destination_folder)
	
	print("\n ########## Conversion Successfully Completed ##########\n")
