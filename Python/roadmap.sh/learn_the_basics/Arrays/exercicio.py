import math

print("==================================================================================")
#1) Faça um programa que possua um vetor denominado A que armazene 6 numeros inteiros. O programa deve executar os seguintes passos:

#(a) Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7. OK

A = []
A.append(1)
A.append(0)
A.append(5)
A.append(-2)
A.append(-5)
A.append(7)

#(b) Armazene em uma variavel inteira (simples) a soma entre os valores das posições #A[0], A[1] e A[5] do vetor e mostre na tela esta soma.
result_for_b = A[0] + A[1] + A[5]
print('A soma resulta em', result_for_b)

#(c) Modifique o vetor na posição 4, atribuindo a esta posição o valor 100.
A[4] = 100
print('Modificado posição 4', A)

#(d) Mostre na tela cada valor do vetor A, um em cada linha.
for x in A:
    print(x)


#2) Crie um programa que le 6 valores inteiros e, em seguida, mostre na tela os valores lidos.
print("==================================================================================")
LIMIT = 6
x = 1
seis_valores_inteiros = []
while x <= LIMIT:
    itn = x #int(input('Digite um número inteiro:'))
    seis_valores_inteiros.insert(x, itn)
    x += 1
for ni in seis_valores_inteiros:
    print(ni, 'é um número inteiro')


#3) Ler um conjunto de numeros reais, armazenando-o em vetor e calcular o quadrado das componentes deste vetor,
# armazenando o resultado em outro vetor. Os conjuntos tem 10 elementos cada. Imprimir todos os conjuntos.
print("==================================================================================")
first_vetor = [3.1, 12.5, 5.5, 10.5, 1.4, 2.55, 1.64, 45.8, 12.2, 12.4]
second_vetor = []

for a in first_vetor:
    raiz = math.sqrt(a)
    second_vetor.append(raiz)

print(first_vetor)
print(second_vetor)

#4)Faça um programa que leia um vetor de 8 posições e, em seguida, leia tambem dois valores X e Y quaisquer
# correspondentes a duas posicoes no vetor. Ao final seu programa devera escrever a soma dos valores
# encontrados nas respectivas posicoes X e Y
print("==================================================================================")
third_vetor = [50, 63, 20, 10 ,44 ,65, 100, 98.6]
a1 = 3
a2 = 6

va1 = third_vetor[a1]
va2 = third_vetor[a2]
print('A soma entre os dois é: ', va1 + va2)

#5) Leia um vetor de 10 posicoes. Contar e escrever quantos valores pares ele possui.
print("==================================================================================")
fourth_vetor = [20, 44, 96, 40, 100, 30, 9, 7, 11, 13]
pars_numbers = 0
for fv in fourth_vetor:
    is_par = fv % 2 == 0
    if is_par: pars_numbers += 1

print('Temos', pars_numbers, 'valores pares no array')

#6) Fac¸a um programa que receba do usuario um vetor com 10 posicoes. Em seguida devera ser impresso
# o maior e o menor elemento do vetor.
print("==================================================================================")

#7) Escreva um programa que leia 10 numeros inteiros e os armazene em um vetor. Imprima o vetor, o maior elemento e
# a posicao que ele se encontra.
print("==================================================================================")

#8) Crie um programa que le 6 valores inteiros e, em seguida, mostre na tela os valores lidos na ordem inversa.
print("==================================================================================")

#9) Crie um programa que le 6 valores inteiros pares e, em seguida, mostre na tela os valores lidos na ordem inversa.
print("==================================================================================")

#10) Faca um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule e imprima a media geral.
print("==================================================================================")

#11) Faca um programa que preencha um vetor com 10 numeros reais, calcule e mostre a quantidade de numeros negativos e
# a soma dos numeros positivos desse vetor.
print("==================================================================================")

#12) Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos juntamente com o maior, o menor
# e a media dos valores.
print("==================================================================================")

#13) Fazer um programa para ler 5 valores e, em seguida, mostrar a posicao onde se encontram o maior e o menor valor
print("==================================================================================")


#14) Faca um programa que leia um vetor de 10 posicoes e verifique se existem valores iguais
#e os escreva na tela.
print("==================================================================================")

#15) Leia um vetor com 20 numeros inteiros. Escreva os elementos do vetor eliminando ele-
#mentos repetidos.
print("==================================================================================")

#16) Faca um programa que leia um vetor de 5 posicoes para numeros reais e, depois, um
#codigo inteiro. Se o codigo for zero, finalize o programa; se for 1, mostre o vetor na ordem
#direta; se for 2, mostre o vetor na ordem inversa. Caso, o codigo for diferente de 1 e 2
#escreva uma mensagem informando que o codigoe invalido.
print("==================================================================================")

#17) Leia um vetor de 10 posicoes e atribua valor 0 para todos os elementos que possuırem
#valores negativos.
print("==================================================================================")

#18) Faca um programa que leia um vetor de 10 numeros. Leia um numerox. Conte os
#multiplos de um numero inteirox num vetor e mostre-os na tela.
print("==================================================================================")

#19) Faca um vetor de tamanho 50 preenchido com o seguinte valor: (i+ 5 ∗ i)%(i+ 1), sendo
#i a posicao do elemento no vetor. Em seguida imprima o vetor na tela.
print("==================================================================================")

#20) Escreva um programa que leia numeros inteiros no intervalo [0,50] e os armazene em um
#vetor com 10 posicoes. Preencha um segundo vetor apenas com os numeros ımpares
#do primeiro vetor. Imprima os dois vetores, 2 elementos por linha.
print("==================================================================================")

#21) Faca um programa que receba do usuario dois vetores,A e B, com 10 numeros inteiros
#cada. Crie um novo vetor denominado C calculando C = A - B. Mostre na tela os dados
#do vetor C.
print("==================================================================================")

#22) Faca um programa que leia dois vetores de 10 posicoes e calcule outro vetor contendo,
#nas posicoes pares os valores do primeiro e nas posicoes impares os valores do segundo.
print("==================================================================================")

#23) Ler dois conjuntos de numeros reais, armazenando-os em vetores e calcular o produto
#escalar entre eles. Os conjuntos tem 5 elementos cada. Imprimir os dois conjuntos e o
#produto escalar, sendo que o produto escalar e dado por:x1 ∗ y1 + x2 ∗ y2 + ... + xn ∗ yn.
print("==================================================================================")

#24) Faca um programa que leia dez conjuntos de dois valores, o primeiro representando o
#numero do aluno e o segundo representando a sua altura em metros. Encontre o aluno
#mais baixo e o mais alto. Mostre o numero do aluno mais baixo e do mais alto, juntamente
#com suas alturas.
print("==================================================================================")

#25) Faca um programa que preencha um vetor de tamanho 100 com os 100 primeiros naturais que nao sao multiplos de 7
# ou que terminam com 7.
print("==================================================================================")


#27) Leia 10 numeros inteiros e armazene em um vetor. Em seguida escreva os elementos
#que sao primos e suas respectivas posicoes no vetor.
print("==================================================================================")

#28) Leia 10 numeros inteiros e armazene em um vetor v. Crie dois novos vetores v1 e v2.
#Copie os valores ımpares de v para v1, e os valores pares de v para v2. Note que cada
#um dos vetores v1 e v2 tem no maximo 10 elementos, mas nem todos os elementos sao
#utilizados. No final escreva os elementos UTILIZADOS de v1 e v2
print("==================================================================================")

#29) Faca um programa que receba 6 numeros inteiros e mostre:
#• Os numeros pares digitados
#• A soma dos numeros pares digitados
#• Os numerosımpares digitados
#• A quantidade de numeros ımpares digitados;
print("==================================================================================")

#30) Faca um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a
#interseccao entre os 2 vetores anteriores, ou seja, que contem apenas os n umeros que
#estao em ambos os vetores. Nao deve conter numeros repetidos.
print("==================================================================================")

#31) Faca um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a uniao
#entre os 2 vetores anteriores, ou seja, que contem os n umeros dos dois vetores. Nao
#deve conter numeros repetidos.
print("==================================================================================")

#32) Leia dois vetores de inteiros x e y, cada um com 5 elementos (assuma que o usuario nao
#informa elementos repetidos). Calcule e mostre os vetores resultantes em cada caso
#abaixo:
#• Soma entre x e y: soma de cada elemento de x com o elemento da mesma posicao
#em y.
#• Produto entre x e y: multiplicacao de cada elemento dex com o elemento da mesma
#posicao emy.
#• Diferenca entre x e y: todos os elementos de x que nao existam emy.
#• Intersecao entrex e y: apenas os elementos que aparecem nos dois vetores.
#• Uniao entrex e y: todos os elementos de x, e todos os elementos de y que nao
#estao emx.
print("==================================================================================")


#33) Faca um programa que leia um vetor de 15 posicoes e o compacte, ou seja, elimine as
#posicoes com valor zero. Para isso, todos os elementosa frente do valor zero, devem ser
#movidos uma posicao para tras no vetor.
print("==================================================================================")

#34) Faca um programa para ler 10 numeros DIFERENTES a serem armazenados em um
#vetor. Os dados deverao ser armazenados no vetor na ordem que forem sendo lidos,
#sendo que caso o usuario digite um n umero que j a foi digitado anteriormente, o programa
#devera pedir para ele digitar outro n umero. Note que cada valor digitado pelo usu ario
#deve ser pesquisado no vetor, verificando se ele existe entre os numeros que j a foram
#fornecidos. Exibir na tela o vetor final que foi digitado.
print("==================================================================================")

#35) Faca um programa que leia dois numeros a e b (positivos menores que 10000) e:
#Crie um vetor onde cada posicao e um algarismo do n umero. A primeira posic ao e
#o algarismo menos significativo;
#Crie um vetor que seja a soma de a e b, mas faca-o usando apenas os vetores
#construıdos anteriormente.
#Dica: some as posicoes correspondentes. Se a soma ultrapassar 10, subtraia 10 do
#resultado e some 1 a pr ` oxima posic ao.
print("==================================================================================")

#36) Leia um vetor com 10 numeros reais, ordene os elementos deste vetor, e no final escreva
#os elementos do vetor ordenado.

#37) Considere um vetor A com 11 elementos onde A1 < A2 < · · · < A6 > A7 > A8 >
#· · · > A11, ou seja, esta ordenado em ordem crescente at e o sexto elemento, e a partir
#desse elemento esta ordenado em ordem decrescente. Dado o vetor da quest ao anterior,
#proponha um algoritmo para ordenar os elementos.
print("==================================================================================")

#38) Peca ao usuario para digitar dez valores num ericos e ordene por ordem crescente esses
#valores, guardando-os num vetor. Ordene o valor assim que ele for digitado. Mostre ao
#final na tela os valores em ordem.
print("==================================================================================")

#39) Escreva um programa que leia um numero inteiro positivo n e em seguida imprima n
#linhas do chamado Triangulo de Pascal:
#1
#1 1
#1 2 1
#1 3 3 1
#1 4 6 4 1
#1 5 10 10 5 1
print("==================================================================================")