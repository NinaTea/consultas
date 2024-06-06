import math
def imprimir_hola_mundo ():
    print ('Hola mundo')
    
imprimir_hola_mundo()

def perimetro () -> float :
    #return 2 * 3.14159265358979323
    return 2 * math.pi

a : float = perimetro ()
print (a)

def es_multiplo_de (n:int, m:int) -> bool:
    return (n % m) == 0



#3
def raizDe2 () -> float :
    return round ((math.sqrt(2)), 4)

print (raizDe2())

#2.1
def imprimir_saludo(nombre= str) -> str:
    print ("Hola " + str(nombre))

print (imprimir_saludo ("Juli"))

#2.2
def raiz_cuadrada_de(numero = int) -> float:
     return (math.sqrt (numero))

print (raiz_cuadrada_de (36))

#2.3
def fahrenheit_a_celsius(tf = float) -> float:
    return (((tf - 32) * 5)/9)

print (fahrenheit_a_celsius (30))

#2.4
def imprimir_dos_veces() -> str:
    print ((" Here comes the sun  \n Here comes the sun, and I say  \n It's alright \n")*2)

imprimir_dos_veces()

#2.5
def es_multiplo_de(a = int, b = int) -> bool:
    while ((a%b) == 0):
        return True
    return False

print (es_multiplo_de (8,6))
print (es_multiplo_de (4,2))

def es_multiplo_de1(c = int, d = int) -> bool:
    return ((c%d) == 0)
      
print (es_multiplo_de1 (8,6))
print (es_multiplo_de1 (4,2))

#2.6
def es_par(n= int) -> bool:
    return es_multiplo_de1(n,2)

print (es_par(4))
print (es_par (9))

#2.7
def min_cant_de_porciones ():
    p :int = 6
    return p

def cantidad_de_pizzas (c = int, p = int) ->int:
        i: int= c * p
        if (i%8) == 0:
            return i/8
        else:
            return int(i/8) + 1

#min_cant_de_porciones(9)
print (cantidad_de_pizzas (30,6))

#3.1
def alguno_es_0 (a = int, b = int) -> bool:
    return (a == 0) or (b == 0)

print (alguno_es_0 (8,0))
print (alguno_es_0(8,5))

#3.3
def es_nombre_largo (nombre :str) -> bool:
    return (3 <= len (nombre)) and (8 >= len (nombre)) 

#4
def peso_pino (altura_metros:int) -> int:
    i:int = altura_metros
    peso_kg: int = 0
    while i > 3:
        i -= 1
        peso_kg += 200
    for i in range (3, 0, -1):
        peso_kg += 300
    return peso_kg

print (peso_pino (8))
print (peso_pino (2))
print (peso_pino (5))

def es_peso_util (peso_pino) -> bool:
    return (peso_pino > 400) and (peso_pino < 1000)

print (es_peso_util(peso_pino(8)))
print (es_peso_util(peso_pino(5)))
print (es_peso_util(peso_pino(2)))


def sirve_pino(altura_pino: int) -> bool:
    return (es_peso_util(peso_pino(altura_pino)))

print (sirve_pino(8))
print (sirve_pino(5))
print (sirve_pino(2))

#5.1
def devolver_el_doble_si_es_par(n:int) -> int:
    if (n % 2) == 0:
       return  2*n 
    else: 
        return n
    
#5.2
def devolver_valor_si_es_par_sino_el_que_sigue(n: int) -> int:
    if (n%2) == 0:
        return n
    else:
        return n + 1
    
print (devolver_valor_si_es_par_sino_el_que_sigue(3))
print (devolver_valor_si_es_par_sino_el_que_sigue(4))

#5.3
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(n: int) -> int:
    if es_multiplo_de(n,9):
        return n * 3
    if es_multiplo_de(n,3):
        return n * 2
    else:
        return n
    
    
print (devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(18))
print (devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(2))
print (devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(6))


    
def jubilacion(sexo: str, edad: int) -> str:
    if sexo == "F":
        if edad < 60 and edad > 18:
            print ("Te toca trabajar")
        else :
            print ("Andá de vacaciones")
    else:
        if edad < 65 and edad > 18:
            print ("Te toca trabajar")
        else :
            print ("Andá de vacaciones")
        

jubilacion("F", 36)
jubilacion("M", 63)
jubilacion("F", 6)
jubilacion("F", 63)
jubilacion("M", 36)
jubilacion("M", 70)
jubilacion("M", 6)

#6

def numeros_pares ():
    n : int = 10
    while n <= 40 :
        if (n % 2) == 0:
            print (n)
        n = n + 1 
        
#numeros_pares()
def ej61 ():
    for i in range (10, 40+1, 2):
        print (i)

ej61()

def ej6():
    i: int = 10
    while i <= 40:
        print (i)
        i += 2

#ej6()
    
def despegue (i:int):
    while i > 0:
        print (i)
        i = i -1
    print ("Despegue")

def despegue1 (i:int):
    for i in range (i,0,-1):
        print(i)
    print ("Despegue")

#6.5
def viaje_en_el_tiempo(año_partida: int, año_llegada: int)-> str:
    i:int = año_partida
    while i > año_llegada:
        print ("Viajó un año al pasado, estamos en el año: " + str (i))
        i -=1
    
viaje_en_el_tiempo(2024,2015)

#6.6
def viaje_a_Aristoteles (año_partida: int, año_llegada: int)-> str:
    i:int = año_partida
    for i in range (año_partida, año_llegada, -20):
        print ("Viajó un año al pasado, estamos en el año: " + str (i))
    
print ("ej 6.6")
viaje_a_Aristoteles (2024, 1800)



