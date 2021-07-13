rangos = ["bebe", "niños", "adolecentes", "adulto joven", "adulto", "tercera edad"]
edad_usuario = int(input("Ingrese su edad en años: "))

def etapa_edad(edad: str, etapas: list) -> str:
    edad_estudiante= edad
    
    if edad_usuario >= 0 and edad_usuario <=3:
        etapas= etapas[0]
    elif edad_usuario > 3 and edad_usuario <= 12:
        etapas= etapas[1]
    elif edad_usuario > 12 and edad_usuario <= 17:
        etapas= etapas[2]   
    elif edad_usuario > 17 and edad_usuario <= 29:
        etapas= etapas[3]
    elif edad_usuario > 29 and edad_usuario <= 54:
        etapas= etapas[4]
    elif edad_usuario > 54:
        etapas= etapas[5]
    else:
        print("la edad ingresada no esta en el rango de etapas")
    return  edad_estudiante, etapas

edad_estudiante, etapa = etapa_edad(edad_usuario, rangos) 

print("El estudiante de {} años esta en la etapa de {}".format(edad_estudiante,etapa))
