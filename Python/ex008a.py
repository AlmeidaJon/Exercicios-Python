'''import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz do número {}, é igual a {}'.format(num, math.ceil(raiz)))
'''
'''
    O math.ceil foi usado para arredondar o valor para cima, mas poderia usar o floor para arredondar para baixo
ou da para formatar dentro das chaves o número para não ficar um número grande, para isso usamos ":.+a quantidade que 
você quer + f (float).
'''

# ou

'''
from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz do número {}, é igual a {}'.format(num, floor(raiz)))
'''
'''
Ao importar uma função só, não é preciso ultilizar a referência "math. + a função",
No site python.org podemos achar outras funções para incluir no programa.
'''
'''
Na parte "import random" pedimos para o computador nos enviar números aleatórios reais entre 0 e 1, para colocar números
inteiros, temos que colocar a função ".randint", essa função permite colocar o número desejado, assim você escolhe de 
qual número até qual número o computador vai apresentar.
'''
'''
    Exemplo

import random
num = random.randint(1,15)
print(num)
'''
import emoji
print(emoji.emojize('Python is :thumbs_up:'))
