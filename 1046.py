begin, end = map(int, input().split(' '))

if end > begin:
    final = end - begin
    print("O JOGO DUROU %i HORA(S)" % final)
else:
    if end == begin:
        print("O JOGO DUROU 24 HORA(S)")
    elif begin > end:
        final = abs(begin - 24) + end
        print("O JOGO DUROU %i HORA(S)" % final)
