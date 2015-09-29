from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from algorithm import *
from decision_tree_classifier import *
from gradient_boosting_classifier import *
from logistic_regression import *
import os



def save():
    filename = filedialog.asksaveasfilename()

def openFile():
    filename = filedialog.askopenfilename()
def loadTrainingData():
    trainingFileName = filedialog.askopenfilename()
    TrainingDataPrompt.config(text=os.path.basename(trainingFileName))

def loadTrainingLabels():
    trainingFileName = filedialog.askopenfilename()
    TrainingLabelPrompt.config(text=os.path.basename(trainingFileName))

def loadTestData():
    testFileName = filedialog.askopenfilename()
    TestDataPrompt.config(text=os.path.basename(testFileName))

def loadTestLabels():
    testFileName = filedialog.askopenfilename()
    TestLabelPrompt.config(text=os.path.basename(testFileName))

def displayMethodOptions(args):
    Alg = AlgList[AlgorithmMenu.curselection()[0]]
    Alg.Display_Options()
    
root = Tk()
root.geometry("900x700+50+50") 
content = ttk.Frame(root, padding=(3,3,12,12))

menubar = Menu(content)

AlgorithmFrame = ttk.Frame(content, padding=(3,3,12,12))
AlgorithmFrame['relief'] = 'sunken'


AlgList = {0: Decision_Tree_Classifier(AlgorithmFrame), 1: Gradient_Boosting_Classifier(AlgorithmFrame), 2: Logistic_Regression(AlgorithmFrame)}

# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=save)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# create more pulldown menus
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About")
menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu
root.config(menu=menubar)
content.grid(column=0, row=0, sticky=(N, S, E, W))

files = ttk.Frame(content, padding=(3,3,12,12))

TrainingDataText = ttk.Label(files, text='Training Data File: ')
TrainingDataText.grid(column=0, columnspan=2, row=0)

TrainingDataPrompt = ttk.Button(files, text="Click Here To Select", command=loadTrainingData)
TrainingDataPrompt.grid(column=2, columnspan=4, row=0)

TrainingLabelText = ttk.Label(files, text='Training Label File: ')
TrainingLabelText.grid(column=0, columnspan=2, row=1)

TrainingLabelPrompt = ttk.Button(files, text="Click Here To Select", command=loadTrainingLabels)
TrainingLabelPrompt.grid(column=2, columnspan=4, row=1)

TestDataText = ttk.Label(files, text='Test Data File: ')
TestDataText.grid(column=7, columnspan=2, row=0)

TestDataPrompt = ttk.Button(files, text="Click Here To Select", command=loadTestData)
TestDataPrompt.grid(column=9, columnspan=4, row=0)

TestLabelText = ttk.Label(files, text='Test Label File: ')
TestLabelText.grid(column=7, columnspan=2, row=1)

TestLabelPrompt = ttk.Button(files, text="Click Here To Select", command=loadTestLabels)
TestLabelPrompt.grid(column=9, columnspan=4, row=1)

files.grid(column=0, columnspan=8, row=0)

AlgNames = []
for value in AlgList.values():
    AlgNames.append(value.name)
AlgNames = tuple(AlgNames)
algorithms = StringVar(value=AlgNames)


AlgorithmFrame.grid(column=4, columnspan=4, row=1, sticky=(N,W,E,S))
AlgorithmMenu = Listbox(content, listvariable=algorithms, height=10, width=30)
AlgorithmMenu.grid(column=0, columnspan=4, row=1, sticky=(N,W,E,S))
AlgorithmMenu.bind('<<ListboxSelect>>', displayMethodOptions)
AlgList[0].Display_Options()
Run = ttk.Button(content, text='Run')
Run.grid(column=0, row=2, sticky=(W))


#Algorithm Options- Layout and Default Options



root.mainloop()
