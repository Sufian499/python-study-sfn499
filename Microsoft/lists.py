# Listinhas
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

planets[3] = "Red Planet" # seleccionamos un valor de la lista mediante indices [x] y podemos manipularlo

print("Mars is also known as", planets[3])
planets[3] = "Mars"
print(f"Hay {len(planets)} planetas en el sistema solar.")

planets.append('Pluto')
print(f"Ackshuali, there is {len(planets)} planets.")
planets.pop() # Elimina el último número de la lista.
print(f"No, there are definetely {len(planets)} planets in the solar systems.")
# Índices negativos, empiezan al final de la lista '-1' y van para atrás, '-2' penúltimo...
print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])
# Buscar valor
jupiter_index = planets.index('Jupiter')
print("Jupiter is the", jupiter_index + 1, "planet from the sun")

# numbers
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
bus_weight = 12650 # in Newtons, on Earth

print("On Earth, a double-decker bus weighs", bus_weight, "N")
# min() número más pequeño de la lista, max() número más gran.
print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "N")
print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "N")

# segmentación de listas. La segmentación crea una nueva lista no modifica la lista con la que se trabaja
planets_after_earh = planets[0:2] # [0,2) el último núm no lo incluye.
print(planets_after_earh)
planets_before_earth = planets[3:] # [3,inf] Todos los que van despues del 3.
print(planets_before_earth)

# Unificar listas
amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]
# Seleccionamos las 2 listas y las unimos con '+'
regular_satellite_moons = amalthea_group + galilean_moons
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

#.sort() ordena listas. Modifica el orden de la lista, oJITO.
regular_satellite_moons.sort() # Ordena la lista en orden alfabetico
print("The regular satellite moons of Jupiter are", regular_satellite_moons)
regular_satellite_moons.sort(reverse=True) # Al inverso
print("The regular satellite moons of Jupiter are", regular_satellite_moons)


