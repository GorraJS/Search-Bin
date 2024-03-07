def busqueda_binaria(lista, elemento):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        valor_medio = lista[medio]

        if valor_medio == elemento:
            return medio  # Elemento encontrado, devuelve el índice
        elif valor_medio < elemento:
            inicio = medio + 1  # Busca en la mitad derecha
        else:
            fin = medio - 1  # Busca en la mitad izquierda

    return -1  # El elemento no está en la lista

# Ejemplo de uso:
lista_ordenada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elemento_buscado = 7

resultado = busqueda_binaria(lista_ordenada, elemento_buscado)

if resultado != -1:
    print(f"El elemento {elemento_buscado} está en la posición {resultado}.")
else:
    print(f"El elemento {elemento_buscado} no está en la lista.")
