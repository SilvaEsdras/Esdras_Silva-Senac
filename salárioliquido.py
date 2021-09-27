
salario_por_hora = float(input('Quanto você ganha por hora? \n'))
horas_trabalha_por_mes = float(input('Quantas horas você trabalha por mês? \n'))

salario_bruto = salario_por_hora*horas_trabalha_por_mes


imposto_de_renda = salario_bruto / 100 * 11
inss = salario_bruto / 100 * 8
sindicato = salario_bruto / 100 * 5
impostos = imposto_de_renda + inss + sindicato

salario_liquido = salario_bruto - impostos


print('Seu salário bruto é: R$\n', salario_bruto )

print('Você pagou 11% do IR que foi: R$\n' , imposto_de_renda)
print('Você pagou 8% do INSS que foi: R$\n', inss)
print('Você pagou 5% do Sindicato que foi: R$\n', sindicato)
print('Total de descontos: R$\n', impostos)

print('Seu salário é de: R$\n', salario_liquido)