import pandas as pd
from function import f
import numpy as np

def regula_falsi(xl, xu):
    
    records = []
    errors = []
    prev_xr = xl

    for i in range(11):
        xr = xu - (f(xu)*(xl - xu))/(f(xl) - f(xu))
        
        error = abs((xr - prev_xr)/prev_xr) 
        errors.append(error)

        prev_xr = xr

        records.append({
            "Iteration": i,
            "xl": xl,
            "xu": xu,
            "xr": xr,
            "f(xr)": f(xr),
            "f(xu)": f(xu),
            "Error": error
        })

        if f(xr)*f(xu) < 0:
            xl = xr

        if f(xl)*f(xr) < 0:
            xu = xr

    p=0
    for j in range(len(errors)): 
        if(j+1 < len(errors)):
            if errors[j+1] == np.float64(0.0):
                break
            if j-1 > -1: 
                p = np.log10(errors[j+1]/errors[j])/np.log10(errors[j]/errors[j-1])
            p = round(p, 3)

    df = pd.DataFrame(records)
    print('rate of convergence =',p)
    return df

    
print(regula_falsi(-1, 1))


    



