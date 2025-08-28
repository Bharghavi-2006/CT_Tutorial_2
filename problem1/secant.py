import numpy as np
import pandas as pd
from function import f

errors = []
records = []

def secant(xl, xu):
    
    ans = -0.8888889

    for i in range(11):
        xr = xu - ((f(xu)*(xl - xu))/(f(xl) - f(xu) + 0.000000001))

        error = abs((xr-ans)/xr)
        errors.append(error)

        records.append({
            "Iteration": i,
            "xl": xl,
            "xu": xu,
            "xr": xr,
            "f(xr)": f(xr),
            "f(xu)": f(xu),
            "Error": error
        })

        xl = xu
        xu = xr


    p=0
    for j in range(len(errors)): 
        if(j+1 < len(errors)):
            if errors[j+1] == np.float64(0.0):
                break
            if j-1 > -1: 
                p = np.log10(errors[j+1]/errors[j])/np.log10(errors[j]/errors[j-1])
            print(p)

    df = pd.DataFrame(records)
    return df

print(secant(-1, 1))







