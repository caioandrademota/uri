lanches = [4.00, 4.50, 5.00, 2.00, 1.50]

code, quantity = map(int, input().split(' '))

price = lanches[code-1] * quantity

print("Total: R$ %.2f" % price)
