from math import radians, cos, sin, tan,trunc
an = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(an))
print('O Ângulo de {}° tem o SENO de {:.2f}'.format(trunc(an), seno))
cos = cos(radians(an))
print('O ângulo de {}° tem o COSSENO de {:.2f}'.format(trunc(an), cos))
tg = tan(radians(an))
print('O ângulo de {}° tem a TANGENTE de {:.2f}'.format(trunc(an), tg))