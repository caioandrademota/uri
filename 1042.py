a = [0, 0, 0]

a[0], a[1], a[2] = map(int, input().split(' '))

cresc = sorted(a)
for i in range(0, 3):
    print(cresc[i])
print()
for i in range(0, 3):
    print(a[i])
