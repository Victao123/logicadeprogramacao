import random

def jogar_adivinhacao():
  """
  Função para o jogo de adivinhação.
  """
  nome_jogador = input("Antes de começarmos, qual é o seu nome? ")
  numero_secreto = random.randint(1, 100)
  tentativas = 0
  acertou = False
  tentativas_passadas = []

  print(f"\nOlá, {nome_jogador}! Bem-vindo ao jogo de adivinhação ")
  print("Tente adivinhar um número entre 1 e 100.")

  while not acertou:
    tentativa = int(input("Digite seu palpite: "))
    tentativas += 1
    tentativas_passadas.append(tentativa)
    if tentativa == numero_secreto:
      acertou = True
      
      print(f"Parabéns, {nome_jogador}! Você acertou o número em {tentativas} tentativas.")
      print(tentativas_passadas)
    elif tentativa < numero_secreto:
      print("Tente um número maior.")
    else:
      print("Tente um número menor.")

jogar_adivinhacao()
