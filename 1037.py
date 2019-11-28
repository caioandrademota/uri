def verify(value):
    if value < 0 or value > 100:
        print("Fora de intervalo")
    else:
        intervalos = [[0, 25], [25.00001, 50], [50.00001, 75], [75.00001, 100]]
        for i in intervalos:
            if i[0] <= value <= i[-1]:
                if i == [0, 25]:
                    print("Intervalo [%d,%d]" % (i[0], i[-1]))
                else:
                    print("Intervalo (%d,%d]" % (i[0], i[-1]))


value = float(input())
verify(value)
