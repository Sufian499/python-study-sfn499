# Proyecto FreeCodeCamp Python
# Madlib
from time import sleep
import sys
def madlib_funct():
    criatura = input("Criatura/Ser: ")
    adj1 = input("Adjetivo: ")
    adj2 = input("Adjetivo: ")
    adj3 = input("Adjetivo: ")
    sustantivo1 = input("Sustantivo: ")
    comparativa = input("Comparación (como...): ")
    sustantivo2 = input("Sustantivo: ")
    sustantivo3 = input("Sustantivo: ")
    sustantivo4 = input("Sustantivo: ")
    verbo1 = input("Verbo: ")
    lugar1 = input("Lugar: ")
    lugar2 = input("Lugar: ")
    lugar3 = input("Lugar: ")
    sustantivo5 = input("Sustantivo:")
    madlib = f"En un agujero en el suelo, vivía un {criatura}. No un agujero {adj1}, {adj2}, {adj3}, \
con restos de gusanos y olor a fango, ni tampoco un agujero seco, desnudo y \
arenoso, sin nada en que sentarse o que comer: era un agujero-{criatura}, y eso \
significa comodidad.\
\nTenía una {sustantivo1} redonda, perfecta  {comparativa}, pintada de verde, con \
una manilla de bronce dorada y brillante, justo en el medio. La {sustantivo1} se abría a un \
{sustantivo2} cilíndrico, como un túnel: un túnel muy cómodo, sin humos, con paredes \
revestidas de {sustantivo3} y suelos enlosados y alfombrados, provistos de sillas barnizadas, y \
montones y montones de {sustantivo4}; el {criatura} era aficionado a \
las {verbo1}. El túnel se extendía serpeando, y penetraba bastante, pero no directamente, \
en la ladera de {lugar1} —{lugar1}, como la llamaba toda la gente de muchas millas \
alrededor—, y muchas puertecitas redondas se abrían en él, primero a un lado y luego al \
otro. Nada de subir escaleras para el {criatura}: dormitorios, cuartos de baño, bodegas, \
{lugar2} (muchas), {lugar3} (habitaciones enteras dedicadas a {sustantivo5}), cocinas, \
comedores, se encontraban en la misma planta, y en verdad en el mismo pasillo. Las \
mejores habitaciones estaban todas a la izquierda de la puerta principal, pues eran las \
únicas que tenían ventanas, ventanas redondas, profundamente excavadas, que miraban \
al jardín y los prados de más allá, camino del río."
    return madlib

def main():
    # Con este bucle muestro la variable que me devuelve la función madlib_funct, que es el madlib.
    for x in madlib_funct():
        # La idea es mostrarmelo como si alguien lo estubiera escribiendo, muestro el texto palabra por palabra sin saltos con end=''.
        print (x,end='')
        sys.stdout.flush() # Esta función de sys muestra por pantalla el output.
        sleep(0.05) # Esperamos x tiempo para que parezca que se este generando el texto.
    
if __name__ == "__main__":
    main()