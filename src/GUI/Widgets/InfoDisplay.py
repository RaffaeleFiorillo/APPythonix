import tkinter as tk
import src.GUI.Widgets.Common as C


class InfoDisplay:
	def __init__(self, app, x, y):
		self.width, self.height = 200, 200
		
		self.canvas = tk.Canvas(background="black")
		self.canvas.place(x=x, y=y, width=580, height=360)
		
		# Create widgets to put inside the frame
		label_font = ("Arial", 20, "bold")
		label1 = tk.Label(app, text="Information & Tutorials", font=label_font, fg="black", bg="white")
		label1.place(x=x+120, y=y-20)
