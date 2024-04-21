import numpy as np

s = [1, 2, 3.0, "hola", 7 + 3]

#print (s[0])
#print (s[1])
#print (s[-1])

v = np.array([1,2,3])
w = np.array([1.2, 7, np.pi])
v, w, v + w

#print (v)
#print (w)
#print (v + w)

np.set_printoptions(precision=2, suppress=True)
v = np.array([1,2,np.e,7])
w = np.array([1.2, np.pi, 4, 5])
#for expr in ["v", "w", "v + w", "v ** 2", "v % 2", "np.sum(v)", "np.sqrt(w)", "v > 3", "w < 3.5"]:
    
#print(f"{expr:11s} == {eval(expr)}")
    
a = np.array ([False, True, False, False, True])

#print (~a)

v = np.array([1,2,np.e,7])
w = np.array([1.2, np.pi, 4, 5])
z = np.array([0,1])
#print (v * w)
#print (v+2)
#print (v+z) #No funciona porque el shape de z y de v no es el mismo 

v = np.array([1, 2, np.e, 7, 5])

#for expr in ["v[0]", "v[1]", "v[-1]", "v[[0, 3]]", "v[0:3]", "v[0:1]"]:
    #print (f"{expr:11s} == {eval(expr)}")
    #print (v[-2])

v = np.array([1, 2, np.e, 7, 5])
w = np.array([1, 0, 2, 5, 0])
#print (v[v > 2])
#print (v[w != 0])

A = np.array([[3, 2, 2], [-1, 0, 1], [-2, 2, 4]])
B = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
C = np.array([[0, 1,-1], [5,-2, 1]])
#print (A + B)
#print (A * B)
#print (C**2) 

a = np.sqrt(2)
a
#np.round(a)
#np.round(a, 2)
#np.info(np.round)
#np.info(np.ceil)

v = np.array([a, a**2, a**3, a**(.5)])
#print (np.floor(v))
#np.info(np.mean)

s = np.array ([3,4])
a = s**2
#print (np.sqrt(a[0]+a[1]))
t = np.array ([3,4])
a = (s - t)**2
#print (np.sqrt (a[0]+a[1]))

#l = [1]
#print (l[-1])

def indiceMaximo (l: np.array) -> int:
    i: int = 0
    while (i < len (l)):
        if l[i] > l[i+1]:
            res = i
        else:
            res = i+1
        i += 1
    
    return res



lista = np.array([15.5,-18,4.215,15.5,-1])
print (indiceMaximo(lista))
