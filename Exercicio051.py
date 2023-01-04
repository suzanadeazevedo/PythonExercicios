print('****Progressão aritmética****')
primeiro= int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10 -1) * razao

for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end= '  →  ')
print('Fim')