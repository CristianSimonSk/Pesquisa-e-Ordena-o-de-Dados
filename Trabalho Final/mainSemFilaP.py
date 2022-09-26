def geradorArqInput(num_elements: int, output: str, name: str = 'input', minNum: int = 0, maxNum: int = 100):
    import random 

    filePath = f"{output}{name}.txt"
    arquivo = open(filePath, 'w')
    for x in range(num_elements):
        i = random.randint(minNum,maxNum)
        arquivo.write(str(10-x) + "\n")
    arquivo.close()

p=0
qtdGerar = 10
qtdTMP = 3
tamanhoTMP = int(qtdGerar/qtdTMP)

def ordenaExtSelect(input_path: str):
    arquivo = open(input_path, 'r')
    x = []
    y = []
    buffer_size = 4
    fileP=0
    filePath=0

    for n in range(3):
        x.append(str(arquivo.readline()))
        aux3 = x[n]
        y.append(int(aux3))

    for n in range(qtdGerar):
        print(x)
        if n == 0:
            fileP = "Temp/arqTMP1.txt"
            filePath = open(fileP, 'w')

        if n == buffer_size:
            filePath.close()
            fileP = "Temp/arqTMP2.txt"
            filePath = open(fileP, 'w')

        if n == buffer_size*2:
            filePath.close()
            fileP = "Temp/arqTMP3.txt"
            filePath = open(fileP, 'w')

        if y[0] != None:
            menorInt = y[0]
            menor = x[0]
        
        elif y[1] != None:
            menorInt = y[1]
            menor = x[1]

        elif y[2] != None:
            menorInt = y[2]
            menor = x[2]


        if y[1] != None:
            if y[1] <= menorInt:
                menorInt = y[1] 
                menor = x[1] 

        if y[2] != None:
            if y[2] <= menorInt:
                menorInt = y[2]
                menor = x[2] 
            
        if n < (10): 
            aux2 = []
            filePath.write(str(menor))   
            if x[0] == menor:
                x[0] = arquivo.readline() 
                aux2 = x[0]
                if aux2 == '':
                    y[0] = None
                else:
                    y[0] = int(aux2)  
            
            elif x[1] == menor:
                x[1] = arquivo.readline() 
                aux2 = x[1]
                if aux2 == '':
                    y[1] = None
                else:
                    y[1] = int(aux2) 
            
            elif x[2] == menor:
                x[2] = arquivo.readline() 
                aux2 = x[2]
                if aux2 == '':
                    y[2] = None
                else:
                    y[2] = int(aux2) 
                        
        else :
            print(n)
            aux=[]
            for n in range(3):
                if x[n] != '':
                    aux.append(x[n])

            if aux[1]< aux[0]:
                filePath.write(str(aux[1])) 
                filePath.write(str(aux[0])) 

            else:
                filePath.write(str(aux[0])) 
                filePath.write(str(aux[1]))
            aux.clear()
                
     
    arquivo = open('Arquivos/input.txt', 'w')
    filePath.close()
    filePath = open('Temp/arqTMP1.txt', 'r')
    for n in range(buffer_size):
        arquivo.write(str(filePath.readline()))
    filePath.close()    
    filePath = open('Temp/arqTMP2.txt', 'r')
    for n in range(buffer_size):
        arquivo.write(str(filePath.readline()))
    filePath.close()
    filePath = open('Temp/arqTMP3.txt', 'r')
    for n in range(buffer_size):
        arquivo.write(str(filePath.readline()))
    filePath.close()
    arquivo.close()
    x.clear()
    y.clear()
    

x = 'Arquivos/'
y = 'input'

x1 = 'Arquivos/input.txt'
y1 = 'Temp/arqTMP1.txt'

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
                geradorArqInput(qtdGerar, x, y, 0, 10) 
            
            case 2:
                ordenaExtSelect(x1)

            case 3:
                op = 0
              
main()