def imprime(v):
    for n in v:
        print(n)

def bubbleSort(v):
    k=1
    for i in range(len(v)-1,0,-1):
        for j in range(i):
            if v[j]<v[j+1]:
                temp = v[j]
                v[j] = v[j+1]
                v[j+1] = temp
            print('Execução ',k)
            imprime(v)
            k+=1    

v = [71, 5, 14, 82]
bubbleSort(v)



