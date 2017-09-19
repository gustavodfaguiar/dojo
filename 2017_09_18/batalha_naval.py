import unittest
from abc import ABC, abstractmethod


class Navio(ABC):
    def __init__(self, posicao_x, posicao_y):
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y

    @abstractmethod
    def tamanho(self):
        pass

class PortaAvioes(Navio):
    def tamanho(self):
        return 5

class Slot:
    def __init__(self, revelado):
        self.revelado = revelado

class Tabuleiro:
    def __init__(self):
        self.matriz = []

    def novo_jogo(self):
        for linha in range(0, 2):
            self.matriz.append([])
            for coluna in range(0, 2):
                self.matriz[linha].append(str(linha) + 'x' + str(coluna))

        print(self.matriz)

#class BatalhaNavalTest(unittest.TestCase):
#    def test_matriz(self):
#        pass
        #self.assertEqual()


if __name__ == '__main__':
   # unittest.main()
   tabuleiro = Tabuleiro()
   tabuleiro.novo_jogo()

