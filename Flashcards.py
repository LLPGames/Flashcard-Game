import random
import operator

# Dicionário que armazena o número de respostas corretas e erradas do usuário
status = {"correto": 0, "errado": 0}

# Dicionário que mapeia os nomes das operações para seus símbolos e funções da biblioteca operator
operacoes = {
    "add": ("+", operator.add),     # Soma
    "sub": ("-", operator.sub),     # Subtração
    "mult": ("x", operator.mul),    # Multiplicação
    "div": ("/", operator.floordiv) # Divisão inteira
}

def flashcard(escolha):
    # Gera números aleatórios para as cartas
    carta_1 = random.randint(0, 100)
    carta_2 = random.randint(0, 100)
    carta_3 = random.randint(1, 100)  # Para divisão, evita zero no divisor
    
    # Caso especial para divisão: garante que a conta seja exata (sem resto)
    if escolha == "div":
        while carta_1 % carta_3 != 0:  # Repete até encontrar divisão exata
            carta_1 = random.randint(0, 100)
            carta_3 = random.randint(1, 100)
        resultado = carta_1 // carta_3
        pergunta = f"Quanto é {carta_1} / {carta_3}: "
    else:
        # Obtém o símbolo e a função da operação escolhida
        simbolo, func = operacoes[escolha]
        resultado = func(carta_1, carta_2)
        pergunta = f"Quanto é {carta_1} {simbolo} {carta_2}: "
        
    # Pede a resposta do usuário
    resposta = input(pergunta)
    try:
        # Verifica se a resposta está correta
        if int(resposta) == resultado:
            print("Está certo")
            status["correto"] += 1
        else:
            print(f"Está errado, o correto é {resultado}")
            status["errado"] += 1
    except ValueError:
        # Caso o usuário digite algo que não seja número
        print(f"Entrada inválida! O correto seria {resultado}")
        status["errado"] += 1
    

# Loop principal do jogo
while True:
    print("Escolha o tipo do jogo")
    escolha = input("add/sub/mult/div: ").lower()

    # Valida a escolha do usuário
    while escolha not in ["add", "sub", "mult", "div"]:
        escolha = input("Operação não reconhecida, escolha novamente: ").lower()

    # Executa uma rodada do flashcard
    flashcard(escolha)
 
    # Mostra o placar
    print(f"Você acertou {status['correto']} e errou {status['errado']}")
    
    # Pergunta se o usuário quer continuar jogando
    continuar = input("Gostaria de jogar novamente? Sim/Não: ").lower()
    
    # Valida a entrada do usuário
    while continuar not in ["sim", "não"]:
        continuar = input("Opção inválida, digite novamente: ").lower()

    # Se a resposta for não, encerra o jogo
    if continuar == "não":
        print("Adeus")
        break
