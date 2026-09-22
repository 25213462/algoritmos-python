"""
p8
Almacenes “El harapiento distinguido” tiene una promoción: a todos los trajes que tienen un precio superior a $2500.00 se les aplicará un descuento de 15%, a todos los demás se les aplicará sólo 8%. Realice un algoritmo para determinar el precio final que debe pagar una persona por comprar un traje y de cuánto es el descuento que obtendrá.
"""
precio=float(input("precio: "))
# esto calcula el precio final y el descuento de un traje, precio es el precio original
def t(precio):
    # si el traje cuesta mas de 2500 se le descuenta 15%
    if precio>2500:
        desc=precio*0.15
    # si cuesta 2500 o menos se le descuenta 8%
    else:
        desc=precio*0.08
    # restamos el descuento al precio original
    final=precio-desc
    return final,desc
print(t(precio))
