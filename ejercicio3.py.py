"""
p3
Un estacionamiento requiere determinar el cobro que debe aplicar a las personas que lo utilizan. Considere que el cobro es con base en las horas que lo disponen y que las fracciones de hora se toman como completas
"""
import math
# esto calcula el cobro del estacionamiento, horas es el tiempo ahi
def c(horas):
    # redondeamos para arriba las fracciones de hora y se multiplica por 10, es el precio porhora
    return math.ceil(horas)*10
# 3 ejemplos
print(c(2.3))
print(c(1.1))
print(c(4))
