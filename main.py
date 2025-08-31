#Bibliotecas
from enum import Enum
from os import system, name as os_name
from time import sleep

# Possiveis Estados de uma Calculadora
class CalcState(Enum):
    START = 0
    INPUT = 1
    EXECUTE = 2
    pass

# Tipos de Operações que ela pode realizar
class Operation(Enum):
    ADD = 0
    SUB = 1
    MULT = 2
    DIV = 3
    EXP = 4
    SQR = 5
    PERCENT = 6
    pass

# Limpar Terminal (Ele checa qual OS tu ta rodando)
def clear_terminal():
    if os_name == 'nt':
        system('cls')
        pass
    else:
        system('clear')
    pass

# Variaveis
running = True
c_state = CalcState.START

operation = None
numA = numB = result = None

# Funções
def init_menu():
    global operation, running, c_state

    opicoes = (
        "Adição (+)",
        "Subtração (-)",
        "Multiplicação (*)",
        "Divisão (/)",
        "Potenciação (^)",
        "Raiz Quadrada (√)",
        "Porcentagem (%)"
    )

    clear_terminal()
    print("==================== Calculadora ====================")
    print("-> Digite o número correspondente ao tipo de operação\nque você deseja fazer:\n")
    for i, j in enumerate(opicoes):
        print(f'{i + 1}: {j}')
        pass

    escolha = input('\nOu para sair, digite "exit" ou "sair": ')
    try:
        temp = int(escolha) - 1
        operation = Operation(temp)
        c_state = CalcState.INPUT
    except:
        if escolha.lower() == "exit" or escolha.lower() == "sair":
            running = False
            clear_terminal()
            print("==================== Calculadora ====================\n")
            print("                - Saindo do Programa -")
            sleep(0.5)
            clear_terminal()
            pass
        else:
            clear_terminal()
            print("==================== Calculadora ====================")
            print("\n         - Opção invalida, tente novamente -\n")
            sleep(1)
            pass
        pass
    pass

def input_numbers():
    global operation, numA, numB, c_state

    simbolos = (
        "+",
        "-",
        "*",
        "/",
        "^",
        "√",
        "%"
    )

    clear_terminal()
    print("==================== Calculadora ====================")

    if numA == None:
        print(f'\n-> "1° Numero" {simbolos[operation.value]} "2° Numero" = "Resultado"')
        print("\n-> Digite o Primeiro Número abaixo.")

        escolha = input('Ou para voltar para o menu, digite "back" ou "voltar": ')

        try:
            numA = float(escolha)
        except:
            if escolha.lower() == "voltar" or escolha.lower() == "back":
                c_state = CalcState.START
                pass
            else:
                clear_terminal()
                print("==================== Calculadora ====================")
                print("\n        - Opção invalida, tente novamente -\n")
                sleep(1)
            pass
        pass
    elif numB == None:
        print(f'\n-> "{numA:g}" {simbolos[operation.value]} "2° Numero" = "Resultado"')
        print("\n-> Digite o Segundo Número abaixo.")

        escolha = input('Ou para voltar para a opção anterior, digite "back" \nou "voltar": ')

        try:
            numB = float(escolha)
            c_state = CalcState.EXECUTE
        except:
            if escolha.lower() == "voltar" or escolha.lower() == "back":
                numA = None
                pass
            else:
                clear_terminal()
                print("==================== Calculadora ====================")
                print("\n         - Opção invalida, tente novamente -\n")
                sleep(1)
            pass
        pass
    pass

def calculate():
    global operation, numA, numB, result, c_state, running
    
    simbolos = (
        "+",
        "-",
        "*",
        "/",
        "^",
        "√",
        "%"
    )

    clear_terminal()
    print("==================== Calculadora ====================")
    if operation != Operation.SQR:
        print(f'\n-> Expressão: {numA:g} {simbolos[operation.value]} {numB:g}')
        pass
    else:
        print(f'\n-> Expressão: {numA:g}{simbolos[operation.value]} {numB:g}')
        pass

    match operation:
        case Operation.ADD:
            result = numA + numB
            pass
        case Operation.SUB:
            result = numA - numB
            pass
        case Operation.MULT:
            result = numA * numB
            pass
        case Operation.DIV:
            try:
                result = numA / numB
                pass
            except ZeroDivisionError:
                result = "Inf"
                pass
            pass
        case Operation.EXP:
            result = numA ** numB
            pass
        case Operation.SQR:
            if numA < 0:
                result = "Undefined"
                pass
            else:
                result = numB ** (1/int(numA))
                pass
            pass
        case Operation.PERCENT:
            result = (numA / 100) * numB
            pass
    
    # Verifica se a variavel "result" é do tipo string 
    # Bug Fix de ultima hora, Já disse que odeio Python hoje?
    if isinstance(result, str):
        strResult = result
        pass
    # Caso nao for
    else:
        strResult = "{:.2g}".format(result) if ((operation == Operation.DIV) or (operation == Operation.SQR)) else "{:g}".format(result)
        pass
    print(f'\n-> O Resultado da Expressão é: {strResult}.')

    escolha = input('Deseja Sair do Programa [y/n]: ').lower()
    match escolha:
        case "y":
            running = False
            clear_terminal()
            print("==================== Calculadora ====================\n")
            print("                - Saindo do Programa -")
            sleep(0.5)
            clear_terminal()
            pass
        case "n":
            c_state = CalcState.START
            result = numA = numB = None
            pass
        case _:
            clear_terminal()
            print("==================== Calculadora ====================")
            print("\n        - Opção invalida, tente novamente -\n")
            sleep(1)
            pass
    pass

#Codigo Principal
while running:
    match c_state:
        case CalcState.START:
            init_menu()
            pass
        case CalcState.INPUT:
            input_numbers()
            pass
        case CalcState.EXECUTE:
            calculate()
            pass
    pass