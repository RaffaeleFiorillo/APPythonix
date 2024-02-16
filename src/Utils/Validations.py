import os
import re


def is_valid_python_script_path(path) -> bool:
	return os.path.exists(path) and os.path.isfile(path) and path.endswith('.py')


def is_valid_file_name(file_name) -> bool:
	if file_name == "":  # default case
		return True
	return bool(re.match(r'^[A-Za-z0-9_\- ()]+$', file_name))


def is_valid_icon_image_path(path) -> bool:
	if path == "":  # default case
		return True
	return os.path.exists(path) and os.path.isfile(path) and path.endswith('.ico')


def is_valid_new_path(path) -> bool:
	if path == "":  # default case
		return True
	return os.path.exists(path) and os.path.isdir(path)
