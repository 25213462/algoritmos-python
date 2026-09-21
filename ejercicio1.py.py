"""
p1
Una empresa importadora desea determinar cuántos
dólares puede adquirir con equis cantidad de dinero
mexicano.
"""
# esto calcula cuantos dolares se pueden comprar con pesos mexicanos, mxn es dinero en pesos, tc es tipo de cambio
def c(mxn,tc):
    # calculamos los dolares dividiendo los pesos entre el valor
    dolares=mxn/tc
    # regresa en dolares
    return dolares
# 3 ejemplos
print(c(1000,20))
print(c(500,18.5))
print(c(2500,19.8))
