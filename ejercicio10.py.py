"""
p10
Determina cuánto se debe pagar por equis cantidad de lápices considerando que si son 1000 o más el costo es de $0.85; de lo contrario, el precio es de $0.90
"""
# esto calcula cuanto se paga por los lapices, c es la cantidad de lapices
def l(c):
    # si son 1000 o mas cuestan .85 cada uno
    if c>=1000:
        return c*0.85
    # si son menos de 1000 cuestan .9 cada uno
    else:
        return c*0.9
# 2 ejemplos
print(l(1000))
print(l(500))
