"""
p14
la politica de la compania telefonica “chimefon” es: “chismea + x -”. 
cuando se realiza una llamada, el cobro es por el tiempo que esta dura, 
de tal forma que los primeros cinco minutos cuestan $1.00 peso c/u, 
los siguientes tres, 80 centavos de peso c/u, los siguientes dos minutos, 
70 centavos de peso c/u, y a partir del decimo minuto, 50 centavos de peso c/u.

ademas, se carga un impuesto de 3 % cuando es domingo, 
y si es dia habil, en turno matutino, 15 %, y en turno vespertino, 10 %. 
realice un algoritmo para determinar cuanto debe pagar por cada concepto 
una persona que realiza una llamada en moneda nacional mexicana (mxn).
"""
m = int(input("minutos: "))
d = input("dia: ")
t = input("turno (matutino/vespertino): ")
# m es minutos de la llamada, d es dia de la semana, t es turno (matutino/vespertino)
def c14(m, d, t):
    # calculamos el costo segun los minutos
    if m <= 5:
        costo = m * 1
    elif m <= 8:
        costo = 5 * 1 + (m - 5) * 0.8
    elif m <= 10:
        costo = 5 * 1 + 3 * 0.8 + (m - 8) * 0.7
    else:
        costo = 5 * 1 + 3 * 0.8 + 2 * 0.7 + (m - 10) * 0.5
    # porcentaje de impuesto
    if d == "domingo":
        imp = 0.03
    elif t == "matutino":
        imp = 0.15
    else:
        imp = 0.1
    return costo * (1 + imp)
print(c14(m, d, t))
