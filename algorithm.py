from tkinter import *
from tkinter import ttk
import numpy as np

class Algorithm:
	def clear_frame(self, frame): #Removes all widgets in the AlgorithmFrame without deleting them.
		for widget in frame.winfo_children(): 
			widget.grid_remove()
	
	def import_data(self, Training_Features_Filename, Training_Labels_Filename, Dev_Features_Filename, Dev_Labels_Filename):
		self.Training_Data = np.loadtxt(Training_Features_Filename)
		self.Training_Labels = open(Training_Labels_Filename).read().splitlines()
		self.Dev_Data = np.loadtxt(Dev_Features_Filename)
		self.Dev_Labels = open(Dev_Labels_Filename).read().splitlines()
		
	def Create_Popup(self, msg):
		popup = Tk()
		popup.geometry("180x70+200+200")
		popup.wm_title("Results")
		label = ttk.Label(popup, text=msg)
		label.grid()
		destroy = ttk.Button(popup, text="Okay", command = popup.destroy)
		destroy.grid()
		popup.mainloop()
		
	def Run(self, Training_Features_Filename, Training_Labels_Filename, Dev_Features_Filename, Dev_Labels_Filename):
		if not self.Validate():
			print("Validation failed.")
			return False
		else:
			print("Validation Passed!")
		self.Create_Classifier()
		self.import_data(Training_Features_Filename, Training_Labels_Filename, Dev_Features_Filename, Dev_Labels_Filename)
		self.Classifier.fit(self.Training_Data, self.Training_Labels)
		score = self.Classifier.score(self.Dev_Data, self.Dev_Labels)
		self.Create_Popup("Score: " + str(score))
		
		
class LabeledCheckbutton(Frame):
    def __init__(self, root):
        Frame.__init__(self, root, padding=(3,3,12,12))
        self.checkbutton = Checkbutton(self)
        self.label = Label(self)
        self.label.grid(row=0, column=0)
        self.checkbutton.grid(row=0, column=1)
		
	