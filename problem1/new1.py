# def f(x):
#     return 729*x**3 - 432*x + 128
# def f_d(x):
#     return 2187*x**2 - 432

import pandas as pd
import numpy as np
from function import f, f_d, f_dd

columns = ['xi' , 'f(xi)', 'f_d(x)', 'xi+1', 'err']
db = pd.DataFrame(columns=columns, dtype=float)

p = np.pi

x = -0.5

errors = []
#we have to use relative error to find rate of convergence

for i in range(11):
    xin = x - f(x)/f_d(x) #did newton raphson in this step
    db.loc[i] = [x, f(x), f(x), xin, (abs(xin - x))]
    if (abs(xin - x)/abs(xin)) == np.float64(0.0):
        break
    errors.append((abs(xin - x)))
    x = xin

print(db)

#lets find the rate of convergence
p=0
for j in range(len(errors)):
    if(j+1 < len(errors)):
        if errors[j+1] == np.float64(0.0):
            break
        if j-1 > -1: 
            p = np.log10(errors[j+1]/errors[j])/np.log10(errors[j]/errors[j-1])
            p = round(p, 3)
            print(p)

# print('rate of convergence is ', p)
    




    