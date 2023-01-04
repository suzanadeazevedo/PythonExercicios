print( "="*40)
print("             GERENCIADOR DE PAGAMENTOS")
print( "="*40)

valor_produto = float(input('Preço da compra: R$ '))
print('''\nFORMAS DE PAGAMENTO\n''')

print('[ 1 ] a vista dinheiro/cheque')
print('[ 2 ] a vista cartão')
print('[ 3 ] Parcelado: 2x no cartão')
print('[ 4 ] Parcelado 3x ou mais no cartão')

opcao_pagamento =int( input('Digite a opção de pagamento: '))

if opcao_pagamento == 1:
    desconto_dinheiro = valor_produto -  (valor_produto * 0.1)
    print('A compra de  R$: {:.2f} terá desconto de 10% e ficará em R$: {:.2f} '.format(valor_produto, desconto_dinheiro))
elif opcao_pagamento == 2:
    desconto_cartao = valor_produto - (valor_produto *0.05)
    print( 'A compra de  R$: {:.2f} terá desconto de 5% e ficará em R$: {:.2f} '.format(valor_produto, desconto_cartao))
elif opcao_pagamento == 3:
    duas_parcelas = valor_produto  / 2
    print('A compra de R$: {:.2f} será pacerla em 2x de R$: {:.2f}'.format(valor_produto, duas_parcelas))
elif opcao_pagamento == 4:
    numero_parcelas = int(input("Digite o numero de parcelas desejada: "))
    juros_parcela =  (valor_produto + (valor_produto * 0.2 )) / numero_parcelas
    preço_final = (juros_parcela * numero_parcelas)
    print('A compra de R$: {:.2f} será pacerla em {}x  e terá  juros de 20%. O valor da parcela será de R$: {:.2f}'.format(valor_produto, numero_parcelas, juros_parcela))
    print('Preço Total com Juros R$: {:.2f} '.format(preço_final))
else:
    print('Opção invalida, tente outra vez')
