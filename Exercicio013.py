valor = float(input('Digite o valor do seu salario R$: '))
aumento = valor * 0.15
print('Seu salario era R$ {:.2f}, com aumento de 15% você receberá R${:.2f}'.format(valor, valor + aumento))