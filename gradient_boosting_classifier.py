from algorithm import Algorithm
from tkinter import *
from tkinter import ttk

class Gradient_Boosting_Classifier(Algorithm):

	def __init__(self, frame):
		self.frame = frame
		
		self.name = "Gradient Boosting Classifier"
		#Options for the loss criteria.
		self.Loss_Label = ttk.Label(frame, text="Loss Function:")
		self.Loss = StringVar()
		self.Loss.set('deviance')
		self.Loss_Deviance = ttk.Radiobutton(frame, text='Deviance', variable=self.Loss, value='deviance')
		self.Loss_Exponential = ttk.Radiobutton(frame, text='Exponential', variable=self.Loss, value='exponential')
		
		#Options for the learning rate.
		self.LearningRate_Label = ttk.Label(frame, text="Learning Rate:")
		self.LearningRate = StringVar()
		self.LearningRate.set('0.1')
		self.LearningRate_Box = Spinbox(frame, textvariable=self.LearningRate, from_=0.0, to=1.0, increment=0.01, width=5)
		
		#Options for the number of boosting stages.
		self.Estimators_Label = ttk.Label(frame, text='# of Stages:')
		self.Estimators = StringVar()
		self.Estimators.set('100')
		self.Estimators_Box = ttk.Entry(frame, textvariable=self.Estimators, width=7)
		
		#Options for the max depth
		self.MaxDepth_Label = ttk.Label(frame, text='Max Depth:')
		self.MaxDepth = StringVar()
		self.MaxDepth.set('0')
		self.MaxDepth_Box = ttk.Entry(frame, textvariable=self.MaxDepth, width=7)
		
		#Options for the minimum number of samples before an internal node is split.
		self.MinSamplesSplit_Label = ttk.Label(frame, text='Min Samples to Split:')
		self.MinSamplesSplit = StringVar()
		self.MinSamplesSplit.set('2')
		self.MinSamplesSplit_Box = ttk.Entry(frame, textvariable=self.MinSamplesSplit, width=7)
		
		#Options for the minimum number of leaf nodes
		self.MinSamplesLeaf_Label = ttk.Label(frame, text='Min # of Leaf Nodes:')
		self.MinSamplesLeaf = StringVar()
		self.MinSamplesLeaf.set('1')
		self.MinSamplesLeaf_Box = ttk.Entry(frame, textvariable=self.MinSamplesLeaf, width=7)
		
		#Options for the minimum fraction of leaf nodes
		self.MinFractionLeaf_Label = ttk.Label(frame, text='Min % of Leaf Nodes:')
		self.MinFractionLeaf = StringVar()
		self.MinFractionLeaf.set('0.0')
		self.MinFractionLeaf_Box = ttk.Entry(frame, textvariable=self.MinFractionLeaf, width=7)
		
		#Options for batch size
		self.Subsample_Label = ttk.Label(frame, text='Batch Size:')
		self.Subsample = StringVar()
		self.Subsample.set('1.0')
		self.Subsample_Box = Spinbox(frame, from_=0.0, to=1.0, increment=0.01, textvariable=self.Subsample, width=5)
		
		#Options for max features.
		self.MaxFeatures_Label = ttk.Label(frame, text='Max Features:')
		self.MaxFeatures = StringVar()
		self.MaxFeatures.set('none')
		self.MaxFeatures_Integer = StringVar()
		self.MaxFeatures_Float = StringVar()
		self.MaxFeatures_Float.set('0.1')
		self.MaxFeatures_None = ttk.Radiobutton(frame, text='None', variable=self.MaxFeatures, value='none')
		self.MaxFeatures_Integer_Button = ttk.Radiobutton(frame, text='Number:', variable=self.MaxFeatures, value='integer')
		self.MaxFeatures_Integer_Box = ttk.Entry(frame, textvariable=self.MaxFeatures_Integer, width=7)
		self.MaxFeatures_Float_Button = ttk.Radiobutton(frame, text='Percentage:', variable=self.MaxFeatures, value='float')
		self.MaxFeatures_Float_Box = Spinbox(frame, from_=0.0, to=1.0, textvariable=self.MaxFeatures_Float, width=5, increment=0.01)
		self.MaxFeatures_Auto = ttk.Radiobutton(frame, text='Auto', variable=self.MaxFeatures, value='auto')
		self.MaxFeatures_Log2 = ttk.Radiobutton(frame, text='Log2', variable=self.MaxFeatures, value='log2')
		
		#Options for the max # of leaf nodes
		self.MaxLeafNodes_Label = ttk.Label(frame, text='Max Leaf Nodes:')
		self.MaxLeafNodes = StringVar()
		self.MaxLeafNodes.set('none')
		self.MaxLeafNodes_None = ttk.Radiobutton(frame, text='None', variable=self.MaxLeafNodes, value='none')
		self.MaxLeafNodes_Integer = StringVar()
		self.MaxLeafNodes_Integer.set('0')
		self.MaxLeafNodes_Integer_Button = ttk.Radiobutton(frame, text='Number:', variable=self.MaxLeafNodes, value='integer')
		self.MaxLeafNodes_Integer_Box = ttk.Entry(frame, textvariable=self.MaxLeafNodes_Integer, width=7)
		
		#Options for verbosity
		self.Verbose_Label = ttk.Label(frame, text='Verbose Level:')
		self.Verbose = StringVar()
		self.Verbose.set('0')
		self.Verbose_Box = ttk.Entry(frame, textvariable=self.Verbose, width=7)

	def Display_Options(self): #Display options for the Decision Tree Classifier.
		self.clear_frame(self.frame)
		
		#Insert the options into the frame.
		self.Loss_Label.grid(column=0,row=0, sticky=(W))
		self.Loss_Deviance.grid(column=1, row=0, sticky=(W))
		self.Loss_Exponential.grid(column=2, row=0, sticky=(W))
		self.LearningRate_Label.grid(column=0, row=1, sticky=(W))
		self.LearningRate_Box.grid(column=1, row=1, sticky=(W))
		self.Estimators_Label.grid(column=0, row=2, sticky=(W))
		self.Estimators_Box.grid(column=1, row=2, sticky=(W))
		self.MaxDepth_Label.grid(column=0, row=3, sticky=(W))
		self.MaxDepth_Box.grid(column=1, row=3, sticky=(W))
		self.MinSamplesSplit_Label.grid(column=0, columnspan=2, row=4, sticky=(W))
		self.MinSamplesSplit_Box.grid(column=2, row=4, sticky=(W))
		self.MinSamplesLeaf_Label.grid(column=0, columnspan=2, row=5, sticky=(W))
		self.MinSamplesLeaf_Box.grid(column=2, row=5, sticky=(W))
		self.MinFractionLeaf_Label.grid(column=0, columnspan=2, row=6, sticky=(W))
		self.MinFractionLeaf_Box.grid(column=2, row=6, sticky=(W))
		self.Subsample_Label.grid(column=0, row=7, sticky=(W))
		self.Subsample_Box.grid(column=1, row=7, sticky=(W))
		self.MaxFeatures_Label.grid(column=0, row=8, sticky=(W))
		self.MaxFeatures_None.grid(column=0, row=9, sticky=(W))
		self.MaxFeatures_Integer_Button.grid(column=0, row=10, sticky=(W))
		self.MaxFeatures_Integer_Box.grid(column=1, row=10, sticky=(W))
		self.MaxFeatures_Float_Button.grid(column=0, row=11, sticky=(W))
		self.MaxFeatures_Float_Box.grid(column=1, row=11, sticky=(W))
		self.MaxFeatures_Auto.grid(column=0, row=12, sticky=(W))
		self.MaxFeatures_Log2.grid(column=0, row=12, sticky=(W))
		self.MaxLeafNodes_Label.grid(column=0, row=13, sticky=(W))
		self.MaxLeafNodes_None.grid(column=0, row=14, sticky=(W))
		self.MaxLeafNodes_Integer_Button.grid(column=0, row=15, sticky=(W))
		self.MaxLeafNodes_Integer_Box.grid(column=1, row=15, sticky=(W))
		self.Verbose_Label.grid(column=0, row=16, sticky=(W))
		self.Verbose_Box.grid(column=1, row=16, sticky=(W))