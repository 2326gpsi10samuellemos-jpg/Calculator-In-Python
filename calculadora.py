def adicionar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def calculadora():
    print("Bem-vindo à Calculadora em Python")
    print("Operações disponíveis: +, -, *, /")
    
    while True:
        a = input("Insere o primeiro número (ou 'sair' para terminar): ")
        if a.lower() == 'sair':
            break
        b = input("Insere o segundo número: ")
        operacao = input("Escolhe a operação (+, -, *, /): ")

        try:
            a = float(a)
            b = float(b)
        except ValueError:
            print("Erro: insere números válidos.")
            continue

        if operacao == '+':
            print("Resultado:", adicionar(a, b))
        elif operacao == '-':
            print("Resultado:", subtrair(a, b))
        elif operacao == '*':
            print("Resultado:", multiplicar(a, b))
        elif operacao == '/':
            print("Resultado:", dividir(a, b))
        else:
            print("Operação inválida. Tenta novamente.")

if __name__ == "__main__":
    calculadora()
