#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem  por extenso de zero até vinte.
# O programa deverá ler um numero pelo teclado (0-20) e mostralo por extenso
print (100*'-')
print ('NÚMERO POR EXTENSO')
print (100*'-')



cont = ('zero','um','dois','tres','quatro',
                'cinco','seis','sete','oito','nove','dez',
                'onze','doze','treze','quatorze','quinze',
                'dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
        numero_escolha = int(input('Digite um número entre 0 e 20: '))
        if 0 <=  numero_escolha <= 20:
            break
        print('Tente novamente. ', end=' ')
print (100*' *')
print(f' Você digitou o número {cont [numero_escolha]}')

