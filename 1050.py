ddd = {'61': 'Brasilia', '71': 'Salvador', '11': 'Sao Paulo',
        '21': 'Rio de Janeiro', '32': 'Juiz de Fora', '19': 'Campinas',
        '27': 'Vitoria', '31': 'Belo Horizonte'}

num = input()
if num not in ddd.keys():
    print("DDD nao cadastrado")
else:
    for k in ddd.keys():
        if num == k:
            print(ddd.get(k))
