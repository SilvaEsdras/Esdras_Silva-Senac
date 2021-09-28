print('Calculando sua média!! \n')

nota1 = float(input('Qual foi sua primeira nota? \n'))
nota2 = float(input('Qual foi sua segunda nota? \n'))
media = (nota1 + nota2) / 2

if media == 10:
  print('Aprovado com Distinção')

elif media < 7:
  print('Reprovado')

elif 10 > media >= 7:
  print('Aprovado')

else:
  print('Média invalida')