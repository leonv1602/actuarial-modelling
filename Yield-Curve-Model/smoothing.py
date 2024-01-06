import numpy as np
import pandas as pd 

class smoothing:
    def __init__(self):
        self.data = None 
        self.smoothing = None
        self.smoothing_tech = None 
        self.smoothness = None 
        self.error = 0
    
    def linear_method(self):
        t = np.linspace(0,self.smoothness) 
        return 


    def error(self, error_type):
        if error_type == 'mean-squared-error':
            return np.mean((self.data - self.smoothing)**2)
        if error_type == 'absolute-error':
            return np.mean(np.abs(self.data - self.smoothing))