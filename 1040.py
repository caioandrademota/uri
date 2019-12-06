def exame(media):
    print("Media: %.1f" % media)
    print("Aluno em exame.")
    exame = float(input())
    print("Nota do exame: ", exame)
    mf = (media + exame)/2
    if mf >= 5.0:
        print("Aluno aprovado.")
        print("Media final: %.1f" % mf)
    else:
        print("Aluno reprovado.")


n1, n2, n3, n4 = map(float, input().split(' '))

n1 = 2 * n1
n2 = 3 * n2
n3 = 4 * n3
n4 = n4

media = (n1 + n2 + n3 + n4)/10

if media >= 7.0:
    print("Media: %.1f" % media)
    print("Aluno aprovado.")
elif media >= 5.0 and media <= 6.9:
    exame(media)
else:
    print("Media: %.1f" % media)
    print("Aluno reprovado.")
