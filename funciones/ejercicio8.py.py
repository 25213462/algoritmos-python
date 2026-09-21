"""
f8
Diseña una función llamada area_triangulo (base, altura) que
calcule el área mediante la fórmula (base x altura) / 2 y valide que
ambos valores sean mayores a cero; si no lo son, debe retornar
0.
"""
# esto calcula el area de un triangulo, b es base y h es altura
def ati(b, h):
    if b and h <= 0:
        return cero
    else:
        return (b * h ) / 2
# ejemplo
print(ati(10, 10))
