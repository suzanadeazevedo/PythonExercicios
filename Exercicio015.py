dias = int(input("Digite quantos dias o carro ficou alugado: "))
kmP = float(input("Digite quantos km o carro percorreu: "))

precoDia = int  (60) *dias
precoKm = float ( 0.15)  *kmP
total =  precoDia + precoKm

print('O carro foi alugado por {} dia(s) e rodou {} km\n O valor a ser pago pelo(s) dia(s) de aluguel é de R$ {:.2f} \n O valor a ser pago pelos km percorridos é R$ {:.2f}\n O valor total a ser pago é R${:.2f}'.format(dias, kmP, precoDia, precoKm, total))