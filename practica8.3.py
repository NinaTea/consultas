def contar_lineas() -> int:
    i: int = 0
    f = open('ejemplo.txt', 'r')
    while f.readline() != '':
        i += 1
    f.close()
    return i

print(contar_lineas())

def existe_palabra(palabra: str) -> bool:
    archivo = open('ejemplo.txt', 'r')
    lineas = archivo.readlines()
    for linea in lineas:
        if palabra in linea:
              return True
    archivo.close()
    return False

print(existe_palabra("ejemplo"))  

def cantidad_apariciones(palabra:str) -> int:
    archivo = open('ejemplo.txt', 'r')
    lineas = archivo.readlines()
    i: int = 0
    for linea in lineas:
        if palabra in linea:
            i += linea.count(palabra)
    archivo.close()
    return i

print(cantidad_apariciones("ejemplo"))


#2
def clonar_sin_comentarios():
    archivo_entrada = open("comentarios.txt", "r")
    lineas = archivo_entrada.readlines()
    lineas_sin_comentarios = [] 
    for linea in lineas:
        i = 0
        while i < len(linea) and linea[i] == ' ':
                i += 1
        if i < len(linea) and linea[i] != '#':
                        lineas_sin_comentarios.append(linea)
    archivo_entrada.close()
    archivo_salida = open("sin_comentarios.txt", "w")
    archivo_salida.writelines(lineas_sin_comentarios)
    
clonar_sin_comentarios()

def invertir_lineas():
      archivo_entrada = open("ejemplo.txt", "r")
      lineas = archivo_entrada.readlines()
      archivo_salida = open("reverso.txt", "w")
      i:int = (len(lineas)-1)
      archivo_entrada.close()
      for i in range ((len(lineas)-1),-1,-1):
            archivo_salida.write(lineas[i])

#invertir_lineas()

def agregar_frase_al_final(frase: str):
    archivo = open("ejemplo.txt", "r+")
    lineas = archivo.readlines()
    archivo.write('\n')
    archivo.write(frase)
    archivo.close()

agregar_frase_al_final("hola como estas")

def agregar_frase_al_principio(frase: str):
    archivo = open("ejemplo.txt", "r+")
    lineas = archivo.readlines()
    archivo.seek(0,0)
    archivo.write(frase)
    archivo.write('\n')
    for linea in lineas:
         archivo.write(linea)
    archivo.close()

agregar_frase_al_principio("hola como estas")

#def listar_palabras_de_archivo() -> list:

def promedio_estudiante(lista:list[(str,float)]):
     i: int = 0
     j:int = 0
     h:int = 0
     tuplas_finales:list(str,float)= []
     while i > len(lista):
          promedios = lista[h][1]
          if lista[h][0] == lista [i+1][0]:
               promedios += lista[i+1][1]
               #tuplas_finales.append(lista[0][0],promedios)
               j += 1



def calcular_promedio_por_estudiante():
     archivo_notas= open('archivo_notas.csv', 'r')
     archivo_promedios = open ('archivos_promedios.csv', 'w')
     lineas = archivo_notas.readlines()
     listas:list = []
     for linea in lineas:
        i:int = 0
        temp = ""
        while i < len(linea):
            if linea[i] != ',':
                temp += linea[i]
            else:
                listas.append(temp)
                temp = ""
            i += 1
     listas_lu_notas:list = []
     j:int = 0
     while j < len(listas)-3:
        listas_lu_notas.append((listas[j],listas[j+3])) 
        j += 4
     promedio_estudiante(listas_lu_notas)





print("camridad", calcular_promedio_por_estudiante())
#PILAS
from queue import LifoQueue as Pila
import random
def generar_nros_al_azar(cantidad:int, desde:int, hasta:int) -> Pila[int]:
     i:int = cantidad
     pila = Pila()
     while i > 0:
        numero = random.randint(desde,hasta)
        pila.put(numero)
        i -= 1
     return pila

def imprimir_elementos(p:Pila[int]) -> None:
     print:("Mostrando elementos ...")
     while not p.empty():
          print(p.get, end = " ")

print (generar_nros_al_azar(5,0,10))
pila_numeros = generar_nros_al_azar(5,0,10)
while not pila_numeros.empty():
   print(pila_numeros.get())

def cantidad_elementos(p: Pila) -> int:
     contenido:list= []
     while not p.empty():
          contenido.append(p.get())
     i:int= len(contenido)
     for i in range((len(contenido))-1,-1,-1):
          p.put(contenido[i])
     return len(contenido)

p=Pila()
p.put(1)
p.put(2)
p.put(3)
print(cantidad_elementos(p))
#Esto para chequear que la pila sigue igual que al principio
#while not p.empty():
#   print(p.get())

def buscar_el_maximo(p:Pila) -> int:
     contenido:list= []
     while not p.empty():
          contenido.append(p.get())
     i:int= len(contenido)
     for i in range((len(contenido))-1,-1,-1):
          p.put(contenido[i])
     h:int = 0
     k:int = 1
     while h < len(contenido) and k < len(contenido):
          if contenido[h] > contenido[k]:
               k += 1
          else:
               h += 1
     if k > h:
          return contenido[h]
     else:
          return contenido[k]
               
p=Pila()
p.put(1)
p.put(2)
p.put(3)
print(buscar_el_maximo(p))
#Esto para chequear que la pila sigue igual que al principio
while not p.empty():
    print(p.get())

"""def esta_bien_balanceada(s:str) -> bool:
    i: int= 0
    while i < len(s):
         if s[i] == ')':
              if i == 0:
                final_value = False
              elif s[i-1] != 
    
         elif s[i] == '(':
         
         else:
            i += 1"""
#COLAS

from queue import Queue as Cola
import random
def generar_nros_al_azar_cola(cantidad:int, desde:int, hasta:int) -> Cola[int]:
     i:int = cantidad
     cola = Cola()
     while i > 0:
        numero = random.randint(desde,hasta)
        cola.put(numero)
        i -= 1
     return cola

print (generar_nros_al_azar_cola(5,0,10))
cola_numeros = generar_nros_al_azar_cola(5,0,10)
while not cola_numeros.empty():
    print(cola_numeros.get())

def cantidad_elementos(c: Cola) -> int:
     contenido:list= []
     while not c.empty():
          contenido.append(c.get())
     i:int= len(contenido)
     for i in range((len(contenido))-1,-1,-1):
          c.put(contenido[i])
     return len(contenido)

c=Cola()
c.put(1)
c.put(2)
c.put(3)
print(cantidad_elementos(c))
#Esto para chequear que la cola sigue igual que al principio
#while not c.empty():
#   print(c.get())

def buscar_el_maximo(c:Cola) -> int:
     contenido:list= []
     while not c.empty():
          contenido.append(c.get())
     i:int= len(contenido)
     for i in range((len(contenido))-1,-1,-1):
          p.put(contenido[i])
     h:int = 0
     k:int = 1
     while h < len(contenido) and k < len(contenido):
          if contenido[h] > contenido[k]:
               k += 1
          else:
               h += 1
     if k > h:
          return contenido[h]
     else:
          return contenido[k]
               
c=Cola()
c.put(1)
c.put(2)
c.put(3)
print(buscar_el_maximo(c))
#Esto para chequear que la cola sigue igual que al principio
while not c.empty():
    print(c.get())

def armar_secuencia_de_bingo() -> Cola:
     #como hago para que no se repitan los numeros puedo usar random.shuffle con una lista
     c= Cola()
     bolillas: list = []
     for bolilla in range (100):
          bolillas.append(bolilla)
     random.shuffle(bolillas)
     i:int = 0
     while i < len(bolillas):
          c.put(bolillas[i])
          i += 1
     return c

#print(armar_secuencia_de_bingo())




def jugar_carton_de_bingo(carton:list[int], bolillero:Cola) -> int:
     contador:int = 0
     bolillas: list = []
     while not bolillero.empty():
           bolillas.append(bolillero.get())
     i:int = 0
     while i < len(carton):
            if bolillas[contador] in carton:
                  i += 1
            contador += 1
     return contador

print("cantidad bingo",jugar_carton_de_bingo([1,20,21,50,71,22,41,28,9,77,51,91],armar_secuencia_de_bingo()))
     
def n_pacientes_urgentes(c:Cola) -> int:
     lista:list =[]
     while not c.empty():
          lista.append(c.get())
     i:int = 0
     urgentes:int = [1,2,3]
     contador: int = 0
     while i < len(lista):
          if lista[i][0] in urgentes:
               contador += 1
          i += 1
     return contador

cola=Cola()
cola.put((1,'Jorge','ahi anda'))
cola.put((1,'Maria','esta jodida'))
cola.put((5,'Alejandro','blabla'))
cola.put((4,'Martin','Anda bien dentro de todo'))
cola.put((3,'Martin','Anda bien dentro de todo'))
print(n_pacientes_urgentes(cola))  

#DICCIONARIOS
def lista_de_palabras(lineas:str) -> list[str]:
     lista:list = []
     for linea in lineas:
          temp:str= ""
          i:int = 0
          while i < len(linea):
               if linea[i] != " ":
                    temp += linea[i]
               else:
                    temp = ""
               i += 1
     return lista


def agrupar_por_longitud() -> dict[int,int]:
     archivo = open('ejemplo', 'r')
     lineas = archivo.readlines()
     dic: dict= dic()
     palabras:list[str] = lista_de_palabras(lineas)
     for palabra in palabras:
          if len(palabra) in dic:
               dic[len(palabra)] += 1
          else:
               dic[len(palabra)] = 1 
     return dic



     
     
     
            

        



    
