print('Qual a ordem decresente? \n')

num1 = float(input('Digite um número: '))
num2 = float(input('Digite um número: '))
num3 = float(input('Digite um número: '))

if num1 > num2 and num1 > num3:
  if num2 > num3:
    print('A ordem decresente dos três numeros que você digitou é: ', num1, num2, num3)
  elif num2 < num3:
    print('A ordem decresente dos três numeros que você digitou é: ', num1 , num3, num2)

if num2 > num1 and num2 > num3:
  if num1 > num3:
    print('A ordem decresente dos três numeros que você digitou é: ', num2, num3, num1)
  elif num3 > num1:
    print('A ordem decresente dos três numeros que você digitou é: ', num2, num3, num1)

if num3 > num2 and num3 > num1:
  if num1 > num2:
    print('A ordem decresente dos três numeros que você digitou é: ', num3 , num1 , num2)
  elif num2 > num1:
    print('A ordem decresente dos três numeros que você digitou é: ', num3, num2, num1)