print('Calculando excesso de peso do peixe')

peso_do_peixe = float(input('Qual o peso do peixe? '))
maximo_de_peso = 50
valor_multa = 4

if peso_do_peixe <= maximo_de_peso:
  print('Sem peso exedente')

else:
  print('O peso excedente foi: ', peso_do_peixe - maximo_de_peso)
  print('Valor do peso excedente: ', (peso_do_peixe - maximo_de_peso) * valor_multa)















