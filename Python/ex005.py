# Faça um programa que leia um número interiro, e mostre na tela o seu sucessor e seu antecessor

j = int(input('Digite um número: '))
n1 = j - 1
n2 = j + 1
print('De acordo com o número {}, seu antecessor é {}, e o sucessor é {}'.format(j, n1, n2))

'''
Caso precise do antecessor ou do sucessor mais pra frente, o ideal seria guarda-lo em uma variável, então ficaria
assim
'''

print('De acordo com o número {}, seu antecessor é {}, e o sucessor é {}'.format(j, (j-1), (j+1)))
