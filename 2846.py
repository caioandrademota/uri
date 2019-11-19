def fibonot(num):
    ant = 1
    suc = 2
    soma = 3
    while num > 0:
        ant = suc
        suc = soma
        soma = ant + suc
        num -= (soma - suc - 1)
    num += (soma - suc - 1)
    return suc + num

num = int(input())
print(fibonot(num))
