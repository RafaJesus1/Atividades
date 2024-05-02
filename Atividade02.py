import random 

'''
Faça um algoritmo para ler dois vetores V1 e V2 de 15 números cada. Calcular e escrever a
quantidade de vezes que V1 e V2 possuem os mesmos números e nas mesmas posições.
'''

Vetor1 = []
Vetor2 = []

while len(Vetor1) < 15 and len(Vetor2) < 15:
    num_vetor1 = random.randint(1, 15)
    Vetor1.append(num_vetor1)

    num_vetor2 = random.randint(1, 15)
    Vetor2.append(num_vetor2)

qntd_num_repetidos = 0
posicao = 0
for i in (range(len(Vetor1)) and range(len(Vetor2))):
    posicao += 1
    if Vetor1[i] == Vetor2[i]:
        qntd_num_repetidos += 1
        print(f"Os números {Vetor1[i]} e {Vetor2[i]} são iguais e estão na mesma posição {posicao}")
            
print(f"Os vetores 1 e 2 tem exatamente {qntd_num_repetidos} números repetidos.")

