try:
    open("mars.jpg")
except FileNotFoundError as err: # err es el mensaje de error stdout
     print("Got a problem trying to read the file:", err)
     
loaded_config = """# Rocket Ship Configuration File!
fuel_tanks=4
oxygen_tanks=3
initial_propulsion_level=84
$ End of file"""

parsed_config = {}
for line in loaded_config.split("\n"): # Recorre cada linea de loaded_config separado con \n
    try: # Try
        key, value = line.split("=") # Separamos la linea cuando haya un =.
        # Le damos los valores a key y value
        parsed_config[key]=value # Lo pasamos al diccionario
    except ValueError: # Si no encuentra ningun '=' dará el error ValueError. 
            print(f"Unable to parse: {line}")  # Para que no cierre el programa que haga esto
print(parsed_config)

def water_left(astronauts, water_left, days_left):
    # Condición para que salga un mensaje de error si el user inserta datos que no sean enteros.
    for argument in [astronauts,water_left,days_left]:
        try:
            argument / 10
        except TypeError:
            raise TypeError(f"Los argumentos deben de ser de tipo 'int'. {argument}")
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"
try:
    water_left(5,"100",2)
except RuntimeError:
    print()