cash, coins = input().split('.')
cash = int(cash)
coins = int(coins)
notas_100 = int(cash/100)
cash = cash - (notas_100*100)
notas_50 = int(cash/50)
cash = cash - (notas_50*50)
notas_20 = int(cash/20)
cash = cash - (notas_20*20)
notas_10 = int(cash/10)
cash = cash - (notas_10*10)
notas_5 = int(cash/5)
cash = cash - (notas_5*5)
notas_2 = int(cash/2)
cash = cash - (notas_2*2)
notas_1 = int(cash/1)
cash = cash - (notas_1*1)

moedas_50 = int(coins/50)
coins = coins - (moedas_50*50)
moedas_25 = int(coins/25)
coins = coins - (moedas_25*25)
moedas_10 = int(coins/10)
coins = coins - (moedas_10*10)
moedas_5 = int(coins/5)
coins = coins - (moedas_5*5)
moedas_1 = int(coins/1)
coins = coins - (moedas_1*1)

print("NOTAS:")
print(notas_100, "nota(s) de R$ 100.00")
print(notas_50, "nota(s) de R$ 50.00")
print(notas_20, "nota(s) de R$ 20.00")
print(notas_10, "nota(s) de R$ 10.00")
print(notas_5, "nota(s) de R$ 5.00")
print(notas_2, "nota(s) de R$ 2.00")
print("MOEDAS:")
print(notas_1, "moeda(s) de R$ 1.00")
print(moedas_50, "moeda(s) de R$ 0.50")
print(moedas_25, "moeda(s) de R$ 0.25")
print(moedas_10, "moeda(s) de R$ 0.10")
print(moedas_5, "moeda(s) de R$ 0.05")
print(moedas_1, "moeda(s) de R$ 0.01")