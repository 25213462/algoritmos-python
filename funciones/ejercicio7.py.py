"""
f7
Escribe una función llamada es_mayor_de_edad(edad) que reciba
un entero y retorne "Mayor" si tiene 18 años o más, y "Menor" en
caso contrario.
"""
# esto va dar si una persona es mayor de edad, e es la edad
def mde(e):
    if e >= 18:
        return "mayor"
    else:
        return "menor"
# 3 ejemplos
print(mde(17))
print(mde(18))
print(mde(45))
