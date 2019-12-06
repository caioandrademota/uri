def exame(media):
    print("Aluno em exame.")
    exame = float(input("Nota do exame: "))
    mf = (media + exame)/2
    if mf >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")


n1, n2, n3, n4 = map(float, input().split(' '))

n1 = 2 * n1
n2 = 3 * n2
n3 = 4 * n3
n4 = n4

media = (n1 + n2 + n3 + n4)/10

if media >= 7.0:
    print("Media:", media)
    print("Aluno aprovado.")
elif media >= 5.0 and media < 7.0:
    exame(media)
else:
    print("Aluno reprovado.")
