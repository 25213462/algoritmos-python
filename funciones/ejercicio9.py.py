"""
f9
Crea una función llamada obtener_signo(numero) que reciba un
número real o entero. Mediante las ramas if, elif y else, clasifica
el valor: retorna "Positivo" si es mayor que cero, "Negativo" si es
menor que cero, o "Cero" si es exactamente igual a cero.
"""
# esto da el signo de un numero, numero es el valor
def signo(numero):
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "cero"
# 3 ejemplos
print(signo(1))
print(signo(-1))
print(signo(0))
