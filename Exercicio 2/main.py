def imprime(numeros):
    for k in range(qtdGerar):
        print(numeros[k])

def InsertionSort(v):
    k=1
    for i in range(1, len(v)):
        key = v[i]
        j = i - 1
        while j >= 0 and v[j] > key:
            v[j + 1] = v[j]
            j -= 1
            v[j + 1] = key
        print('Execução ',k)
        k+=1
        imprime(v)    

def SelectionSort(numeros):
    k=1
    for i in range(len(numeros)-1,0,-1):
        maior_idx=0
        for j in range(1,i+1):
            if numeros[j]>numeros[maior_idx]:
                maior_idx = j
        temp = numeros[i]
        numeros[i] = numeros[maior_idx]
        numeros[maior_idx] = temp
        print('Execução',k)
        k+=1    
        imprime(numeros)    

def BubbleSort(v):
    k=1
    for i in range(len(v)-1,0,-1):
        for j in range(i):
            if v[j]>v[j+1]:
                temp = v[j]
                v[j] = v[j+1]
                v[j+1] = temp
            print('Execução',k)
            k+=1
            imprime(v)     

qtdGerar = 10
numeros = [20,25,2,88,66,10,3,8,6,9]
print("INSERTION SORT")
print("Vetor Original")
imprime(numeros)
print("Vetor Ordenado")
InsertionSort(numeros) 

numeros = [20,25,2,88,66,10,3,8,6,9]
print("BUBBLE SORT")
print("Vetor Original")
imprime(numeros)
print("Vetor Ordenado")
BubbleSort(numeros)

numeros = [20,25,2,88,66,10,3,8,6,9]
print("SELECTION SORT")
print("Vetor Original")
imprime(numeros)
print("Vetor Ordenado")
SelectionSort(numeros)

