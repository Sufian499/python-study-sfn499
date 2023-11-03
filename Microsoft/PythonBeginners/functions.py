#  *args y **kwargs son parámetros especiales que se utilizan en las funciones para permitir un número variable de argumentos.
# *args se utiliza para pasar un número variable de argumentos posicionales a una función.
# Los argumentos se tratan como una tupla dentro de la función
def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"
print(sequence_time(4, 14, 18))
# **kwargs se utiliza para pasar un número variable de argumentos con nombre a una función.
# Los argumentos se tratan como un diccionario dentro de la función.
def variable_length(**kwargs):
    print(kwargs)
variable_length(tanks=1, day="Wednesday", pilots=3)
print()
def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")
crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins")
