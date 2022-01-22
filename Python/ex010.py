'''Faça um programa que leia um número de 0 a 9999, e mostre na tela cada um dos dígitos separados.

EX:
Digite um número: 1834

Unidade: 4
Dezena : 3
Centena: 8
Milhar : 1
'''

frase = input('Digite um número: ')

print('Unidade:',frase[3])
print('Dezena :',frase[2])
print('Centena:',frase[1])
print('Milhar :',frase[0])