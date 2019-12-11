a, b, c = map(float, input().split(' '))

tri = [a, b, c]
maior = max(tri)
cat1 = min(tri)
cat2 = sum(tri) - (cat1 + maior)


if maior >= cat1 + cat2:
    print("NAO FORMA TRIANGULO")
else:
    if maior ** 2 == cat1 ** 2 + cat2 ** 2:
        print("TRIANGULO RETANGULO")
    if maior ** 2 > cat1 ** 2 + cat2 ** 2:
        print("TRIANGULO OBTUSANGULO")
    if maior ** 2 < cat1 ** 2 + cat2 ** 2:
        print("TRIANGULO ACUTANGULO")

    if a == b and a == c and b == c:
        print("TRIANGULO EQUILATERO")
    else:
        if a == b or a == c or b == c:
            print("TRIANGULO ISOSCELES")
