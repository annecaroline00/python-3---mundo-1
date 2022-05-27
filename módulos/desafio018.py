from math import radians,sin,cos,tan

ang = int(input('Digite o ângulo: '))

seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))

print('o seno é {:.2f}, o cosseno é {:.2f}, a tangente é {:.2f}'.format(seno, cosseno, tangente))