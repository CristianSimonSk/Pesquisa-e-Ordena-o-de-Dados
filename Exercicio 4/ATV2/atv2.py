from difflib import Match
import math
from Gerador import Gerador

class Jogador:

    def __init__(self, codigo: int, nome: str, sobrenome:str, idade: int, quantiPart: int, quantiGols: int):
        self.codigo = codigo
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.quantiPart = quantiPart
        self.quantiGols = quantiGols

    def getCodigo(self):
        return self.codigo

    def getSobrenome(self):
        return self.sobrenome

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade

    def getQuantGols(self):
        return self.quantiGols

    def getQuantParti(self):
        return self.quantiPart

    def getRegistro(self):
        return "\nCódigo: " + str(self.codigo) + "\nNome: " + self.nome + "\nSobrenome: " + self.sobrenome + "\nIdade: " + str(self.idade) + "\nQuantidade de Gols: " + str(self.quantiGols) + "\nQuantidade de Partidas: " + str(self.quantiPart)

    

jo = Gerador()
jogadores = []
x = 0

def insertionSort(jogadores):

    for i in range(1, len(jogadores)):
        key = jogadores[i].getCodigo()
        aux = jogadores[i]
        j = i - 1
        while j >= 0 and jogadores[j].getCodigo() > key:
            jogadores[j + 1] = jogadores[j]
            j -= 1
            jogadores[j + 1] = aux 
            
def selectionSort(jogadores):
    for i in range(len(jogadores) - 1, 0, -1):
        maior_idx = 0
        for j in range(1, i + 1):
            if jogadores[j].getQuantGols() > jogadores[maior_idx].getQuantGols(): 
                maior_idx = j

        temp = jogadores[i]
        jogadores[i] = jogadores[maior_idx]
        jogadores[maior_idx] = temp


def bubbleSort(jogadores):
    
    for i in range(len(jogadores)-1,0,-1):
        for j in range(i):
            if jogadores[j].getNome() > jogadores[j+1].getNome():
                temp = jogadores[j]
                jogadores[j] = jogadores[j+1]
                jogadores[j+1] = temp   

def salvar():
    print("Criando Arquivo....")
    arquivoListaJogadores = open('arquivoListaJogadores.txt','w')
    print("Salvando Arquivo")
    for i in range(len(jogadores)):
        arquivoListaJogadores.write(jogadores[i].getRegistro() + "\n")
        print(".")
    arquivoListaJogadores.close()
    print("Arquivo Salvo")
    menu()            

def menu():
    op = 1

    while(op != 0):
        op2 = int(input("\nInsira o numero que voce deseja executar \n1 - Cadastrar \n2 - Pesquisar\n3 - Excluir\n4 - Listar\n5 - Ordenar Por Nome\n6 - Ordenar Por Código\n7 - Ordenar Por Gols\n8 - Salvar\n0 - Sair\n"))
        match(op2):
            case 1: 
                x = int(input("\nQuantos jogadores deseja adicionar\n"))
                for i in range(x):
                    a = Jogador(i+1, jo.geraNome(), jo.geraSobrenome(), jo.geraIdade(), jo.geraPart(), jo.geraGols())
                    jogadores.append(a)

            case 2: 
                y = int(input("\nInsira o código do jogador que voce deseja consultar\n"))
                for i in range(len(jogadores)):
                    if(jogadores[i].getCodigo() == y):
                        print(jogadores[i].getRegistro())

            case 3: 
                z = int(input("\nInsira o código do jogador a ser excluido\n"))
                for i in range(len(jogadores)):
                    if(jogadores[i].getCodigo() == z):
                        jogadoraux = jogadores[i]
                jogadores.remove(jogadoraux)        

            case 4: 
                for i in range(len(jogadores)):
                    print(jogadores[i].getRegistro())

            case 5: 
                bubbleSort(jogadores)
                for i in range(x):
                    print(jogadores[i].getRegistro())

            case 6: 
                insertionSort(jogadores)
                for i in range(x):
                    print(jogadores[i].getRegistro())

            case 7: 
                selectionSort(jogadores)
                for i in range(x):
                    print(jogadores[i].getRegistro())

            case 8: 
                salvar()

            case 0: 
                op = 0

menu()