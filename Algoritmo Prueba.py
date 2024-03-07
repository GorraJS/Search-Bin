
def SearchBin(lista,valor):
    left = 0
    right = len(lista)-1#11
    pasos = 0
    
    while left <= right:
        pasos += 1
        half = (left+right)/2

        if lista[half] == valor:
            return "Se encontro a {} pasos en la posicion {}".format(pasos,half)
        
        elif lista[half] > valor:
            right = half-1
        
        elif lista[half] < valor:
            left = half+1
    return "no esta"

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] 
posicion = SearchBin(lista,20)
print(posicion)