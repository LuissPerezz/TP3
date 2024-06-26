import math

def cartesian_a_polar(x, y):
    
    r = math.sqrt(x**2 + y**2)
    
    if x > 0:
        theta = math.atan(y / x)
    elif x < 0 and y >= 0:
        theta = math.atan(y / x) + math.pi
    elif x < 0 and y < 0:
        theta = math.atan(y / x) - math.pi
    elif x == 0 and y > 0:
        theta = math.pi / 2
    elif x == 0 and y < 0:
        theta = -math.pi / 2
    else:
        theta = 0
    
    theta_grados = math.degrees(theta)
    
    return r, theta_grados

# Ejemplo de uso
x = 3
y = 4
r, theta = cartesian_a_polar(x, y)

print(f"Coordenadas cartesianas ({x}, {y}) convertidas a polares:")
print(f"Distancia (r): {r}")
print(f"Ángulo (θ) en grados: {theta}")
