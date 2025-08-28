"""Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense."""

print (100*' ')
print (100*'-')
print ('Campeonato Brasileiro de Futebol')
print (100*'-')
print (100*' ')




times = ('Flamengo','Palmeiras','Cruzeiro Saf','Bahia',  'Botafogo',
               'Mirassol','São Paulo','Red Bull Bragantino','Fluminence','Ceará',
                'Corinthians','Atlético Mineiro Saf','Internacional','Gremio','Santos Fc',
                'Vasco da Gama','Vitória','Juventude','Fortaleza Ec Saf','Sport')

time = "Chapecoense"

print (100*'*')
print(f'Primeiros cinco colocados: ')
print(times[0:5])
print (100*'*')

print (100*'*')
print(f'Ultimos quatro colocados: ')
print(times[-4:])
print (100*'*')


print (100*'*')
print(f'Times em Ordem Alfabética: ')
print(sorted(times))
print (100*'*')

print (100*'*')
print(f'Em que posição está o time da Corinthians: ')
print(f'O Corinthians está na {times.index("Corinthians") + 1}ª posição')
print (100*'*')

print (100*'*')
print(f'Em que posição está o time da Chapecoense: ')
if time in times:
    posicao = times.index(times) + 1
    print(f'o {time} esta na posição {posicao}')
else:
    print(f'O{time} não esta na lista da Tabela A')

print (100*'*')
