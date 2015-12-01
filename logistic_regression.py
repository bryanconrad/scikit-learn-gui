from algorithm import Algorithm
from algorithm import LabeledCheckbutton
from tkinter import *
from tkinter import ttk

class Logistic_Regression(Algorithm):
	
	def __init__(self, frame): #Create a Logistic Regression object.
		self.frame = frame
		
		self.name = "Logistic Regression"
		#Options for the normalization.
		self.Penalty_Label = ttk.Label(frame, text="Regularization:")
		self.Penalty = StringVar()
		self.Penalty.set('l1')
		self.Penalty_L1 = ttk.Radiobutton(frame, variable=self.Penalty, text='l1', value='l1')
		self.Penalty_L2 = ttk.Radiobutton(frame, variable=self.Penalty, text='l2', value='l2')
		
		#Dual or Primal formulation
		self.Dual_Label = ttk.Label(frame, text='Formulation:')
		self.Dual = StringVar()
		self.Dual.set('dual')
		self.Dual_Dual = ttk.Radiobutton(frame, text='Dual', variable=self.Dual, value='dual')
		self.Dual_Primordial = ttk.Radiobutton(frame, text='Primordial', variable=self.Dual, value='primordial')
		
		#Options for C, the inverse regularization strength.
		self.C_Label = ttk.Label(frame, text='C:')
		self.C = StringVar()
		self.C.set('1.0')
		self.C_Box = ttk.Entry(frame, textvariable=self.C, width=7)
		
		self.FitIntercept_Label = ttk.Label(frame, text='Fit Intercept:')
		self.FitIntercept = StringVar()
		self.FitIntercept_Button = ttk.Checkbutton(frame, variable=self.FitIntercept, onvalue='true', offvalue='false', text=' ')
		
		self.InterceptScaling_Label = ttk.Label(frame, text='Intercept Scaling:')
		self.InterceptScaling = StringVar()
		self.InterceptScaling_Box = ttk.Entry(frame, textvariable=self.InterceptScaling, width=7)
		
		self.ClassWeights_Label = ttk.Label(frame, text='Class Weights:')
		self.ClassWeights = StringVar()
		self.ClassWeights.set('none')
		self.ClassWeights_None = ttk.Radiobutton(frame, text='None', variable=self.ClassWeights, value='none')
		self.ClassWeights_Auto = ttk.Radiobutton(frame, text='Auto', variable=self.ClassWeights, value='auto')
		
		self.MaxIter_Label = ttk.Label(frame, text='Maximum Iterations:')
		self.MaxIter = StringVar()
		self.MaxIter_Box = ttk.Entry(frame, textvariable=self.MaxIter, width=7)
		
		self.RandomState_Label = ttk.Label(frame, text='Random State:')
		self.RandomState = StringVar()
		self.RandomState.set('none')
		self.RandomState_Integer = StringVar()
		self.RandomState_Integer.set('0')
		self.RandomState_None = ttk.Radiobutton(frame, text='None', variable=self.RandomState, value='none')
		self.RandomState_Integer_Button = ttk.Radiobutton(frame, text='Seed:', variable=self.RandomState, value='integer')
		self.RandomState_Integer_Box = ttk.Entry(frame, textvariable=self.RandomState_Integer, width=7)
		
		self.Solver_Label = ttk.Label(frame, text='Solver:')
		self.Solver = StringVar()
		self.Solver.set('none')
		self.Solver_Newton = ttk.Radiobutton(frame, text='Newton-cg', variable=self.Solver, value='newton-cg')
		self.Solver_LBFGS = ttk.Radiobutton(frame, text='LBFGS', variable=self.Solver, value='lbfgs')
		self.Solver_Liblinear = ttk.Radiobutton(frame, text='Liblinear', variable=self.Solver, value='liblinear')
	def Display_Options(self):
		self.clear_frame(self.frame)
		
		#Display LR options.
		self.Penalty_Label.grid(column=0, row=0, sticky=(W))
		self.Penalty_L1.grid(column=1, row=0, sticky=(W))
		self.Penalty_L2.grid(column=2, row=0, sticky=(W))
		self.Dual_Label.grid(column=0, row=1, sticky=(W))
		self.Dual_Dual.grid(column=1, row=1, sticky=(W))
		self.Dual_Primordial.grid(column=2, row=1, sticky=(W))
		self.C_Label.grid(column=0, row=2, sticky=(W))
		self.C_Box.grid(column=1, row=2, sticky=(W))
		self.FitIntercept_Label.grid(column=0, row=3, sticky=(W))
		self.FitIntercept_Button.grid(column=1, row=3, sticky=(W))
		self.InterceptScaling_Label.grid(column=0, row=4, sticky=(W))
		self.InterceptScaling_Box.grid(column=1, row=4, sticky=(W))
		self.ClassWeights_Label.grid(column=0, row=5, sticky=(W))
		self.ClassWeights_None.grid(column=1, row=5, sticky=(W))
		self.ClassWeights_Auto.grid(column=2, row=5, sticky=(W))
		self.MaxIter_Label.grid(column=0, row=6, sticky=(W))
		self.MaxIter_Box.grid(column=1, row=6, sticky=(W))
		self.RandomState_Label.grid(column=0, row=7, sticky=(W))
		self.RandomState_None.grid(column=0, row=8, sticky=(W))
		self.RandomState_Integer_Button.grid(column=0, row=9, sticky=(W))
		self.RandomState_Integer_Box.grid(column=1, row=9, sticky=(W))
		self.Solver_Label.grid(column=0, row=10, sticky=(W))
		self.Solver_Newton.grid(column=0, row=11, sticky=(W))
		self.Solver_LBFGS.grid(column=0, row=12, sticky=(W))
		self.Solver_Liblinear.grid(column=0, row=13, sticky=(W))