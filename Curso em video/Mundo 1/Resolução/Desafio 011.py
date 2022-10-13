# 11- Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la.
# Sabendo que a cada litro de linta, pinta uma área e 2m²


l = float(input('Informe a largura da parede: '))
a = float(input('Informe a altura da parede: '))

# l = largura
# a = altura
# area = largura * altura

area = l * a
litro = area/2

print('\nSua parede tem {} de área'.format(area))
print('Você precisará de {} l de tinta para pintar essa parede'.format(litro))
