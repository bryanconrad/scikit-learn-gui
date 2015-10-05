from algorithm import Algorithm
from tkinter import *
from tkinter import ttk
import cerberus
from sklearn.tree import DecisionTreeClassifier

class Decision_Tree_Classifier(Algorithm):
	
	def __init__(self, frame): #Display options for the Decision Tree Classifier.
		self.frame = frame
		
		self.name  = "Decision Tree Classifier"
		#Options for the quality criteria.
		self.Criterion_Label = ttk.Label(frame, text="Criterion:")
		self.Criterion = StringVar()
		self.Criterion.set('gini')
		self.Criterion_Gini = ttk.Radiobutton(frame, text='Gini', variable=self.Criterion, value='gini')
		self.Criterion_Entropy = ttk.Radiobutton(frame, text='Entropy', variable=self.Criterion, value='entropy')
		
		#Options for the splitting strategy.
		self.Splitter_Label = ttk.Label(frame, text="Splitter:")
		self.Splitter = StringVar()
		self.Splitter.set('best')
		self.Splitter_Best = ttk.Radiobutton(frame, text='Best', variable=self.Splitter, value='best')
		self.Splitter_Random = ttk.Radiobutton(frame, text='Random', variable=self.Splitter, value='random')
		
		#Options for the maximum number of features.
		self.MaxFeatures_Label = ttk.Label(frame, text='Max Features:')
		self.MaxFeatures = StringVar()
		self.MaxFeatures.set('none')
		self.MaxFeatures_Integer = StringVar()
		self.MaxFeatures_None = ttk.Radiobutton(frame, text='None', variable=self.MaxFeatures, value='none')
		self.MaxFeatures_Integer_Button = ttk.Radiobutton(frame, text='Number:', variable=self.MaxFeatures, value='integer')
		self.MaxFeatures_Integer_Box = ttk.Entry(frame, textvariable=self.MaxFeatures_Integer, width=7)
		self.MaxFeatures_Float_Button = ttk.Radiobutton(frame, text='Percentage:', variable=self.MaxFeatures, value='float')
		self.MaxFeatures_Float_Box = Spinbox(frame, from_=0.0, to=1.0, width=5, increment=0.01)
		self.MaxFeatures_Auto = ttk.Radiobutton(frame, text='Auto', variable=self.MaxFeatures, value='auto')
		self.MaxFeatures_Log2 = ttk.Radiobutton(frame, text='Log2', variable=self.MaxFeatures, value='log2')
		
		#Options for the max depth
		self.MaxDepth_Label = ttk.Label(frame, text='Max Depth:')
		self.MaxDepth = StringVar()
		self.MaxDepth.set('none')
		self.MaxDepth_None = ttk.Radiobutton(frame, text='None', variable=self.MaxDepth, value='none')
		self.MaxDepth_Integer = StringVar()
		self.MaxDepth_Integer.set('0')
		self.MaxDepth_Integer_Button = ttk.Radiobutton(frame, text='Number:', variable=self.MaxDepth, value='integer')
		self.MaxDepth_Integer_Box = ttk.Entry(frame, textvariable=self.MaxDepth_Integer, width=7)
		
		#Options for the minimum number of samples before an internal node is split.
		self.MinSamplesSplit_Label = ttk.Label(frame, text='Min Samples to Split:')
		self.MinSamplesSplit = StringVar()
		self.MinSamplesSplit.set('2')
		self.MinSamplesSplit_Integer_Box = ttk.Entry(frame, textvariable=self.MinSamplesSplit, width=7)
		
		#Options for the minimum number of leaf nodes
		self.MinSamplesLeaf_Label = ttk.Label(frame, text='Min # of Leaf Nodes:')
		self.MinSamplesLeaf = StringVar()
		self.MinSamplesLeaf.set('1')
		self.MinSamplesLeaf_Integer_Box = ttk.Entry(frame, textvariable=self.MinSamplesLeaf, width=7)
		
		#Options for the minimum fraction of leaf nodes
		self.MinFractionLeaf_Label = ttk.Label(frame, text='Min % of Leaf Nodes:')
		self.MinFractionLeaf = StringVar()
		self.MinFractionLeaf.set('0.0')
		self.MinFractionLeaf_Float_Box = ttk.Entry(frame, textvariable=self.MinFractionLeaf, width=7)
		
		#Options for the max # of leaf nodes
		self.MaxLeafNodes_Label = ttk.Label(frame, text='Max Leaf Nodes:')
		self.MaxLeafNodes = StringVar()
		self.MaxLeafNodes.set('none')
		self.MaxLeafNodes_None = ttk.Radiobutton(frame, text='None', variable=self.MaxLeafNodes, value='none')
		self.MaxLeafNodes_Integer = StringVar()
		self.MaxLeafNodes_Integer.set('0')
		self.MaxLeafNodes_Integer_Button = ttk.Radiobutton(frame, text='Number:', variable=self.MaxLeafNodes, value='integer')
		self.MaxLeafNodes_Integer_Box = ttk.Entry(frame, textvariable=self.MaxLeafNodes_Integer, width=7)
		
		#Options for the class weights
		self.ClassWeight_Label = ttk.Label(frame, text='Class Weights:')
		self.ClassWeight = StringVar()
		self.ClassWeight.set('none')
		self.ClassWeight_None = ttk.Radiobutton(frame, text='None', variable=self.ClassWeight, value='none')
		self.ClassWeight_Auto = ttk.Radiobutton(frame, text='Auto', variable=self.ClassWeight, value='auto')
		self.ClassWeight_Dictionary = ttk.Radiobutton(frame, text='Dictionary: Work in Progress', variable=self.ClassWeight, value='dictionary')
		
		#Options for the random state
		self.RandomState_Label = ttk.Label(frame, text='Random State:')
		self.RandomState = StringVar()
		self.RandomState.set('none')
		self.RandomState_Integer = StringVar()
		self.RandomState_Integer.set('0')
		self.RandomState_None = ttk.Radiobutton(frame, text='None', variable=self.RandomState, value='none')
		self.RandomState_Integer_Button = ttk.Radiobutton(frame, text='Seed:', variable=self.RandomState, value='integer')
		self.RandomState_Integer_Box = ttk.Entry(frame, textvariable=self.RandomState_Integer, width=7)
	
	def Validate(self):
		Fields = {}
		Features = {}
		if self.MaxFeatures.get() == 'integer':
			try:
				Features['MaxFeatures'] = int(self.MaxFeatures_Integer.get())
				MaxFeatures_Integer_Pattern = {'MaxFeatures':{'type':['integer'], 'min': 0}}
				v = cerberus.Validator(MaxFeatures_Integer_Pattern)
				if not v.validate(Features):
					print("MaxFeatures failed verification.")
					return False
				self.MaxFeatures_Final = int(self.MaxFeatures_Integer.get())
			except ValueError:
				print("Invalid value for Max Features: Not an integer.")
				return False
		elif self.MaxFeatures.get() == 'float':
			try:
				Features['MaxFeatures'] = float(self.MaxFeatures_Float_Box.get())
				MaxFeatures_Float_Pattern = {'MaxFeatures':{'type':['float'], 'min': 0.0, 'max':1.0}}
				v = cerberus.Validator(MaxFeatures_Float_Pattern)
				if not v.validate(Features):
					print("MaxFeatures failed verification.")
					return False
				self.MaxFeatures_Final = float(self.MaxFeatures_Float_Box.get())
			except ValueError:
				print("Invalid value for Max Features: Not a float")
				return False
		elif self.MaxFeatures.get() == 'none':
			self.MaxFeatures_Final = None
		else:
			self.MaxFeatures_Final = self.MaxFeatures.get()
		if self.MaxDepth.get() == 'integer':
			try:
				Fields['MaxDepth'] = int(self.MaxDepth_Integer.get())
			except ValueError:
				print("Invalid value for Max Depth: Not an integer")
				return False
			self.MaxDepth_Final = int(self.MaxDepth_Integer.get())
		else:
			self.MaxDepth_Final = None
		try:
			Fields['MinSamplesSplit'] = int(self.MinSamplesSplit.get())
		except ValueError:
			print("Invalid value for Min Samples to Split: Not an integer.")
			return False
		self.MinSamplesSplit_Final = int(self.MinSamplesSplit.get())
		try:
			Fields['MinSamplesLeaf'] = int(self.MinSamplesLeaf.get())
		except ValueError:
			print("Invalid value for Minimum Leaf Samples: Not an integer.")
			return False
		self.MinSamplesLeaf_Final = int(self.MinSamplesLeaf.get())
		try:
			Fields['MinFractionLeaf'] = float(self.MinFractionLeaf.get())
		except ValueError:
			print("Invalid value for Min Fraction: Not a float.")
			return False
		self.MinFractionLeaf_Final = float(self.MinFractionLeaf.get())
		if self.MaxLeafNodes.get() == 'integer':
			try:
				Fields['MaxLeafNodes'] = int(self.MaxLeafNodes_Integer.get())
			except ValueError:
				print("Invalid value for Max Leaf Nodes: Not an integer.")
				return False
			self.MaxLeafNodes_Final = int(self.MaxLeafNodes_Integer.get())
		else:
			self.MaxLeafNodes_Final = None
		if self.ClassWeight.get() == 'dictionary': #Dictionary option is not yet implemented
			print("Dictionary option is not yet implemented")
			return False
		if self.RandomState.get() == 'integer':
			try:
				Fields['RandomState'] = int(self.RandomState_Integer.get())
			except ValueError:
				print("Invalid value for Random State: Not an integer.")
				return False
			self.RandomState_Final = int(self.RandomState_Integer.get())
		else:
			self.RandomState_Final = None
		Main_Pattern = {'MaxDepth':{'required':False, 'type':['integer'], 'min':2}, 'MinSamplesSplit':{'required': True, 'type': ['integer'], 'min': 2}, 'MinSamplesLeaf':{'required': True, 'type': ['integer'], 'min': 1}, 'MinFractionLeaf':{'required': True, 'type': ['float'], 'min': 0.0, 'max':1.0}, 'MaxLeafNodes':{'required': False, 'type': ['integer'], 'min': 1}, 'RandomState':{'required': False, 'type': ['integer'], 'min': 0}}
		v = cerberus.Validator(Main_Pattern)
		if not v.validate(Fields):
			print("Failed main tests.")
			return False
		return True
		
	def import_data(self):
		x = 1
	
	def Run(self):
		if not self.Validate():
			print("Validation failed.")
			return False
		else:
			print("Validation Passed!")
			
		Classifier = DecisionTreeClassifier(criterion=self.Criterion.get(), splitter=self.Splitter.get(), max_features=self.MaxFeatures_Final, max_depth=self.MaxDepth_Final, min_samples_split=self.MinSamplesSplit_Final, min_samples_leaf=self.MinSamplesLeaf_Final, min_weight_fraction_leaf=self.MinFractionLeaf_Final, max_leaf_nodes=self.MaxLeafNodes_Final, class_weight=self.ClassWeight.get(), random_state=self.RandomState_Final)
		print("Classifier constructed")
		self.import_data()
		#Classifier.fit(self.Training_Data, self.Training_Labels)
		#self.
		
	def Display_Options(self):
		self.clear_frame(self.frame)

		#Insert the options into the frame.
		self.Criterion_Label.grid(column=0,row=0, sticky=(W))
		self.Criterion_Gini.grid(column=1, row=0, sticky=(W))
		self.Criterion_Entropy.grid(column=2, row=0, sticky=(W))
		self.Splitter_Label.grid(column=0, row=1, sticky=(W))
		self.Splitter_Best.grid(column=1, row=1, sticky=(W))
		self.Splitter_Random.grid(column=2, row=1, sticky=(W))
		self.MaxFeatures_Label.grid(column=0, row=2, sticky=(W))
		self.MaxFeatures_None.grid(column=0, row=3, sticky=(W))
		self.MaxFeatures_Integer_Button.grid(column=0, row=4, sticky=(W))
		self.MaxFeatures_Integer_Box.grid(column=1, row=4, sticky=(W))
		self.MaxFeatures_Float_Button.grid(column=0, row=5, sticky=(W))
		self.MaxFeatures_Float_Box.grid(column=1, row=5, sticky=(W))
		self.MaxFeatures_Auto.grid(column=0, row=6, sticky=(W))
		self.MaxFeatures_Log2.grid(column=0, row=7, sticky=(W))
		self.MaxDepth_Label.grid(column=0, row=8, sticky=(W))
		self.MaxDepth_None.grid(column=0, row=9, sticky=(W))
		self.MaxDepth_Integer_Button.grid(column=0, row=10, sticky=(W))
		self.MaxDepth_Integer_Box.grid(column=1, row=10, sticky=(W))
		self.MinSamplesSplit_Label.grid(column=0, columnspan=2, row=11, sticky=(W))
		self.MinSamplesSplit_Integer_Box.grid(column=2, row=11, sticky=(W))
		self.MinSamplesLeaf_Label.grid(column=0, columnspan=2, row=12, sticky=(W))
		self.MinSamplesLeaf_Integer_Box.grid(column=2, row=12, sticky=(W))
		self.MinFractionLeaf_Label.grid(column=0, columnspan=2, row=13, sticky=(W))
		self.MinFractionLeaf_Float_Box.grid(column=2, row=13, sticky=(W))
		self.MaxLeafNodes_Label.grid(column=0, row=14, sticky=(W))
		self.MaxLeafNodes_None.grid(column=0, row=15, sticky=(W))
		self.MaxLeafNodes_Integer_Button.grid(column=0, row=16, sticky=(W))
		self.MaxLeafNodes_Integer_Box.grid(column=1, row=16, sticky=(W))
		self.ClassWeight_Label.grid(column=0, row=17, sticky=(W))
		self.ClassWeight_None.grid(column=0, row=18, sticky=(W))
		self.ClassWeight_Auto.grid(column=0, row=19, sticky=(W))
		self.ClassWeight_Dictionary.grid(column=0, columnspan=4, row=20, sticky=(W))
		self.RandomState_Label.grid(column=0, row=21, sticky=(W))
		self.RandomState_None.grid(column=0, row=22, sticky=(W))
		self.RandomState_Integer_Button.grid(column=0, row=23, sticky=(W))
		self.RandomState_Integer_Box.grid(column=1, row=23, sticky=(W))