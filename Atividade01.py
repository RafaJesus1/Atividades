import random
'''
Faça um algoritmo para ler 50 números e armazenar em um vetor VET, verificar e escrever se
existem números repetidos no vetor VET e em que posições se encontram. 
'''
vet = []
num_repetidos = []

while len(vet) < 50:
    num = random.randint(1, 100)
    if num in vet:
        num_repetidos.append(num)
    vet.append(num)

i = 0
posicao = 0 
for i in range(len(vet)):
    posicao += 1
    if vet[i] in num_repetidos:
        print(f"Número repetido {vet[i]} na posição {posicao-1} do vetor")