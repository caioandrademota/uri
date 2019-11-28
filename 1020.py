days = int(input())

years = int(days/365)
days = days - years*365

months = int(days/30)
days = days - months*30

print("%d ano(s)\n%d mes(es)\n%d dia(s)" %(years, months, days))
