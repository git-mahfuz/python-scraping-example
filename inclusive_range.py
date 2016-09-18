# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 17:26:49 2016

@author: Mahfuzul Alam
"""

class InclusiveRange:
    def __init__(self, *args):
        
        noOfArguments = len(args)        
        
        if noOfArguments < 1:
            raise ValueError("Range requires at least 1(one) parameter")
            
        elif noOfArguments == 1:
            self.start = 0
            self.stop = args[0]
            self.step = 1
            
        elif noOfArguments == 2:
            self.start = args[0]
            self.stop = args[1]
            self.step = 1
            
        elif noOfArguments ==  3:
            (self.start, self.stop, self.step) = args
            
        else:
            raise ValueError("Whoops! No of arguments can be at most 3")
            
            
    def __iter__(self):
        i = self.start
        while i <= self.stop:
            yield i
            i += self.step
        
        
try:
    inRange = InclusiveRange(0, 25, 5)
    
    for i in inRange:
        print(i)
    
except ValueError as e:
    print(e)
    
except Exception as e:
    print(e)
        
        


