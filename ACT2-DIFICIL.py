import math

x = 3
y = 4

r = math.hypot(x, y)
theta = math.atan2(y, x)

theta_grados = math.degrees(theta)

coordenadas_cartesianas = (x, y)

coordenadas_polares = (r, theta)

print("Coordenadas cartesianas:", coordenadas_cartesianas)
print("Coordenadas polares (r, θ en radianes):", coordenadas_polares)
print("Ángulo θ en grados:", theta_grados)
