"""
p9
Determina el promedio que obtendrá un alumno considerando que realiza tres exámenes, de los cuales el primero y el segundo tienen una ponderación de 25%, mientras que el tercero de 50%
"""
e1=int(input("examen 1: "))
e2=int(input("examen 2: "))
e3=int(input("examen 3: "))
# esto calcula un promedio , e1 e2 y e3 son las calificaciones de los tres examenes
def p(e1,e2,e3):
    # el primero y segundo valen 25% cada uno y el tercero vale 50%
    return e1*0.25+e2*0.25+e3*0.5
print(p(e1,e2,e3))
