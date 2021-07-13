rangos = ["bebe", "niños", "adolescentes", "adulto joven", "adulto", "tercera edad","difunto"]
#edad_usuario = int(input("Ingrese su edad: "))


    
def etapa_edad(edad: str, etapas: list,) -> str:
    #
    #
    return

while True:
    try: 
        edad_usuario = int(input("\nIngrese su edad: "))
        break
    except ValueError:
        print("\ndigita un número no letras por favor")


while edad_usuario < 0:
    print("\ndigita un número entero positivo por favor")    
    edad_usuario = int(input("\nIngrese su edad: "))



if edad_usuario <5:
    x=0

elif edad_usuario >4 and edad_usuario <14:
    x=1

elif edad_usuario >13 and edad_usuario <18:
    x=2

elif edad_usuario >17 and edad_usuario <36:
     x=3

elif edad_usuario >35 and edad_usuario <65:
    x=4

elif edad_usuario >64 and edad_usuario <115:
    x=5
else:
    x=6

edad=edad_usuario
etapas=rangos[x] 

print(f"\nTienes :",edad," años y perteneces al rago de :",etapas)    
