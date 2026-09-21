"""
f12
Problema: Crea una función llamada calificar(nota) que reciba un
número decimal o entero que represente una calificación de 0 a
100. Utilizando una cadena de condiciones if / elif / else:
• Si la nota es mayor o igual a 90, retorna "A".
• Si está entre 80 y 89 inclusive, retorna "B".
• Si está entre 70 y 79 inclusive, retorna "C".
• Si es menor estrictamente a 70, retorna "F".
"""
# esto pone la calificacion en letra segun el numero, cal es la calificacion
def calif(cal):
    if cal >= 90:
        return "A"
    elif cal < 70:
        return "F"
    elif 80 <= cal <= 89:
        return "B"
    elif 70 <= cal <= 79:
        return "C"
# 4 ejemplos
print(calif(100))
print(calif(89))
print(calif(79))
print(calif(50))
