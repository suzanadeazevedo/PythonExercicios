#Calcular soma de numeros impar, multiplos de 3
cont=0
soma= 0
for c in range(1, 501,2):
    if c % 3 == 0:
        cont= cont +1
        soma = soma + c
print(' A soma dos valores impares e multiplos de 3, totalizando {} números  no intervalo de 1 a 500  é: {} '.format(cont, soma))
