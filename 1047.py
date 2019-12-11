hi, mi, hf, mf = map(int, input().split(' '))

ht = hf - hi
mt = mf - mi
if ht < 0:
    ht += 24
if mt < 0:
    mt += 60
    ht -= 1

if ht == 0 and mt == 0:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" % (ht, mt))
