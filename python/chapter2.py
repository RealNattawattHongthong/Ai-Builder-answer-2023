import math

def calccylindersurfacearea(radius, height):
    if radius <= 0 or height <= 0:
        return -1

    base_area = math.pi * (radius ** 2)
    lateral_area = 2 * math.pi * radius * height
    surface_area = 2 * base_area + lateral_area

    return math.ceil(surface_area)
print(calccylindersurfacearea(2, -5))

