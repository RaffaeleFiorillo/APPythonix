import tkinter as tk
from idlelib.tooltip import Hovertip


class InfoHoover:
	def __init__(self, container, x: int, y: int, info: str):
		# Load the image (replace 'your_image_path.png' with your actual image path)
		image = tk.PhotoImage(file="assets/info icon.png")
		image = image.subsample(2, 2)  # Adjust subsample factor as needed
		self.button = tk.Button(container, image=image, text="", width=0, height=0, bg="black")
		self.button.image = image  # Retain reference to the image
		self.button.place(x=x, y=y)
		
		self.info = info
		self.tooltip = Hovertip(self.button, self.info, hover_delay=0)
		
