"""
p4
La compañía de autobuses “La curva loca” requiere determinar el costo que tendrá el boleto de un viaje sencillo, esto basado en los kilómetros por recorrer y en el costo por kilómetro.
Costo por km: $80.00 mxn
"""
# esto calcula el costo de boleto, km es la cantidad de kilometros
def b(km):
    # cada kilometro cuesta 80
    return km*80
# 2 ejemplos
print(b(10))
print(b(25))
