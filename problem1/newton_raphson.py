import pandas as pd
import numpy as np
from function import f, f_d

columns = ['xi' , 'f(xi)', "f'(xi)", 'xi+1', 'err']
db = pd.DataFrame(columns=columns, dtype=float)

p = np.pi

x = -0.5
final_ans = -0.8888889

errors = []
#we have to use relative error to find rate of convergence

for i in range(11):
    xin = x - (f(x)/f_d(x)) #did newton raphson in this step
    db.loc[i] = [x, f(x), f_d(x), xin, (abs(xin - final_ans)/abs(xin))]
    if (abs(xin - x)/abs(xin)) == np.float64(0.0):
        break
    errors.append((abs(xin - final_ans)/abs(xin)))
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
            print(p)

    




    