print('Qual o menor? \n')

produto1 = float(input('Digite o preço do produto: '))
produto2 = float(input('Digite o preço do produto: '))
produto3 = float(input('Digite o preço do produto: '))

if produto1 > produto2 < produto3:
  print('Sugerimos o protudo de valor: ', produto2 )
elif produto2 > produto1 < produto3:
  print('Sugerimos o protudo de valor:', produto1 )
elif produto1 > produto3 < produto2:
  print('Sugerimos o protudo de valor:', produto3 )