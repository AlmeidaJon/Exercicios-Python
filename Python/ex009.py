'''
  -> Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadam-
ente.

EX: Ana Maria de Souza
Primeito: Ana
Último: Souza
'''

nome = input('Nome completo: ')
print('Primeiro nome:',nome.split()[0])
print('Último nome:',nome.split()[3:])