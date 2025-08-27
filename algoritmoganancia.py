notas_e_moedas = [200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]

valor_a_receber = float(input('Qual o valor a receber? '))
valor_recebido = float(input('Qual o valor recebido? '))

troco = (valor_recebido -valor_a_receber )  # Arredondar para evitar erros de ponto flutuante
print(f'Troco: {troco}')


for valor in notas_e_moedas: #200
        quantidade_de_itens = 0
        while valor <= troco : #200<300
            quantidade_de_itens += 1
            troco -= valor
        if quantidade_de_itens > 0:
            print(f'{quantidade_de_itens} itens de {valor}')
