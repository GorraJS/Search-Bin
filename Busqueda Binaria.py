arr = []
print("Defina largo del Arreglo")
ArrLong = input()

for i in range(int(ArrLong)):
    print("Defina Elemento(Int):")
    Num = input()
    Num = int(Num)
    arr.append(Num)
    print("Array = ", arr)

print("Defina N:") 
n = input()
n = int(n)

def swap(arr,x,j):
    aux = arr[x]
    arr[x] = arr[j]
    arr[j] = aux
    return

def Sort(arr):
    for x in range(0,len(arr),1):
        min = x
        for j in range(x+1,len(arr),1):
            if arr[j] < arr[min]:
                min = j
            swap(arr,x,min)
    return arr

def SearchBin(arr, n):
    izquierda = 0 
    derecha = len(arr) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if arr[medio] == n:
            return medio
        elif arr[medio] > n:
            derecha = medio - 1
        else:
            izquierda = medio + 1
    return -1

resultado = SearchBin(arr, n)

def respuesta(resultado):
    if resultado != -1:
        return print(f"El arreglo es {Sort(arr)} y el elemento {n} si está dentro del arreglo.")
    else:
        return print(f"El arreglo es {Sort(arr)} y el elemento {n} no está en el arreglo.")

print(respuesta(resultado))