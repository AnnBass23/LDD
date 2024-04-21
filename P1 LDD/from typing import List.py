from typing import List

def indiceMaximo (l: list) -> int:
    i: int = 0
    res = 0
    while (i < len (l)-1):
        if l[i+1] < l[i]:
            res = i
        else:
            res = i+1
        i += 1
    
    return res

lista = [15.5,-18,4.125,15.5,-1]
print (indiceMaximo(lista))