nome =  str(input('Digite o seu nome completo: ')).strip()
busca =nome.split()
print('Seu primeiro nome é : {}'. format(busca[0]))
print('Seu ultimo nome é : {}'. format(busca[len(busca)-1]))