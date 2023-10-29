seconds = 1042
display_minutes = 1042 // 60 # '//' division redondea '/' division normal
display_seconds = 1042 % 60 # '%' saca el resto.

print(f"Tiempo: {display_minutes}m{display_seconds}s")


# libreria math
from math import ceil, floor
round_up = ceil(12.5) # ceil() redondea hacia arriba
print(round_up)

round_down = floor(12.5) # floor() redondea hacia abajo
print(round_down)