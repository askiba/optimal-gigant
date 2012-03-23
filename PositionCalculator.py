#coding=utf8
'''
Created on 23-03-2012

@author: Anka
'''
from scipy.integrate import odeint
import numpy as np
import pylab as p
from math import cos,sin,pi

g = 9.80665
 
def prawa_strona_rownania(w, t, params):
    '''
        Arguments:
            w: state vector(x,v)
            t: time
            params: parameters vector (alfa,mi,k) (k with mass "inside")
        In vector f we get the values
    '''
    x, v = w
    alfa, mi,k  = params
    
    f = [v,                                     # dx/dt
         g*sin(alfa)-mi*g*cos(alfa)- k *v*v]    # dv/dt
    return f

def calculate(alfa, mi,k):
    t = np.linspace(0, 5, 21)
    params = [alfa,mi,k]
    w = [0, 0]                    # initial condition (t=0) for x and v
     
    result = odeint(prawa_strona_rownania, w, t, args=(params,) ) 
     
    x = result[:, 0]
    v = result[:, 1]
    
    p.plot(t,x, t,v)
    p.legend(('x', 'v'))
    p.grid(True)
    p.show()    

if __name__ == '__main__':
    mi = 0.2
    alfa = pi/3.0
    k=0.1
    calculate(alfa,mi,k)
