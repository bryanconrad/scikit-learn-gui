def save():
    filename = filedialog.asksaveasfilename()

def openFile():
    filename = filedialog.askopenfilename()

def displayMethodOptions(args):
    global Alg
    Alg = AlgList[AlgorithmMenu.curselection()[0]]
    Alg.Display_Options()

def RunCurrentAlgorithm():
    global Alg
    Alg.Run(Training_Features_Filename.get(), Training_Labels_Filename.get(), Dev_Features_Filename.get(), Dev_Labels_Filename.get(), Predictions_Filename.get())
    
root = Tk()
root.geometry("900x700+50+50") 
content = ttk.Frame(root, padding=(3,3,12,12))

menubar = Menu(content)

AlgorithmFrame = ttk.Frame(content, padding=(3,3,12,12))
AlgorithmFrame['relief'] = 'sunken'

#To add a new algorithm to the list, add an instance of its class to the following dictionary:
AlgList = {0: Decision_Tree_Classifier(AlgorithmFrame), 1: Gradient_Boosting_Classifier(AlgorithmFrame), 2: Logistic_Regression(AlgorithmFrame)}

Alg = AlgList[0]
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
Training_Features_Filename = StringVar()
Training_Labels_Filename = StringVar()
Dev_Features_Filename = StringVar()
Dev_Labels_Filename = StringVar()
Predictions_Filename = StringVar()

TrainingDataText = ttk.Label(files, text='Training Data File: ')
TrainingDataText.grid(column=0, columnspan=2, row=0)

TrainingDataEntry = ttk.Entry(files, textvariable=Training_Features_Filename)
TrainingDataEntry.grid(column=2, columnspan=4, row=0)

TrainingDataPrompt = ttk.Button(files, text="Browse", command=lambda: Training_Features_Filename.set(filedialog.askopenfilename()))
TrainingDataPrompt.grid(column=6, columnspan=2, row=0)

TrainingLabelText = ttk.Label(files, text='Training Label File: ')
TrainingLabelText.grid(column=0, columnspan=2, row=1)

TrainingLabelEntry = ttk.Entry(files, textvariable=Training_Labels_Filename)
TrainingLabelEntry.grid(column=2, columnspan=4, row=1)

TrainingLabelPrompt = ttk.Button(files, text="Browse", command=lambda: Training_Labels_Filename.set(filedialog.askopenfilename()))
TrainingLabelPrompt.grid(column=6, columnspan=2, row=1)

TestDataText = ttk.Label(files, text='Test Data File: ')
TestDataText.grid(column=8, columnspan=2, row=0)

TestDataEntry = ttk.Entry(files, textvariable=Dev_Features_Filename)
TestDataEntry.grid(column=10, columnspan=4, row=0)

TestDataPrompt = ttk.Button(files, text="Browse", command=lambda: Dev_Features_Filename.set(filedialog.askopenfilename()))
TestDataPrompt.grid(column=14, columnspan=2, row=0)

TestLabelText = ttk.Label(files, text='Test Label File: ')
TestLabelText.grid(column=8, columnspan=2, row=1)

TestLabelEntry = ttk.Entry(files, textvariable=Dev_Labels_Filename)
TestLabelEntry.grid(column=10, columnspan=4, row=1)

TestLabelPrompt = ttk.Button(files, text="Browse", command=lambda: Dev_Labels_Filename.set(filedialog.askopenfilename()))
TestLabelPrompt.grid(column=14, columnspan=4, row=1)

PredictionsText = ttk.Label(files, text='Predictions File: ')
PredictionsText.grid(column=0, columnspan=2, row=2)

PredictionsEntry = ttk.Entry(files, textvariable=Predictions_Filename)
PredictionsEntry.grid(column=2, columnspan=4, row=2)

PredictionsPrompt = ttk.Button(files, text="Browse", command=lambda: Predictions_Filename.set(filedialog.askopenfilename()))
PredictionsPrompt.grid(column=6, columnspan=2, row=2)

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
Run = ttk.Button(content, text='Run', command=RunCurrentAlgorithm)
Run.grid(column=0, row=2, sticky=(W))