lista = ['Dasher', 'Dancer', 'Prancer',
         'Vixen', 'Comet', 'Cupid',
         'Donner', 'Blitzen', 'Rudolph']

a, b, c, d, e, f, g, h, i = map(int, input().split())
renas = a + b + c + d + e + f + g + h + i

while renas > 9:
    renas -= 9

print(lista[renas-1])
