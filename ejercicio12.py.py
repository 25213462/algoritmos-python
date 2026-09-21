"""
p12
“La langosta ahumada” es una empresa dedicada a ofrecer banquetes; sus tarifas son las siguientes: el costo de platillo por persona es de $95.00, pero si el número de personas es mayor a 200 pero menor o igual a 300, el costo es de $85.00. Para más de 300 personas el costo por platillo es de $75.00. Se requiere un algoritmo que ayude a determinar el presupuesto que se debe presentar a los clientes que deseen realizar un evento.
"""
# esto calcula el presupuesto del plato, n es el numero de personas
def b(n):
    # cuantas personas son para saber el precio por persona
    if n>300:
        # mas de 300 personas cuestan 75 cada una
        p=75
    elif n>200:
        # entre 201 y 300 personas cuestan 85 cada una
        p=85
    else:
        # 200 o menos cuestan 95 cada una
        p=95
    # multiplicamos personas por el precio
    return n*p
# 3 ejemplos
print(b(150))
print(b(250))
print(b(350))

