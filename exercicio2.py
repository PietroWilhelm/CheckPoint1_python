salario = float(input('Salario: '))

if salario <= 1903.98:
    print('isento')
elif salario >= 1903.99 and salario <= 2826.65:
    ir = salario * 0.075
elif salario >= 2826.65 and salario <= 3751.06:
    ir = salario * 0.15
elif salario >= 3751.07 and salario <= 4664.68:
    ir = salario * 0.2
elif salario >= 4664.69:
    ir = salario *0.25

pagar = ir + salario
print(f'você tem que pagar R${ir} de imposto')
print(f'você tem que pagar um total de R$ {pagar}')