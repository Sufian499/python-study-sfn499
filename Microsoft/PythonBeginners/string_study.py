# `.title()` Convierte en titulo la string (añade mayusculas)
print("temperatures and facts about nature".title())
# `.split()` Separar una string y lo convierte en una lista. De normal separa por espacios, esto lo puedes configurar dentro de los parentesis.
temperatures = "Daylight: 260 F\n Nighttime: -280 F"
temperatures_list = temperatures.split()
print(temperatures_list)

# `in` Confirmar si hay una palabra en una string.
print("Moon" in "This text will describe facts and challenges with space travel")
print("Moon" in "This text will describe facts about the Moon")

# `.find()` Buscar una palabra y su posicion.
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Mars"))
# Output: 64 la posición de Mars, si no encuentra nada devuelve -1

# Count. Cuenta cuantas veces sale una palabra en la string.
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.count("Mars")) # output: 1
print(temperatures.count("Moon")) # output: 0

# En el siguiente ejemplo, sepearamos por los 2 puntas la siguiente string dejandonos un valor con el enunciado
# y otro valor con la temperatura
temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':')
print(parts)
# El -1 nos da el último valor de la lista.
print(parts[-1])

#.isnumeric() Aqui separamos la siguiente string y en un bucle buscamos si el item es un int
mars_temperature = "The highest temperature on Mars is about 30 C" # los numeros negativos no funcionan
for item in mars_temperature.split():
    if item.isnumeric(): #.isdecimal() para floats
        print(item)
        
#.startswith() y .endswith()
mars_temperature = "The highest temperature on Mars is about -40 C"
for item in mars_temperature.split():
    if item.startswith('-'): # Si la string empieza por x valor.
        print(item)
        
if "30 C".endswith("C"): # Si la string termina por X
    print("This temperature is in Celsius")

#.replace(string, cambio) reemplaza una string por otra 
print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C"))
#.lower() Usos de .lower()
text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text)
text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text.lower())
#.join() unimos los elementos de una lista en una string
moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
print(' '.join(moon_facts))