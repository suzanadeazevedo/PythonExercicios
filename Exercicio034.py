print('----------AUMENTO DO SALARIO----------')
salario = float(input('Digite o salario do funcionario: R$ '))
if salario >= 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15
print('Salario abaixo de R$ 1.250,00 tem aumento de 15%\nSalario acima de R$ 1.250,00 tem aumento de 10%')
print('O salario digitado foi {:.2f}\nApós o aumento o funcionario receberá : R$ {:.2f}'.format(salario, aumento + salario))

