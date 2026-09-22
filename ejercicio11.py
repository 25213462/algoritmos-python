"""
p11
Se requiere determinar cuál de tres cantidades proporcionadas es la mayor.
"""
a=int(input("cantidad 1: "))
b=int(input("cantidad 2: "))
c=int(input("cantidad 3: "))
# esto determina el mayor de tres numeros
def m(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
print(m(a,b,c))

