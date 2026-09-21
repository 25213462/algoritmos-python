"""
p14
La política de la compañía telefónica “chimefón” es: “Chismea + x -”. 
Cuando se realiza una llamada, el cobro es por el tiempo que ésta dura, 
de tal forma que los primeros cinco minutos cuestan $1.00 peso c/u, 
los siguientes tres, 80¢ centavos de peso c/u, los siguientes dos minutos, 
70¢ centavos de peso c/u, y a partir del décimo minuto, 50¢ centavos de peso c/u.

Además, se carga un impuesto de 3 % cuando es domingo, 
y si es día hábil, en turno matutino, 15 %, y en turno vespertino, 10 %. 
Realice un algoritmo para determinar cuánto debe pagar por cada concepto 
una persona que realiza una llamada en moneda nacional mexicana (MXN).
"""

# esto calcula el costo de una llamada, m es minutos de la llamada, d es dia de la semana, t es turno, matutino/vespertino
def c(m,d,t):
    # calculamos el costo segun los minutos
    if m<=5:
        # si son 5 minutos o menos, cada minuto cuesta 1
        costo=m*1
    elif m<=8:
        # si son entre 6 y 8 minutos, primeros 5 cuestan 1 los demas cuestan 0.8
        costo=5*1+(m-5)*0.8
    elif m<=10:
        # si son entre 9 y 10 minutos, 5 minutos a 1 + 3 minutos a 0.8 + los demas a 0.7
        costo=5*1+3*0.8+(m-8)*0.7
    else:
        # si son mas de 10 minutos, 5 a 1 peso + 3 a 0.8 + 2 a 0.7 + lo demas a 0.5
        costo=5*1+3*0.8+2*0.7+(m-10)*0.5
    # que impuesto se aplica, si domingo cobra 3%, otro dia y es matutino 15%, en vespertino 10%
    if d=="domingo":
        imp=0.03
    elif t=="matutino":
        imp=0.15
    else:
        imp=0.1
    # el costo mas el impuesto
    return costo*(1+imp)
# 3 ejemplos
print(c(4,"lunes","matutino"))
print(c(7,"domingo","vespertino"))
print(c(12,"martes","vespertino"))
