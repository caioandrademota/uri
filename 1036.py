import math
a, b, c = input().split(' ')
a = float(a)
b = float(b)
c = float(c)
delta = b**2 - 4*a*c
if delta <= 0 or a == 0:
    print("Impossivel calcular")
else:
    root1 = (-b + math.sqrt(delta))/(2*a)
    root2 = (-b - math.sqrt(delta))/(2*a)
    print("R1 = %.5f" %root1)
    print("R2 = %.5f" %root2)
