"""
p1
Una empresa importadora desea determinar cuántos
dólares puede adquirir con equis cantidad de dinero
mexicano.
"""
mxn=int(input("pesos mexicanos: "))
# esto calcula cuantos dolares se pueden comprar con pesos mexicanos, mxn es dinero en pesos
def c(mxn):
    # calculamos los dolares dividiendo los pesos entre el tipo de cambio fijo (20)
    dolares=mxn/20
    # regresa en dolares
    return dolares
print(c(mxn))
