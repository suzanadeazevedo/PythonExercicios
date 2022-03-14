# Cotação dolar 14/03/2022 US$ = 5,12
dolar = float (5.12)
realTotal = float(input('Digite a quantia de dinheiro que você tem (R$): '))
print('Com a quantia de R$ {:.2f}, você pode comprar US$ {:.2f}'. format(realTotal, realTotal / dolar))