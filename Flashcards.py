import random

status = {"correto": 0, "errado":0}

def flashcard(escolha):
    carta_1 = random.randint(0,100)
    carta_2 = random.randint(0,100)
    carta_3 = random.randint(1,100)
    
    if escolha == "add":
        resultado = carta_1 + carta_2
        resposta = input(f"Quanto é {carta_1} + {carta_2}: ")
        if int(resposta) == resultado:
            print("Esta certo ")
            status["correto"] += 1
        else:
            print(f"Esta errado, o correto é {resultado}")
            status["errado"] += 1
    
    if escolha == "sub":
        resultado = carta_1 - carta_2
        resposta = input(f"Quanto é {carta_1} - {carta_2}: ")
        if int(resposta) == resultado:
            print("Esta certo ")
            status["correto"] += 1
        else:
            print(f"Esta errado, o correto é {resultado}")
            status["errado"] += 1
    
    if escolha == "mult":
        resultado = carta_1 * carta_2
        resposta = input(f"Quanto é {carta_1} X {carta_2}: ")
        if int(resposta) == resultado:
            print("Esta certo ")
            status["correto"] += 1
        else:
            print(f"Esta errado, o correto é {resultado}")
            status["errado"] += 1
    
    if escolha == "div":
        while carta_1%carta_3 != 0:
            carta_1 = random.randint(0,100)
            carta_3 = random.randint(1,100)
        resultado = carta_1 / carta_3
        resposta = input(f"Quanto é {carta_1} / {carta_3}: ")
        if int(resposta) == resultado:
            print("Esta certo ")
            status["correto"] += 1
        else:
            print(f"Esta errado, o correto é {resultado}")
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