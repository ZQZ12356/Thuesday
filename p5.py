# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 14:30:04 2019

@author: microsoft
"""
import numpy as np
x=np.linspace(0,10,100)
y=[i**2 for i in x]
from matplotlib.pyplot import *
plot(x,y,'-b')