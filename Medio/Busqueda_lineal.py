def busqueda_lineal(lista,objetivo):
    for i,elem in enumerate(lista):
        if elem == objetivo:
            return 1
        
    return -1

ls = [5,4,4,3,4,1,2,1]
print(busqueda_lineal(ls,9))