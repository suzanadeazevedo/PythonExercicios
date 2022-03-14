n1 = float (input ('Digiteo preço do produto: R$ '))
desconto = n1 * 0.05
print('O valor do produto era R$ {:.2f}, o valor do desconto de 5% é R$ {:.2f}\n O preço total a ser pago é R$ {:.2f}'. format(n1, desconto, n1 - desconto))