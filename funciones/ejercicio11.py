"""
f11
Diseña una función llamada mayor_de_tres(a, b, c) que reciba
tres números y determine cuál es el mayor utilizando únicamente
operadores lógicos (and) y comparaciones (>=) sin emplear
max(). Por ejemplo: si a>=b y a>=c, el mayor es a. La función
debe devolver el número más grande encontrado.
"""
# esto haya el mayor de tres numeros, a b y c son los numeros
def mde3(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
# 3 ejemplos
print(mde3(5, 12, 9))
print(mde3(20, 3, 1))
print(mde3(4, 4, 4))
