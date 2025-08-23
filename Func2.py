import numpy as np

def fun2(x): 
    return np.cos(x)*np.cosh(x)
def fun2_d(x):
    return (np.cos(x)*np.sinh(x) - np.sin(x)*np.cosh(x))