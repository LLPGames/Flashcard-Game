import random
import operator

status = {"correto": 0, "errado":0}

operacoes = {
    "add": ("+", operator.add),
    "sub": ("-", operator.sub),
    "mult": ("x", operator.mul),
    "div": ("/", operator.floordiv)  # divisão inteira
}

def flashcard(escolha):
    carta_1 = random.randint(0,100)
    carta_2 = random.randint(0,100)
    carta_3 = random.randint(1,100)
    
    if escolha == "div":
        while carta_1 % carta_3 != 0:
            carta_1 = random.randint(0,100)
            carta_3 = random.randint(1,100)
        resultado = carta_1 // carta_3
        pergunta = f"Quanto é {carta_1} / {carta_3}: "
    else:
        simbolo, func = operacoes[escolha]
        resultado = func(carta_1, carta_2)
        pergunta = f"Quanto é {carta_1} {simbolo} {carta_2}: "
        
    resposta = input(pergunta)
    try:
        if int(resposta) == resultado:
            print("Está certo")
            status["correto"] += 1
        else:
            print(f"Está errado, o correto é {resultado}")
            status["errado"] += 1
    except ValueError:
        print(f"Entrada inválida! O correto seria {resultado}")
        status["errado"] += 1
    
while True:
    print("escolha o tipo do jogo")
    escolha = input ("add/sub/mult/div: ").lower()

    while escolha not in ["add", "sub", "mult", "div"]:
        escolha = input("operação não reconhecida, escolha novamente: ").lower()

    flashcard(escolha)
 
    print(f"você acertou {status['correto']} e errou {status['errado']}")
    continuar = input ("Gostaria de jogar novamente?"
                       "Sim/Não: ").lower()
    
    while continuar not in ["sim" , "não"]:
        continuar = input("Opção inválida digite novamente: ").lower()

    if continuar != "sim":
        print("adeus")
        break