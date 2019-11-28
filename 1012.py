a, b, c = input().split(' ')
a = float(a)
b = float(b)
c = float(c)

triangle = a * c/2
circle = 3.14159 * (c**2)
trapezium = (c * (a + b))/2
square = b**2
rectangle = a * b

print("TRIANGULO: %.3f" % triangle)
print("CIRCULO: %.3f" % circle)
print("TRAPEZIO: %.3f" % trapezium)
print("QUADRADO: %.3f" % square)
print("RETANGULO: %.3f" % rectangle)
