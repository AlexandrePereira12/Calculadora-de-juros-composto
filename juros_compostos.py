import math
 
capital = float(input('Qual o capital investido? '))
juros = float(input('Qual o valor do juros em %? '))
tempo = int(input('Durante quanto meses vai render? '))
                    
juros = juros/100
tempo = tempo/12

def composto(capital, juros, tempo):

    return capital*pow((1+juros), tempo)

def simples(capital, juros, tempo):
    return capital*juros*tempo


valor_final = composto(capital, juros, tempo)

print(f'O valor final sera de R${valor_final:.02f}')

rendimento = valor_final - capital

print(f'Os juros de rendimento foram de R${rendimento:.02f}')


valor_simples = simples(capital, juros, tempo)

print(f'No juros simples o valor seria de: {(valor_simples + capital):.02f}')

