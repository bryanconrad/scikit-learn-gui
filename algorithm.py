from tkinter import *
from tkinter import ttk

class Algorithm:
	def clear_frame(self, frame): #Removes all widgets in the AlgorithmFrame without deleting them.
		for widget in frame.winfo_children(): 
			widget.grid_remove()
			
class LabeledCheckbutton(Frame):
    def __init__(self, root):
        Frame.__init__(self, root, padding=(3,3,12,12))
        self.checkbutton = Checkbutton(self)
        self.label = Label(self)
        self.label.grid(row=0, column=0)
        self.checkbutton.grid(row=0, column=1)