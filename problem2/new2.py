import pandas as pd
import numpy as np
from Func2 import fun2, fun2_d

columns = ['xi' , 'f(xi)', 'xi+1', 'err']
db = pd.DataFrame(columns=columns, dtype=float)

p = np.pi

x = 4.5

errors = []
#we have to use relative error to find rate of convergence

for i in range(11):
    xin = x - fun2(x)/fun2_d(x) #did newton raphson in this step
    db.loc[i] = [x, fun2(x), xin, (abs(xin - x)/abs(xin))]
    if (abs(xin - x)/abs(xin)) == np.float64(0.0):
        break
    errors.append((abs(xin - x)/abs(xin)))
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

print('rate of convergence is ', p)
    




    