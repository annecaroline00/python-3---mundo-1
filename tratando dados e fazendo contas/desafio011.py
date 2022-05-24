largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area = largura*altura

qtd_tinta = area/2

print('A largura é {}, a altura é {}, a quantidade de tinta necessária será {}'.format(largura,altura,qtd_tinta))