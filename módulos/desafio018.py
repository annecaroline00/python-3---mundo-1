from math import sin
from math import cos
from math import tan
from math import pi

ang = int(input('Digite o ângulo: '))/(180/pi)

seno = sin(ang)
cosseno = cos(ang)
tangente = tan(ang)

print('o seno é {:.2f}, o cosseno é {:.2f}, a tangente é {:.2f}'.format(ang, seno, cosseno, tangente))