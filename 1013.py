a, b, c = input().split(' ')
a = int(a)
b = int(b)
c = int(c)


maior1 = (a + b + abs(a - b))/2
maior2 = (b + c + abs(b - c))/2
maior = (maior1 + maior2 + abs(maior1 - maior2))/2
print("%i eh o maior" % maior)
