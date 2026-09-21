"""
f10
Implementa una función llamada operacion_basica(a, b,
operacion) donde a y b son operandos numéricos y operacion es
una cadena. Usa ramas condicionales para comparar el texto: si
vale "suma", devuelve a+b; si vale "resta", devuelve a - b; si vale
"multiplica", devuelve a x b. Si el texto recibido no coincide con
ninguna de esas opciones, debe retornar "Operación no válida".
"""
# esto hace una operacion entre dos numeros, a y b son numeros, ope es el tipo de operacion
def oper(a, b, ope):
    if(ope == "suma"):
        return a + b
    elif(ope == "division"):
        return a / b
    elif(ope == "resta"):
        return a - b
    elif(ope == "multiplicacion"):
        return a * b
    else:
        return "error"
# 4 ejemplos
print(oper(9, 9, "suma"))
print(oper(9, 9, "resta"))
print(oper(9, 9, "multiplicacion"))
print(oper(9, 9, "dev"))
