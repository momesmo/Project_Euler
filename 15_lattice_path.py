from math import factorial, fabs

def lattice_paths(r, c):
    return (factorial(r + c) / (factorial(r) * factorial(c)))

print(lattice_paths(20, 20))