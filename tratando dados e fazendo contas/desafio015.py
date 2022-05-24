km = float(input('Quantos km o carro percorreu?'))
qtd_dias = int(input('Por quantos dias ele foi alugado?'))

preço_pagar = (60*qtd_dias) + (0.15*km)

print('O preço do aluguel é: R$ {:.2f}'.format(preço_pagar))