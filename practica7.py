
def suma_total(s:list[int]) -> int:
    acum: int = 0
    i: int = 0
    while i < len (s):
        acum += s[i]
        i += 1
    return acum

print(suma_total ([1,2,3]))

def pertenece(s: list [int], e: int) -> bool:
    i:int = 0
    while i < len (s) and s[i] != e:
        i+= 1
    return (i < len (s))

def nopertenece(s: list [int], e: int) -> bool:
    i:int = 0
    while i < len (s) and s[i] != e:
        i=+1
    return i == len (s)

def divide_a_todos(s:list[int], e:int) -> bool:
    i:int = 0
    while i < len (s) and (s[i] % e) == 0:
            i += 1
    return (i == len (s))

def ordenados(s: list[int]) -> bool:
     i:int = 0
     while i<(len(s)-1) and s[i] < s[i+1]:
          i += 1
     return (i == (len (s)-1))

def lista_palabras(s: list[str])-> bool:
     i:int = 0
     while i<len (s) and len (s[i]) != 7:
          i += 1
     return (i < len (s))

def palindromo(s: str) -> bool:
     i:int = 0
     m:int = len (s)-1
     if (len(s) % 2) == 0:
        while i<(len (s)/2) and s[i] == s[m]:
            i += 1
            m -= 1
        return (i == (len(s)/2))
     else:
          while i<((len (s)-1)/2) and s[i] == s[m]:
            i += 1
            m -= 1
          return (i == ((len(s)-1)/2))
     
def condicion(c:str) -> bool:
    i: int = 0
    condicion1: bool = False
    condicion2: bool = False
    condicion3: bool = False
    while i < len(c):
        if (c[i] <= 'z') and (c[i] >= 'a'):
            condicion1 = True
        if(c[i] <= 'Z') and (c[i] >= 'A'):
            condicion2 = True
        if (c[i] <= '9') and (c[i] >= '0'):
            condicion3 = True
        i += 1
    return (condicion3 and condicion2 and condicion1)
 
def contraseña(c:str) -> str:
    if len(c) > 8 and condicion(c):
        print ("VERDE")
    elif len(c) < 5:
        print ("ROJA")
    else:
        print ("AMARILLO")

contraseña("Cl4ve123E")
contraseña("Cl4")
contraseña("Cdfdfsdfsdfs")

def banco(b: list[(str, int)]) -> int:
    i:int = 0
    saldo: int = 0
    while i < len (b):
        if b[i][0] == 'I':
            saldo += b[i][1] 
        if b[i][0]  == 'R':
            saldo -= b[i][1] 
        i += 1
    return saldo

print (banco ([("I",2000), ("R", 20),("R", 1000),("I", 300)]))

    

def tres_vocales_distintas(p:str) -> bool:
    i:int = 0
    e:int = 0
    vocales:list = ['a','e', 'i','o','u', 'A', 'E', 'I', 'O', 'U']
    while i < len(p):
        if p[i] in vocales:
            vocales.remove (p[i])
            e += 1
        i += 1
    if e >= 3:
        return True
    else:
        return False        


print (tres_vocales_distintas("aeoj"))
print (tres_vocales_distintas("aej"))
print (tres_vocales_distintas("aeaj"))

#parte2
#2.1
def posic_pares0 (s:list[int], res:list[int]):
    i:int= 0
    res.clear()
    while i < len(s):
        if (s[i]%2)== 0:
            res.insert(i,0)
        else:
            res.insert(i,s[i])
        i += 1
    return res

print (posic_pares0([1,2,3,4,6,7,8,10],[1,2]))

#2.2
def posic_pares01 (s:list[int]) -> list[int]:
    i:int= 0
    res:list=[]
    while i < len(s):
        if (s[i]%2)== 0:
            res.insert(i,0)
        else:
            res.insert(i,s[i])
        i += 1
    return res

print (posic_pares01([1,2,3,4,6,7,8,10]))

#2.3
def sin_vocales(s:list[str]) -> list[str]:
    vocales:list = ['a','e', 'i','o','u', 'A', 'E', 'I', 'O', 'U']
    for letra in s:
        if pertenece(vocales,letra):
            s.remove(letra)
    return s

print (sin_vocales(['a','b','c','e']))
 #2.4
def reemplazar_vocales(s:list[str]) -> list[str]:
    i:int = 0
    vocales:list = ['a','e', 'i','o','u', 'A', 'E', 'I', 'O', 'U']
    for letra in s:
        if pertenece(vocales,letra):
            s.remove(letra)
            s.insert(i,'_')
        i += 1
    return s

print (reemplazar_vocales(['a','b','c','e']))

#2.5
def da_vuelta_str(s:list[str]) -> list[str]:
    i:int= 0
    l:int = len(s)
    for i in range (0,l,1):
        s.insert(i,s[l-1])
        del s[l]
    return s

print(da_vuelta_str(['a','b','c']))

#2.6
def eliminar_repetidos(s:list[str]) -> list[str]:
    l:list = []
    for letra in s:
        if pertenece(l,letra):
            l = l
        else:
            l.append(letra)
    return l

print(eliminar_repetidos(['a','b','a','c','a','c','f']))

#3
def todas_mayores(s:list[int]) -> bool:
    i:int= 0
     value:bool = True
    for i in range(0, len (s), 1):
        if s[i] < 4:
            value = False
    return value

def promedio(s:list[int]) -> int:
    i: int= 0
    p: int = 0
    for i in range(0, len (s), 1):
        p += s[i]
    m: int = p/len(s)
    return m

def aprobado(s:list[int])-> int:
    i:int = 0
    if todas_mayores(s):
        if promedio (s) >= 7:
            return 1
        elif promedio (s) > 4:
            return 2
        else:
             return 3
    else:
        return 3
    
print (aprobado([5,7,4]))
    
#4


    
            


#5.2
def pertenece_a_cada_uno2(s: list[list[int]], e:int,res: list [bool]) -> None:
    i:int = 0
    res.clear()
    for i in range (0, len(s), 1):
        if pertenece(s[i],e):
            res.append(True)
        else:
            res.append(False)
        i += 1

lista_ejemplo = [True]
print ("antes: " + str(lista_ejemplo))
pertenece_a_cada_uno2 ([[]],2, lista_ejemplo)
print ("despues: " + str(lista_ejemplo))

#5.3
def es_matriz(s: list[list[int]]) -> bool:
    i:int= 0
    value:bool= True
    for i in range (0,len(s),1):
        if len (s[i]) != len (s[0]):
            value = False
    return value
#5.4
def filas_ordenadas(s: list[list[int]], e:int,res: list [bool]) -> None:
    i:int = 0
    res:list[bool]= []
    for i in range (0,len(s),1):
        if ordenados(s[i]):
            res.append (True)
        else: 
            res.append (False)
    return res









