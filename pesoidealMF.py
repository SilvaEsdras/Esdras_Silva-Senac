print('Vamos calcular o seu peso ideal? ')

sexo = input('Digite M para masculino \n ou Digite F para Feminino \n')
altura = float(input('Qual é sua altura? '))

if (sexo == "m", "M"):
  print('Seu peso ideal é', (72.7*altura)-58)

elif (sexo == "f", "F"):
  print('Seu peso ideal é', (62.1*altura)-44.7)

else:
  print('Sexo invalido')