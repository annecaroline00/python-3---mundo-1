# a² = b² + c²
# Onde: a: representa a hipotenusa; 
# b e c: representa os catetos oposto e adjacente.

from math import sqrt

cateto_opo = int(input('O valor do cateto oposto é:'))
cateto_adj = int(input('O valor do cateto adjacente é: '))

hipotenusa = sqrt((cateto_opo**2) + (cateto_adj**2))

print('O comprimento da hipotenusa é {}'.format(hipotenusa))