print(90 * '- ')
print(18 * '-*', '  CAIXA ELETRONICO      ', 18 * '-*')
print(90 * '- ')

valor = int(input('Qual valor você deseja sacar?: R$ '))
total = valor

cedula = 50
total_cedulas = 0

while True:
    if total >= cedula:
        total -= cedula
        total_cedulas +=1
    else:
        if total_cedulas > 0:
            print(f'Total de {total_cedulas} de R$ {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula =1
        total_cedulas = 0
        if total == 0:
                        break
print(30 * '-')
print('Fim da operação')
