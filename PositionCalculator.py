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
    ''' Argumenty:
         w: wektor stanu (u nas x, v)
         t: czas
         params: wektor parametr�w (u nas omega_kwadrat)
 
     W wektorze f funkcja zwraca
              obliczone dla danego wektora stanu
              warto�ci prawej strony r�wnania
    '''
    x, v = w                  # dla czytelno�ci r�wnania wypakowuj� zmienne z wektora "w"
    alfa, mi,k  = params   # i podobnie z parametrami "params"
    # poni�ej do tablicy f w kolejnych wierszach wpisuj�
    # kolejne prawe strony r�wna� stanowi�cych uk�ad
    f = [v,                   # warto�� pochodnej dx/dt
         g*sin(alfa)-mi*g*cos(alfa)- k *v*v]  # warto�� pochodnej dv/dt
    return f

def calculate(alfa, mi,k):
    t = np.linspace(0, 5, 21)
    params = [alfa,mi,k]
    w = [0, 0]                    # warunek pocz�tkowy (t=0) dla x i v
    print "Wektor stanu w chwili pocz�tkowej: ",
    print prawa_strona_rownania(w, t[0], params)
     
    # argumentami odeint s�:
    # - nazwa funkcji,
    # - wektor stanu pocz�tkowego,
    # - wektor zawieraj�cy chwile czasu, dla kt�rych ma by� zwr�cony stan uk�adu
    # - krotka zawieraj�ca dodatkowe parametry, kt�re maj� by� przekazane do funkcji
    #           opisuj�cej prawe strony r�wna�
     
    wynik = odeint(prawa_strona_rownania, w, t, args=(params,) ) 
     
    x = wynik[:, 0]
    v = wynik[:, 1]
     
    p.plot(t,x, t,v)
    p.legend(('x', 'v'))
    p.grid(True)
    p.show()    

if __name__ == '__main__':
    mi = 0.2
    alfa = pi/3.0
    k=0.1
    calculate(alfa,mi,k)
