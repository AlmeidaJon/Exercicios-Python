'''
                            Operações:

Fatiamento: fatiar string, é conseguir pegar pedaços dela

    Exemplo

frase = ('Curso em Vídeo Python')
print(frase[9:14])

    No exemplo acima, foi feito o comando de imprimir só a palavra vídeo, entendemos isso ao olhar o que esta dentro do
"print", em python as strins são numeradas e grardadas na memória, uma por uma, observando isso, vamos entender melhor
como funciona, foi impresso só a palavra vídeo, porque e foi colocado entre colchetes o número "9" e o número "14", se
contar cada caracter da frase, vamos ver que a letra "V" é o número "9", e o "14" é o espaço depois do "o", colocamos
um caracter depois de uma letra da qual queremos imprimir, porque em python não é considerado o último caracter colocado
    Se for colocado mais um ":" nos colchetes, colocar maia uma número tipo o "2", ele vai pular de duas em duas.

    Outra forma de fatiamento é omitir o primeiro número (início), exemplo: print(frase[:5]), com isso, vai ser impressa
a palavra "Curso" da nossa frase.

    Se indicar-mos só o início e omitir-mos o final (exemplo: print(frase[15:])), vai ser impresso do "P" até o final.

                            Análise

    Uma forma de analizar uma string, é ultilizando "len"(exemplo: print(len(frase))), ele mostra a quantidade de carac-
ter que temos na nossa frase(string).

    Outra forma de analisar uma string é usando "frase.count("o"), count conta quantas letras tem, nesse caso ele vai
contar quantos "o" (obs: minúsculos), tem na nossa frase.

    Outra forma de analizar uma string, é ultilizando "find"(encontrar), usando "frase,find("deo")" por exemplo, ele vai
identificar onde esta essa sequência de caracteres. Se você colocar dentro do find uma string que não existe, ele reto-
rna o valor "-1", então se você receber o valor "-1", quer dizer que não existe, ou que não foi encontrada.

    Outra forma de analisar uma string, é atravez do '(palavra desejada para a verificação)' in frase, esse é um modelo
de um operador, mas podemos fazer análise atravez dele, ao fazer isso, o programa irá nos retornar true(verdadeiro) ou
false(falso).

                         Transformação

  ->Uma lista de string, ela é imutável(não conseguimos mexer nela), mas podemos mexer nela atravéz dos métodos.

  ->Um desses métodos é o repleace(trocar, substituir), se fizermos "frase.repleace('Python','Android'), ele vai trocar
a palavra Python por Android, mas o repleace não substitui diretamente na string, ele substitui de uma foma secundária.

  ->Podemos usar o upper, ele vai deixar todas as letras maiúsculas, exemplo de uso: frase.upper(), ele mantém as que
já estão em maiúsculo e só muda as que estão em minúsculo.

  ->Podemos usar o lower também, o lower substitui as maiúsculas por minúsculas.

  ->Temos a capitalize, ele vai jogar todos os caracteres para minúsculos, e colocar só a primeira em maiúscula.

  ->Temos o title, ele parece o capitalize, só que ele identifica a quebra de linha e coloca toda a primeira letra em
maiúsculo(a).

  ->strip(), ele remove todos os espaços "inúteis" do início e do final da frase.
    Obs: Se colocar o r antes (ex: rstrip), ele vai começar a tratar só a parte da direita, então nesse caso ele iria
remover os espaços "inúteis" só da direita(os últimos espaços), e para fazer o contrário disso, retirar os espaços "inú-
teis" da esquerda, ultilizamos o l antes (lstrip).

                        Divizão

  ->split(), com isso, vamos dividir as strings, ele tecnicamente gera uma lista com todas as palavras de uma cadeia de
caracter. então se a frase for: Curso em vídeo Python, ele vai separar isso em listas, e númerar as palavras, ficaria:
0 = Curso, 1 = em, 2 = vídeos, 3 = Python.

                        Junção

  ->'-'.join(frase), de forma contraria do split, o '-'.join() vai juntar tudo isso, mas vai colocar esse "-" no lugar
dos espaços, mas se quiser colocar os espaços, é só colocar um espaço em branco, exemplo: ''.join().
'''
