def busqueda_binaria(lista, elemento):
    izquierda = 0 
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if lista[medio] == elemento:
            return medio
        elif lista[medio] > elemento:
            derecha = medio - 1
        else:
            izquierda = medio + 1

    return -1

lista_ordenada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elemento_buscado = 3

resultado = busqueda_binaria(lista_ordenada, elemento_buscado)

if resultado != -1:
    print(f"El elemento {elemento_buscado} se encuentra en la posición {resultado}.")
else:
    print(f"El elemento {elemento_buscado} no está en la lista.")
