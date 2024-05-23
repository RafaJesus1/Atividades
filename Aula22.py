
from ntpath import join

def calculo():
    if simbolo == "+":
        print(f"Resultado: {soma(a, b)}")
    if simbolo == "-":
        print(f"Resultado: {subt(a, b)}")
    if simbolo == "/":
        print(f"Resultado: {divi(a, b)}")
    if simbolo == "*":
        print(f"Resultado: {mult(a, b)}")

soma = lambda a, b: a + b
mult = lambda a, b: a * b
subt = lambda a, b: a - b
divi = lambda a, b: a / b 

simbolos = "+", "-", "/", "*"
 

while True:
    a = int(input("Digite o valor de A: "))
    b = int(input("Digite o valor de B: "))

    simbolo = input("Digite o símbolo matemático: ")
    while simbolo not in simbolos:
        print("Tente novamente")
        print(f"Os símbolos matemáticos são: {" | ".join(simbolos)}")
        simbolo = input("Digite o símbolo matemático: ")

    calculo()
    
    print("Deseja continuar? 1 para SIM e 0 para NÃO")
    opcao = int(input())

    while opcao != 1 or 0:
        print("Opção inválida.")
        print("Deseja continuar? 1 para SIM e 0 para NÃO")
        opcao = int(input())

    if opcao == 1:
        print("Faça uma nova operação")
    if opcao == 0:
        print("Saindo...")
        break


    




