# Crie um algoritmo que leia um número e mostre o seu dobro, multiplo e raiz quadrada.

j = int(input('Digite um número: '))
k = j * 2
l = j * 3
m = j ** (1/2)
print('O dobro de {}, vale {}.\nO triplo de {}, vale {}. \nA raiz quadrada de {}, é igual a {:.2f}.'.format(j, k, j, l, j, m))

'''
ou, Caso precise do antecessor ou do sucessor mais pra frente, o ideal seria guarda-lo em uma variável, então ficaria assim:

print('O dobro de {}, vale {}.'.format(j, (j*2)))
print('O triplo de {}, vale {}.'.format(j, (j*3)))
print('A raiz quadrada de {}, é igual a {:.2f}.'.format(j, (j**(1/2))))

\n = serve para fazer a quebra de linha.
o :.2f = foi usado como um tipo de formatação para o resultado da raiz quadrada, para não ficar um número gigante, da para formatar e deixar mais visível.
pow = função de potência, da para coloca-la para calcular a raiz quadrada também.
'''
