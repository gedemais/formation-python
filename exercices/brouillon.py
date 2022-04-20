from math import pi
def cube(x) :
    return x**3

def volumeSphere(r) :
    return 4* pi * cube(r) / 3
rayon = float(input("rayon : "))
print(volumeSphere)


