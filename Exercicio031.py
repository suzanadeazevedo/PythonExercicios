print('----------> PREÇO DA PASSAGEM <----------')
print(' O preço da passagem é  cobrado por km.\nViagem até 200 km é cobrado R$ 0,50 por km rodado.\nAcima de 200 km é cobrado R$0,45 por km rodado')
distancia = float(input('Digite quantos km terá  entre a origem e destino: '))
curto = distancia * 0.50
longo =  distancia * 0.45
if distancia <=200:
    print(' A distancia da viagem é de {:.1f} km. O preço da passagem é: R$ {:.2f}.'.format(distancia, curto))
else:
    print(' A distancia da viagem é de {:.1f} km. O preço da passagem é: R$ {:.2f}.'.format(distancia, longo))

