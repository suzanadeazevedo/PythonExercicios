from datetime import date
print('*** Será que o ano é bissexto? ***')
ano = int(input('Digite o ano que quer analisar ou zero para o ano atual: '))
if ano == 0:
    ano=date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print('O ano {} É bissexto'.format(ano))
else:
     print('O ano {} NÃO é bissexto'.format(ano))