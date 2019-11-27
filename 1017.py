hour = int(input())
speed = int(input())

distance = speed * hour
gas_amount = distance/12
gas_amount = float(gas_amount)

print("%.3f" %gas_amount)
