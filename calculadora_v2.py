# calculadora_v2.py

saida = ''  # controla a repetição do programa (S/N)

def adicao(a, b):
    return a + b

def subracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    return a / b

def calculadora(num1, num2, operacao):
    op = operacao.strip().lower()

    # aceita símbolo ou nome da operação
    if op in ['+', 'adicao', 'adição', 'soma', 'mais']:
        resultado = adicao(num1, num2)
    elif op in ['-', 'subracao', 'subtração', 'subtracao', 'menos']:
        resultado = subracao(num1, num2)
    elif op in ['*', 'x', 'multiplicacao', 'multiplicação', 'vezes']:
        resultado = multiplicacao(num1, num2)
    elif op in ['/', 'divisao', 'divisão', 'dividir']:
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida. Use +, -, *, / ou seus nomes."

    return resultado


# Loop principal
while saida not in ('n', 'N'):
    # lê os números; se digitar algo inválido, reinicia a iteração
    try:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida. Digite números válidos (ex.: 10, 3.5).")
        continue

    oper = input("Digite a operação (+, -, *, /) ou o nome (adição, subtração, multiplicação, divisão): ")

    resultado = calculadora(n1, n2, oper)
    print("Resultado da operação: " + str(resultado))

    saida = input("Deseja continuar? (S/N): ").strip()
