import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
def fitfunc(m,mu,sigma,R,A,b1,b2):
    bexp = b1 * (m-105.5) + b2 * ( (m-105.5) **2 )
    b = A*np.exp(bexp)
    sexp = -( (m-mu) **2) / (2 * (sigma**2) )
    s = (R/(sigma * math.sqrt( 2 * math.pi ) ))*np.exp(sexp)
    return b+s

def fitter(xval, yval, initial):
    best, _ = curve_fit(fitfunc, xval, yval, p0=initial)
    return best

init = (125.8, 1.4, 470.0, 5000.0, -0.04, -1.5e-4)
xvalues = np.arange(start=105.5, stop=160.5, step=1)
data = np.array([4780, 4440, 4205, 4150, 3920, 3890, 3590, 3460, 3300, 3200, 3000, 
                 2950, 2830, 2700, 2620, 2610, 2510, 2280, 2330, 2345, 2300, 2190, 
                 2080, 1990, 1840, 1830, 1730, 1680, 1620, 1600, 1540, 1505, 1450, 
                 1410, 1380, 1380, 1250, 1230, 1220, 1110, 1110, 1080, 1055, 1050, 
                 940, 920, 950, 880, 870, 850, 800, 820, 810, 770, 760])
fit = fitter(xvalues,data,init)
lobf = fitfunc(xvalues,fit[0],fit[1],fit[2],fit[3],fit[4],fit[5])
plt.plot(xvalues,data,'r+')
plt.plot(xvalues,lobf,'r')
plt.show()

resratio = (lobf-data)/data
plt.plot(xvalues,resratio)
plt.plot()