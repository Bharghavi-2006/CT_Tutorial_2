import numpy as np
import pandas as pd
from Func2 import fun2, fun2_d

columns = ['x1','x2', 'f(xl)', 'f(xr)', 'xi+1', 'f(xi+1)', 'error']
db = pd.DataFrame(columns=columns)

x1=4.1
x2=4.9

errors=[]

for i in range(11):
    xn = x2 - fun2(x2)*(x2 - x1)/(fun2(x2)-fun2(x1))
    if abs(x2-x1) == np.float64(0.0):
        break
    db.loc[i] = [x1,x2,fun2(x1),fun2(x2),xn,fun2(xn),abs(x2-x1)]
    errors.append(abs(x2-x1))
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
            p = round(p, 3)
print(p)
    