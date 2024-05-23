
soma = lambda a, b: a + b
mult = lambda a, b: a * b
subt = lambda a, b: a - b
divi = lambda a, b: a / b 

simbolos = ("+", "-", "/", "*")

while True:
    a = int(input("Digite o valor de A: "))
    b = int(input("Digite o valor de B: "))

    simbolo = input("Digite o símbolo matemático: ")
    while simbolo not in simbolos:
        print("Tente novamente")
        print(f"Os símbolos matemáticos são: {simbolos}")
        simbolo = input("Digite o símbolo matemático: ")

    if simbolo == "+":
        print(soma(a, b))
    if simbolo == "-":
        print(subt(a, b))
    if simbolo == "/":
        print(divi(a, b))
    if simbolo == "*":
        print(mult(a, b))