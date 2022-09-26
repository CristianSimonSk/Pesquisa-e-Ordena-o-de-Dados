def geradorArqInput(num_elements: int, output: str, minNum: int = 0, maxNum: int = 100):
    import random 

    arquivo = open(output, 'w')
    for x in range(num_elements):
        i = random.randint(minNum,maxNum)
        arquivo.write(str(10-x) + "\n")
    arquivo.close()


def criaPrioridadesEOrdena(arquivo: str, numTMP: int):
    fileP = f"Temp/arqTMP{str(numTMP+1)}.txt"
    priorid = []
    x = []
    filePath = open(fileP, 'w')
    
    for n in range(bufferSize):
        x.append(arquivo.readline())

    for n in range(bufferSize):
        aux = x[n]
        if aux == '':
            priorid.append(set())
        else:
            priorid.append(int(aux))

    a = priorid[0]
    b = priorid[1]
    c = priorid[2]
    aux2 = 3
    menor = 100000

    for n in range(bufferSize):
        if a is int:
            menor = a
        
        elif b is int:
            menor = b

        else:
            menor = c

        if b is int and b <= menor:
            menor = b

        if c is int and c <= menor:
            menor = c
        print(menor)
        if a is int:
            if a == menor:
                filePath.write(str(menor)+{'\n'})
                a = priorid[aux2] 
                aux2 += 1
                
        elif b is int:
            if b == menor:
                filePath.write(str(menor))
                b = priorid[aux2] 
                aux2 += 1
                
        else:
            if c == menor:
                filePath.write(str(menor))
                c = priorid[aux2] 
                aux2 += 1
                
    x.clear()
    priorid.clear()
    filePath.close()



def ordenaExtSelect(input_path: str):
    arquivo = open(input_path, 'r')

    for n in range(qtdBuffers):
        numTMP= n
        criaPrioridadesEOrdena(arquivo, numTMP)   
    
    arquivo.close()

    arquivo = open(input_path, 'w')

    for m in range(qtdBuffers):
        fileP2 = f"Temp/arqTMP{str(m+1)}.txt"
        filePath = open(fileP2, 'r')

        for n in range(bufferSize):
            arquivo.write(str(filePath.readline()))
        filePath.close()

    arquivo.close()
        
    
qtdGerar = 10   
bufferSize = 4
qtdBuffers = 3
dirP = 'Arquivos/input.txt'


def main():
    print("===========================================\n")
    print("Iniciando programa Main...")
    print("\n===========================================")
    op = 1
    """logF = int(0.30103 * 4) + 1
    for p in range(logF):"""
    while(op != 0):
        op2 = int(input("\n\nInsira o numero que voce deseja executar \n\n1 - Gerar novo arquivo aleatório \n\n2 - Executar Ordenação Externa (caso queira ir até o arquivo ficar ordenado terá que executar varias vezes)\n\n0 - Sair\n\n"))
        print("\n")
        match(op2):
            case 1:
                geradorArqInput(qtdGerar, dirP, 0, 10) 
            
            case 2:
                ordenaExtSelect(dirP)

            case 3:
                op = 0

              
main()