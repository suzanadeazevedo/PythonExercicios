print( 'Calculadora de Média - Alunos')

n1 = (float(input("Digite a primeira nota: ")))
n2 = (float(input("Digite a segunda nota: ")))

nota = (n1 + n2)/2

print("Nota um:  {:.1f} \nNota dois: {:.1f}\nA média do aluno é: {:.2f}".format(n1, n2, nota))
if nota <= 4.9:
    print("Média abaixo de 5.0: REPROVADO")
elif nota  >= 5.0 and nota <= 6.9 :
    print("Média entre 5.0 e 6.9: RECUPERAÇÃO")
else:
    print("Média 7.0 ou superior: APROVADO")


