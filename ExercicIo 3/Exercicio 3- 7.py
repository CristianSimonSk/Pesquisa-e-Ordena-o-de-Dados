#7. Para um vetor de 10 elementos desordenados, faça o teste de mesa, aplicado cada um dos algoritmos de ordenação estudados (Insertion, Bubble, Selection). Demonstre, de forma detalhada como ficam os elementos do vetor em cada iteração do algoritmo.
def imprime(v):
    for n in v:
        print(n)

def insertionSort(a):
    v=a
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

def bubbleSort(a):
    v=a
    k=1
    for i in range(len(v)-1,0,-1):
        for j in range(i):
            if v[j]>v[j+1]:
                temp = v[j]
                v[j] = v[j+1]
                v[j+1] = temp
            print('Execução ',k)
            k+=1
            imprime(v)    

def selectionSort(a):
    v=a
    k=1
    for i in range(len(v)-1,0,-1):
        maior_idx=0
        for j in range(1,i+1):
            if v[j]>v[maior_idx]:
                maior_idx = j
                temp = v[i]
                v[i] = v[maior_idx]
                v[maior_idx] = temp
        print('Execução ',k)
        k+=1
        imprime(v)


v = [2, 12, 69, 77, 93, 10, 131, 1, 76, 11]
print('ORDENANDO POR INSERTION')
insertionSort(v)
print('ORDENANDO POR BUBBLE')
bubbleSort(v)
print('ORDENANDO POR SELECTION')
selectionSort(v)