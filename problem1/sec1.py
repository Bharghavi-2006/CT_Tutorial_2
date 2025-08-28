import numpy as np
import pandas as pd
from function import f, f_d

columns = ['x1','x2', 'f(xl)', 'f(xr)', 'xi+1', 'f(xi+1)', 'error']
db = pd.DataFrame(columns=columns)

x1=0
x2=1

errors=[]

for i in range(13):
    xn = x2 - f(x2)*(x2 - x1)/(f(x2)-f(x1)+0.000001)
    if abs(x2-x1) == np.float64(0.0):
        break
    db.loc[i] = [x1,x2,f(x1),f(x2),xn,f(xn),abs(-0.888889-xn)]
    errors.append(abs(-0.888889-xn))
    x1 = x2
    x2 = xn


print(db)
#lets find the rate of convergence
p=0
for j in range(len(errors)):
    if(j+1 < len(errors)):
        if errors[j+1] == np.float64(0.0):
            break
        if j-1 > -1: 
            p = np.log10(errors[j+1]/errors[j])/np.log10(errors[j]/errors[j-1])
            # print(p)
print('rate of convergence')
for i in range(-3,0):
    p= p + errors[i]/3
p = round(p, 3)
print(p)
    