#Basico

#imprimir
print("hello world!")

#variables
x = 7
y = 2.5
z = "hi"
a =True

#if 
if x > 7:
    print("x es más grande que 7")
else:
    print("x es menos o igual que 7")

#ciclo for y while
for i in range(5):
    print(i)

i = 0
while i < 5:
    print(i)
    i += 1

#funciones
def multiply(a,b):
    return a*b
#funcion recursiva
def multiply_recursive(a,b):
    if b==0:
        return 0
    return a * multiply_recursive(a,b-1)

#programacion orientado a objetos
class YoutubeVideo:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def play(self):
        return self.title + " se esta reproduciendo"

#estructura de datos
#organizar informacion

#arrays (listas en python)
my_list = [7,5.0,"hi",True]

#Linked List
class LinkedList:
    def __init__(self,value,next =None):
        self.value = value
        self.next = next

#arbol de busqueda binario
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

#hash table (diccionario en python)
my_dict = {"super":1,"idol":2,"smile":3}

#algoritmos

#Big-O notation: O(1) TO O(n!)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx],arr[i]
    return arr
