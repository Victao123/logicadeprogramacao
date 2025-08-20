import random

numero_secreto = random.randint(1, 100)
tentativas = 0
acertou = False


print("Bem-vindo ao jogo de adivinhação!")
print("Estou a pensar num número entre 1 e 100.")

while True:
    try:
        tentativas = int(input("Adivinhe o número: "))

        if tentativas == numero_secreto:
            acertou = True
            tentativas += 1
            print("Parabéns! Acertou em {tentativas} o número!")
            break
        elif tentativas < numero_secreto:
            print("O seu palpite é muito baixo. Tente novamente.")
        else:
            print("O seu palpite é muito alto. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")

