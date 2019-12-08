A, B, C = map(float, input().split(' '))
if abs(B - C) < A < (B + C) and (A - C) < B < (A + C)and (A - B) < C < (A + B):
    per = A + B + C
    print("Perimetro = %.1f" % per)
else:
    area = ((A + B) / 2) * C
    print("Area = %.1f" % area)
