salary = float(input())

if (salary <= 400):
    print("Novo salário: %.2f" % (salary * 1.15))
    print("Reajuste ganho: %.2f" % (salary * 0.15))
    print("Em percentual: 15 %")
if (salary > 400 and salary <= 800):
    print("Novo salário: %.2f" % (salary * 1.12))
    print("Reajuste ganho: %.2f" % (salary * 0.12))
    print("Em percentual: 12 %")
if (salary > 800 and salary <= 1200):
    print("Novo salário: %.2f" % (salary * 1.10))
    print("Reajuste ganho: %.2f" % (salary * 0.10))
    print("Em percentual: 10 %")
if (salary > 1200 and salary <= 2000.00):
    print("Novo salário: %.2f" % (salary * 1.07))
    print("Reajuste ganho: %.2f" % (salary * 0.07))
    print("Em percentual: 7 %")
if (salary > 2000):
    print("Novo salário: %.2f" % (salary * 1.04))
    print("Reajuste ganho: %.2f" % (salary * 0.04))
    print("Em percentual: 4 %")
