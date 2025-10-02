"""Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas
    – A maior nota
        – A menor nota
            – A média da turma
                – A situação (opcional)
"""


def notas(*n, sit=False):
    """
    -> Função para analisar notas dos alunos e sua situação escolar
    :param n: uma ou mais notas dos alunos (pode inserir quants valores forem necessarios)
    :param sit: valor opcional, se sit=True retornara a situação do aluno: Boa, razoavel ou ruim
    :return: retorna dicionário com as informações sobre as notas: quantas notas ao total foram informadas, maior nota, menor nota e média total do aluno
    """
    r = dict()
    r['total de notas informadas'] = len(n)
    r['maior nota'] = max(n)
    r['menor nota'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
      if r['média']  >= 7:
          r['situação'] = 'BOA'
      elif r['média'] >= 5:
          r['situação'] = 'RAZOAVEL'
      else:
          r['situação'] = 'RUIM'


    return r


# Programa principal:
resp = notas(10, 10, 9, 4, sit=True)
print(resp)
help(notas)
