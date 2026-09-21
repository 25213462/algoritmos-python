"""
p2
Una empresa que contrata personal requiere determinar la
edad de las personas que solicitan trabajo, pero cuando
se les realiza la entrevista sólo se les pregunta el año en
que nacieron.
"""
# esto calcula la edad de una persona, anio_nac es el anio de nacimiento, anio_act es el anio actual
def c(anio_nac,anio_act):
    # calculamos la edad restando el anio de nacimiento al anio actual
    edad=anio_act-anio_nac
    # resultado de la edad en anios
    return edad
# 3 ejemplos
print(c(2000,2026))
print(c(1995,2026))
print(c(1988,2026))
