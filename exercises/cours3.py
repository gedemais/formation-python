#1
def table(base, debut, fin, inc):
    x = debut
    y = fin
    while x < fin:
        print(x,y)
        x = x + inc
table (1,3,7,9)
#2
from math import pow
from math import pi
def cube(x):
    return pow(x,3)
def volumeSphere(r):
    return 4 * pi * ((pow(r,3)) / 3)

