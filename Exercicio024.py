print('*****Veja se o nome da cidade começa com "São"*****' )
cidade = str(input('Digite o nome de uma cidade: ')).strip()
print( cidade[:3].upper() == 'SÃO')