print ('------- Aprovando Empréstimo--------')

preco =  float(input('Digite o valor total do preço da casa, sem ponto: R$'))
salario = float(input('Digite o valor do do seu salário, sem ponto: R$ '))
ano = int(input('Digite em quantos anos você pretende pagar: '))
prestacao = (preco  /( ano * 12))

print ('Para pagar uma casa de R$ {:.2f} em {} anos, a prestação será de R${:.2f}'.format(preco, ano, prestacao))

if prestacao  <= 0.30 * salario:
    print('Empréstimo CONCEDIDO')
else:
    print('Empréstimo NEGADO')





