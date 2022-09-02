from datetime import date

print( "========== Classificação de Atletas============")

birth = (int(input("Digite o ano do seu nascimento: ")))
year = date.today().year
age = year - birth
print("O seu ano de nascimento é: {}\nO atual ano é: {}\nSua idade é: {}".format(birth, year, age))
if age <= 9:
    print("Atleta MIRIM")
elif age<= 14:
    print("Atleta INFANTIL")
elif age <=19:
    print("Atleta JUNIOR")
elif age <=25:
    print("Atleta SENIOR")
else:
    print("Atleta MASTER")