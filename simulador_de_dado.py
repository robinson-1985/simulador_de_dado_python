# Simular o uso de um dado, gerando um valor de 1 a 6

import random
class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um valor para o dado?'

    def Iniciar(self):
            resposta = input(self.mensagem)
            if resposta == 'sim':
                self.GerarValorDoDado()

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))



