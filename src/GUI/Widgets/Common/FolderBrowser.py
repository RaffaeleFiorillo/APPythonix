import tkinter as tk


class FolderBrowser:
	def __init__(self, container, x, y, browsing_function):
		# Load the image (replace 'your_image_path.png' with your actual image path)
		image = tk.PhotoImage(file="assets/folder icon.png")
		image = image.subsample(2, 2)  # Adjust subsample factor as needed
		self.button = tk.Button(container, image=image, command=browsing_function, text="", width=0, height=0, bg="black")
		self.button.image = image  # Retain reference to the image
		self.button.place(x=x, y=y)
		
	def disable(self):
		self.button.config(state="disabled")
	
	def enable(self):
		self.button.config(state="normal")
