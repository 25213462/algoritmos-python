"""
p7
Determina cuánto pagará finalmente una persona por un artículo equis, considerando que tiene un descuento de 20%, y debe pagar 15% de IVA (debe mostrar el precio con descuento y el precio final).

Crea un menú para que el usuario elija entre 2 productos y el que elija, despliega el nombre de producto, precio, precio con descuento y precio final.
"""
print("1. camisa - 500")
print("2. pantalon - 800")
op=int(input("elige (1 o 2): "))
# segun opcion se guarda el nombre y el precio
if op==1:
    nombre="camisa"
    precio=500
else:
    nombre="pantalon"
    precio=800
# calculamos el 20% de descuento
desc=precio*0.2
# precio despues del descuento
con_desc=precio-desc
# le sumamos el 15% de iva
iva=con_desc*0.15
final=con_desc+iva
# mostramos todo
print(nombre)
print("precio:",precio)
print("con descuento:",con_desc)
print("precio final:",final)
