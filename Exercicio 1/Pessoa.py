"""
Código utilizado para fins didáticos no Curso de Sistemas de Informação da Universidade Federal de Santa Maria - Campus Frederico Westphalen
Autor: Prof. Dr. Joel da Silva

Este módulo de exemplo implenta a Classe Pessoa.

"""


class Pessoa:
    """
    A Classe Pessoa encapsula um id, um nome, um sobrenome e uma idade
    """
    def __init__(self, id: int, sobrenome: str, nome: str, idade: int):
        """
        :param int id: Número Inteiro que será o identificador da pessoa
        :param str sobrenome: Sobrenome da pessoa
        :param str nome: Nome da pessoa
        :param int idade: Idade da pessoa

        """
        self.id = id
        self.sobrenome = sobrenome
        self.nome = nome
        self.idade = idade

    def getId(self):
        '''
        :return: (int) Identificador da Pessoa
        '''
        return self.id

    def getSobrenome(self):
        '''
        :return: (str) Sobrenome da Pessoa
        '''
        return self.sobrenome

    def getNome(self):
        '''
        :return: (str) Nome da Pessoa
        '''
        return self.nome

    def getIdade(self):
        '''
        :return: (int) Idade Pessoa
        '''
        return self.idade

    def getRegistro(self):
        '''
        :return: (str) Registro completo, com id, nome, sobrenome e idade
        '''
        return str(self.id) + " - " + self.nome + " " + self.sobrenome + " - " + str(self.idade)


if __name__ == '__main__':
    '''
    Exemplo de como criar um objeto pessoa: 
    '''
    p = Pessoa(1,'Silva','Maria',34)
    print(p.getRegistro())