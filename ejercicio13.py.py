"""
p13
La política de la compañía telefónica “chimefón” es: “Chismea + x -”. 
Cuando se realiza una llamada, el cobro es por el tiempo que ésta dura, 
de tal forma que los primeros cinco minutos cuestan $1.00 peso c/u, 
los siguientes tres, 80¢ centavos de peso c/u, los siguientes dos minutos, 
70¢ centavos de peso c/u, y a partir del décimo minuto, 50¢ centavos de peso c/u.
Determinar cuánto debe pagar por cada concepto una persona que realiza una llamada en moneda nacional mexicana (MXN).
"""
# esto calcula el costo de una llamada, m es minutos de la llamada
def c(m):
    # calculamos el costo segun los minutos
    if m<=5:
        # si son 5 minutos o menos, cada minuto cuesta 1
        return m*1
    elif m<=8:
        # si son entre 6 y 8 minutos, primeros 5 cuestan 1 los demas cuestan 0.8
        return 5*1+(m-5)*0.8
    elif m<=10:
        # si son entre 9 y 10 minutos, 5 minutos a 1 + 3 minutos a 0.8 + los demas a 0.7
        return 5*1+3*0.8+(m-8)*0.7
    else:
        # si son mas de 10 minutos, 5 a 1 peso + 3 a 0.8 + 2 a 0.7 + lo demas a 0.5
        return 5*1+3*0.8+2*0.7+(m-10)*0.5
# 4 ejemplos
print(c(4))
print(c(7))
print(c(9))
print(c(15))
