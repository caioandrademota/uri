def inputfunction(x ,y , z):
    x = int(x)
    y = int(y)
    z = float(z)
    value = float(y * z)
    return value

piece_code, piece_number, piece_value = input().split(' ')
piece_code2, piece_number2, piece_value2 = input().split(' ')
price = float()

price = inputfunction(piece_code,piece_number, piece_value) + inputfunction(piece_code2, piece_number2, piece_value2)

print("VALOR A PAGAR: R$ %.2f" % price)
