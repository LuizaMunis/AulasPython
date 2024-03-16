import math

a=1
b=-3
c=-54

delta= b**2-4*a*c
print(delta)

x1=(-b+ delta **(1/2))/(2*a)
x2=(-b- delta **(1/2))/(2*a)

raiz= math.sqrt(delta)

print(x1)
print(x2)
print(raiz)