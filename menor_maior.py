print('Qual o número maior? \n')

num1 = float(input('Digite um número: '))
num2 = float(input('Digite um número: '))
num3 = float(input('Digite um número: '))

if num1 < num2 > num3:
  print('O número é maior', num2 )
elif num2 < num1 > num3:
  print('O número é maior', num1 )
elif num1 < num3 > num2:
  print('O número é maior', num3 )

if num1 > num2 < num3:
  print('O número é menor', num2 )
elif num2 > num1 < num3:
  print('O número é menor', num1 )
elif num1 > num3 < num2:
  print('O número é menor', num3 )


