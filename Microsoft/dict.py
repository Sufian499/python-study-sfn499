planet = {
    'name': 'Earth',
    'moons': 1
}

print(planet.get('name'))
# planet['name'] is identical to using planet.get('name')
print(planet['name'])

wibble = planet.get('wibble') # Returns None
# wibble = planet['wibble'] # Throws KeyError

# Cambiar valores de diccionario
#.update()
planet.update({
    'name': 'Jupiter',
    'moons': 79
}) 
# [] =
planet['name'] = 'Jupiter'
planet['moons'] = 79

# Crear nuevos valores en el diccionario
planet['orbital period'] = 4333

# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
#   orbital period: 4333
# }

# Eliminar valores
planet.pop('orbital period') # key

# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
# }

# Diccionario anidado
# Add address
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}

# planet dictionary now contains: {
#   name: 'Jupiter'
#   moons: 79
#   diameter (km): {
#      polar: 133709
#      equatorial: 142984
#   }
# }
# Printer datos de diccionario anidado
print(f'{planet["name"]}, polar diameter: {planet["diameter (km)"]["polar"]}')

#.keys(), te devuelve una lista con el nombre de las keys
rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}
for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')
    
if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1

# Because december exists, the value will be 3.1
#.values()
total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value

print(f'There was {total_rainfall}cm in the last quarter.')