def busqueda_binaria(lista,objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio -1
    return -1

ls = [1,1,2,3,4,4,4,5]
print(busqueda_binaria(ls,4))