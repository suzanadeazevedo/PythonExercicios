print(90 * '- ')
print(18 * '-*', '   LOJA SUPER BARATÃO      ', 18 * '-*')
print(90 * '- ')

contador_produto= 0
compra = 0
maior_valor = 0
menor_valor = 0
cont=0
barato = ' '

while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Digite o preço do produto: R$'))
    compra += preco
    cont += 1
    if preco > 1000:
        contador_produto +=1
    if cont == 1:
        menor_valor = preco
        barato = produto
    else:
        if preco < menor_valor:
            menor_valor = preco
            barato = produto
    continuar= ' '
    while continuar not in 'NS':
        continuar=str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break


print(f'O Total da compra foi de R$ {compra}')
print(f'Há {contador_produto} produto(s) custando mais de R$ 1.000,00')
print(f'o produto mais barato foi {barato} que custou R$ {menor_valor:.2f}')




