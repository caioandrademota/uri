a, b, c = map(float, input().split(' '))

tri = [a, b, c]
maior = max(tri)
cat1 = min(tri)
cat2 = sum(tri) - cat1 - maior

while True:
    if maior >= cat1 + cat2:
        print("NAO FORMA TRIANGULO")
        break

    if maior ** 2 == cat1 ** 2 + cat2 ** 2:
        print("TRIANGULO RETANGULO")
    elif maior ** 2 > cat1 ** 2 + cat2 ** 2:
        print("TRIANGULO OBTUSANGULO")
    elif maior ** 2 < cat1 ** 2 + cat2 ** 2:
        print("TRIANGULO ACUTANGULO")

    if maior == cat1 == cat2:
        print("TRIANGULO EQUILATERO")
    c1 = (maior == cat1 != cat2)
    c2 = (cat1 == cat2 != maior)
    c3 = (maior == cat2 != cat1)
    if c1 is True or c2 is True or c3 is True:
        print("TRIANGULO ISOSCELES")
    break
