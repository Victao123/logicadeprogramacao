comentário de uma linha  



primeiro_numero = int(input("Digite o segundo numero"))
segundo_numero=int(input("Digite outro número inteiro: "))


while primeiro_numero != segundo_numero:
    if primeiro_numero > segundo_numero:
        primeiro_numero = primeiro_numero - segundo_numero
    else:
        segundo_numero = segundo_numero - primeiro_numero

print("Os números ficaram iguais:", primeiro_numero, segundo_numero )
