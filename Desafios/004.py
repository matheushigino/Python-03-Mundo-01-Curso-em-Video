# Faça um programa que leia algo pelo
# teclado e mostra na tela o seu tipo
# primitivo e todas as informações possíveis sobre ele.

algo = input('Digite alguma coisa: ')
print('O item digitado é numérico? {}.'.format(algo.isnumeric()))
print('O item digitado é alfabético? {}.'.format(algo.isalpha()))
print('O item digitado é alfanumérico? {}.'.format(algo.isalnum()))
