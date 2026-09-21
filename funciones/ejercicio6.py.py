"""
f6
Crea una función llamada mayor_de_dos(a, b) que devuelva el
número más grande sin usar la función integrada max(). Si son
iguales, retorna cualquiera de los dos.
"""
# esto da el mayor de dos numeros, a y b son numeros
def md2(a, b):
    if a > b:
        return a
    elif(b > a):
        return b
    else:
        return a
# 3 ejemplos
print(md2(15, 27))
print(md2(40, -10))
print(md2(8, 8))
