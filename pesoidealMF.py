print('Vamos calcular o seu peso ideal? \n')

sexo = input('Digite 1 para masculino \n ou Digite 2 para Feminino \n')
altura = float(input('Qual é sua altura? '))

if (sexo == '1'):
  print('Seu peso ideal é', (72.7*altura)-58)

elif (sexo == '2'):
  print('Seu peso ideal é', (62.1*altura)-44.7)

else:
  print('Sexo invalido')
