from math import pi, cos, sin, tan

x = float(input())
r = (x * pi) / 180

print(sin(r) + cos(r) + tan(r)**2)