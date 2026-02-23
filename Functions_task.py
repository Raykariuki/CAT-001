import math

def area_of_circle(radius):
    if radius <= 0:
        return "Error: Radius must be a positive number."
    
    area = math.pi * (radius ** 2)
    
    return round(area, 2)

print(area_of_circle(5)) 