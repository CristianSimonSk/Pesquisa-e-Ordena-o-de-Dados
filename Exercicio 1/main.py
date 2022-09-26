from Pessoa import Pessoa
from Gerador import Gerador
 
def SelectionSortId(v):
    for i in range(len(v) - 1, 0, -1):
        maior_idx = 0
        for j in range(1, i + 1):
            if v[j].getId() > v[maior_idx].getId():
                maior_idx = j

        temp = v[i]
        v[i] = v[maior_idx]
        v[maior_idx] = temp

def SelectionSortIdade(v):
    for i in range(len(v) - 1, 0, -1):
        maior_idx = 0
        for j in range(1, i + 1):
            if v[j].getIdade() > v[maior_idx].getIdade(): 
                maior_idx = j

        temp = v[i]
        v[i] = v[maior_idx]
        v[maior_idx] = temp

def SelectionSortNome(v):
    for i in range(len(v) - 1, 0, -1):
        maior_idx = 0
        for j in range(1, i + 1):
            if v[j].getNome() > v[maior_idx].getNome(): 
                maior_idx = j

        temp = v[i]
        v[i] = v[maior_idx]
        v[maior_idx] = temp

def SelectionSortSobrenome(v):
    for i in range(len(v) - 1, 0, -1):
        maior_idx = 0
        for j in range(1, i + 1):
            if v[j].getSobrenome() > v[maior_idx].getSobrenome(): 
                maior_idx = j

        temp = v[i]
        v[i] = v[maior_idx]
        v[maior_idx] = temp

numero_contatos = 10
contatos = []
g = Gerador()
for i in range(numero_contatos):
    p = Pessoa(i+1, g.geraSobrenome(), g.geraNome(), g.geraIdade())
    contatos.append(p)

var = int(input("\nInsira por qual item voce deseja ordenar\n\n1-Por ID\n2-Por NOME\n3-Por SOBRENOME\n4-Por IDADE\n"))
if (var == 1):
    print("Vetor Original")
    for k in range(numero_contatos):
        print(contatos[k].getRegistro())

    SelectionSortid(contatos)

    print("Vetor Ordenado")
    for k in range(numero_contatos):
        print(contatos[k].getRegistro())
elif (var == 2):
    print("Vetor Original")
    for k in range(numero_contatos):
        print(contatos[k].getRegistro())
    SelectionSortIdade(contatos)
    print("Vetor Ordenado")
    for k in range(numero_contatos):
        print(contatos[k].getRegistro())
elif (var == 3):
    print("Vetor Original")
    for k in range(numero_contatos):
        print(contatos[k].getRegistro())
    SelectionSortNome(contatos)
    print("Vetor Ordenado")
    for k in range(numero_contatos):
        print(contatos[k].getRegistro())
elif (var == 4):
    print("Vetor Original")
    for k in range(numero_contatos):
        print(contatos[k].getRegistro())
    SelectionSortSobrenome(contatos)
    print("Vetor Ordenado")
    for k in range(numero_contatos):
        print(contatos[k].getRegistro())