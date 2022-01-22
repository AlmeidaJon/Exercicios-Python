# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas aas informações possíveis sobre ele.

# Resposta
import inspect

jo = input('Digitite algo: ')
print('Só tem espaços?',jo.isspace())
print('É numérico?', jo.isnumeric())
print('É alfabético?', jo.isalpha())
print('Está em maiúsculas?', jo.isupper())
print('Está em minúsculas?', jo.islower())
print('Está capitalizada?', jo.istitle())
