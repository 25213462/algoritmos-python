"""
p6
Se requiere determinar el costo que tendrá realizar una llamada telefónica con base en el tiempo que dura la llamada y en el costo por minuto.
costo por minuto: $3.00 mxn
"""
# esto calcula el costo de la llamada, m es los minutos que duro
def c(m):
    # cada minuto cuesta 3 
    return m*3
# 2 ejemplos
print(c(5))
print(c(10))
