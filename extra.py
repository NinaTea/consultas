from queue import LifoQueue as Pila
from queue import Queue as Cola
import random

# def generar_nros_al_azar(cantidad:int, desde:int, hasta:int) -> Pila:
#      i:int = cantidad
#      pila = Pila()
#      while i > 0:
#         numero = random.randint(desde,hasta)
#         pila.put(numero)
#         i -= 1
#      return pila

# pila_numeros = generar_nros_al_azar(5,0,10)

# def imprimir_elementos(p:Pila) -> None:
#      print("Mostrando elementos ...")
#      while not p.empty():
#         print(p.get(), end= " ")
#      print ('\n')

# imprimir_elementos(pila_numeros)

# def sacar_espacios_blancos(e: str) -> str:
#      temp: str = ""
#      for caracteres in e:
#           if caracteres != ' ':
#                temp += caracteres
#      print(temp)
#      return temp

# def chequeo_misma_cantidad_parentesis(s: str) -> bool:
#      pila: Pila = Pila()
#      for caracteres in s:
#           pila.put(caracteres)
#      parentesis_cerrados: int = 0
#      parentesis_abiertos: int = 0
#      while not pila.empty():
#           actual = pila.get()
#           if actual == '(':
#             parentesis_abiertos += 1
#           elif actual == ')':
#             parentesis_cerrados += 1
#      if parentesis_cerrados == parentesis_abiertos:
#           return True
#      else:
#           return False

# def expresiones_aritmeticas_post_parentesis(s: str) -> bool:
#      pila: Pila = Pila()
#      lista_arit: list = ['+','-', '*', '/']
#      lista_no_deseados: list = [')', '(', '+', '-', '*', '/']
#      lista_no_deseados1: list = [')']
#      lista_no_deseados2: list = ['(', '+', '-', '*', '/']
#      booleano: bool = True
#      for caracteres in s:
#           pila.put(caracteres)
#      i: int = 0
#      while i < len(s)-1:
#           actual = pila.get()
#           siguiente = pila.get()
#           if actual == '(' and siguiente in lista_no_deseados1:
#                booleano = False
#           elif actual == ')' and siguiente in lista_no_deseados2:
#                booleano = False
#           elif actual in lista_arit and siguiente in lista_no_deseados:
#                booleano = False
#           i += 2
#      return booleano


# def esta_bien_balanceada(e:str) -> bool:
#      s: str = sacar_espacios_blancos(e)
#      if not chequeo_misma_cantidad_parentesis(s):
#           return False
#      elif not expresiones_aritmeticas_post_parentesis(s):
#           return False
#      else:
#           return True
     
           
# print(esta_bien_balanceada("1 + ) 2 x 3 ( ( )"))
# print(esta_bien_balanceada("10 * ( 1 + ( 2 * ( =1)))"))

# def evaluar_expresion(s: str) -> float:
#      lista_arit: list = ['+', '-', '*', '/']
#      pila_numeros: Pila = Pila()
#      for i in s:
#           if i not in lista_arit and i != ' ':
#                pila_numeros.put(i)
#           elif i in lista_arit:
#                 numero1: float = float(pila_numeros.get())
#                 numero2: float = float(pila_numeros.get())
#                 if i == '+':
#                     pila_numeros.put(numero2 + numero1)  
#                 elif i == '-':
#                     pila_numeros.put(numero2 - numero1)  
#                 elif i == '*':
#                     pila_numeros.put(numero2 * numero1)    
#                 elif i == '/':
#                     pila_numeros.put(numero2 / numero1)    
#      return pila_numeros.get()

# expresion = "3 4 + 5 * 2 -"
# resultado = evaluar_expresion(expresion)
# print(resultado) # Deber´ıa devolver 33


     

# c=Cola()
# c.put(("Mario",65,False,False))
# c.put(("Jorge",25,True,False))
# c.put(("Marta",26,True,True))
# c.put(("Pedro",29,False,True))
# c.put(("Pepe",45,False,False))
# c.put(("Pepa",45,True,False))


# def imprimir_cola(c:Cola) ->None:
#      while not c.empty():
#           print (c.get())

# #imprimir_cola(c)

# def atencion_clientes(c: Cola[(str,int,bool,bool)]) -> Cola[(str,int,bool,bool)]:
#      lista_pacientes:list = []
#      while not c.empty():
#           lista_pacientes.append(c.get())
#      lista_prioridad: list = []
#      lista_preferencial: list = []
#      lista_nada: list = []
#      for paciente in lista_pacientes:
#           if paciente[2] == True:
#                lista_prioridad.append(paciente)
#           elif paciente[3] == True:
#                lista_preferencial.append(paciente)
#           else:
#                lista_nada.append(paciente)
#      cola_final: Cola= Cola()
#      for prioritario in lista_prioridad:
#           cola_final.put(prioritario)
#      for preferido in lista_preferencial:
#           cola_final.put(preferido)
#      for nadie in lista_nada:
#           cola_final.put(nadie)
#      return cola_final

# imprimir_cola(atencion_clientes(c))


     
# #DICCIONARIOS
# def lista_de_palabras(lineas:str) -> list:
#      lista:list = []
#      temp:str= ""
#      for linea in lineas:
#           i:int = 0
#           while i < len(linea):
#                if linea[i] != "\n" and linea[i] != " ":
#                     temp += linea[i]
#                else:
#                     if len(linea[i]) > 0:
#                         lista.append(temp)
#                         temp = ""
#                i += 1
#      #lista.append(temp)
#      return lista

# print('\n',lista_de_palabras("hola mundo"))

# """def agrupar_por_longitud(archiv:str) -> dict:
#      archivo = open('ejemplo', 'r')
#      lineas = archivo.readlines()
#      dicc:dict= {}
#      palabras:list[str] = lista_de_palabras(lineas)
#      print(palabras)
#      for palabra in palabras:
#           if len(palabra) in dicc:
#                dicc[len(palabra)] += 1
#           else:
#                dicc[len(palabra)] = 1 
#      return dicc
# archiv = 'ejemplo'
# print(agrupar_por_longitud('ejemplo'))

# def la_palabra_mas_frecuente() -> str:
#      archivo = open('ejemplo', 'r')
#      lineas = archivo.readlines()
#      dic: dict= {}
#      palabras:list[str] = lista_de_palabras(lineas)
#      for palabra in palabras:
#         if palabra in dic:
#             dic[palabra] += 1
#         else:
#             dic[palabra] = 1
#      max_p:str = ""
#      max_v:int= 0
#      for k,v in dic.items():
#           if v > max_v:
#                max_v = v
#                max_p = k
#      return max_p


# print(la_palabra_mas_frecuente())"""

# def separar_por_comas(lista: list) -> list[str]:
#      temp: str = ""
#      lista_separada: list = []
#      for linea in lista:
#           i = 0 
#           while i < len(linea):
#             if linea[i] == ',':
#                lista_separada.append(temp)
#                temp = ""
#                i += 1
#             else: 
#                temp += linea[i]
#                i += 1  
#      lista_separada.append(temp)
#      return lista_separada

#print(separar_por_comas("hola,como,estas"))

def funcion_datos_utiles(lista:list[str]) -> list[str]:
     i: int = 0
     lista_util: list = []
     while i < len(lista):
          lista_util.append(lista[i])
          lista_util.append(lista[i+3])
          i += 4
     return lista_util

def promedio(notas:list[float]) -> float:
     total:float = 0
     for nota in notas:
        nota = float(nota)
        total += nota
     promedio_final: float= total / len(notas)
     promedio_final_final: float = round(promedio_final,2)
     return promedio_final_final

#print(promedio(['10', '7.4', '5']))
     
# def calcular_promedio(diccionario_notas:dict) -> dict:
#      for estudiante, lista_notas in diccionario_notas.items():
#           diccionario_notas[estudiante] = promedio(lista_notas) 
#      return diccionario_notas

# def calcular_promedio_estudiante(archivo_notas: str) -> dict:
#      archivo_notas: str = open('archivo_de_notas1.txt', 'r')
#      lineas = archivo_notas.readlines()
#      lista_de_datos:list = separar_por_comas(lineas)
#      datos_utiles:list = funcion_datos_utiles(lista_de_datos)
#      diccionario_de_notas: dict = {}
#      i: int = 0
#      while i < len(datos_utiles):
#           if datos_utiles[i] not in diccionario_de_notas:
#                diccionario_de_notas[datos_utiles[i]]= []
#           diccionario_de_notas[datos_utiles[i]].append(datos_utiles[i+1])
#           i += 2
#      promedio_final = calcular_promedio(diccionario_de_notas)
#      return promedio_final

# print(calcular_promedio_estudiante('archivo_de_notas1.txt'))



sitios= Pila()
sitios.put("google")
sitios.put("youtube")
sitios.put("lanacion")




inventario : dict = {}
"""inventario_aux : dict = {}
precio : float = 0.0
cantidad: int = 0
inventario_aux[precio] = cantidad
producto: str = ""
inventario[producto] = inventario_aux

print (inventario)"""

def agregar_producto(inventario: dict, nombre: str, precio: float, cantidad: int) -> dict:
     inventario_aux: dict = {}
     inventario_aux["precio"] = precio
     inventario_aux["cantidad"] = cantidad
     inventario[nombre] = inventario_aux
     return inventario

print(agregar_producto(inventario,"camisa", 20.0, 50))

def actualizar_stock(inventario: dict, nombre: str, cantidad: int) -> dict:
     inventario_aux = inventario[nombre]
     inventario_aux["cantidad"] = cantidad
     return inventario

print(actualizar_stock(inventario, "camisa", 10))

def actualizar_precios(inventario: dict, nombre: str,precio: float) -> dict:
     inventario_aux = inventario[nombre]
     inventario_aux["precio"] = precio
     return inventario

print(actualizar_precios(inventario, "camisa", 100.0))

def calcular_valor_inventario(inventario : dict) -> float:
     valor_total: float = 0
     for productos, dicc in inventario.items():
          valor_total += dicc["precio"] * dicc["cantidad"]
     return valor_total


agregar_producto(inventario, "Camisa", 20.0, 50)
agregar_producto(inventario, "Pantalon", 30.0, 30)
actualizar_stock(inventario, "Camisa", 10)
print(inventario)
valor_total = calcular_valor_inventario(inventario)
print("Valor total del inventario:", valor_total)




def visitar_sitio(historiales: dict[str, Pila[str]],usuario: str,sitio: str) -> dict:
     if usuario in historiales:
          historiales[usuario].put(sitio)
     else:
        sitios: Pila = Pila()
        sitios.put(sitio)
        historiales[usuario] = sitios
     return historiales

def navegar_atras(historiales: dict[str, Pila[str]], usuario:str) -> dict:
     sitio_actual: str = historiales[usuario].get()
     sitio_anterior: str = historiales[usuario].get()

     #lo damos vuelta
     historiales[usuario].put(sitio_actual)
     historiales[usuario].put(sitio_anterior)
     
     print(historiales[usuario].queue, "Soy el historial del usuario")
     return historiales

historiales = {}
visitar_sitio(historiales, "Usuario1", "google.com")
visitar_sitio(historiales, "Usuario1", "facebook.com")
navegar_atras(historiales, "Usuario1")
# visitar_sitio(historiales, "Usuario2", "youtube.com")
# visitar_sitio(historiales, "jorge", "github")
# #print(historiales)
# visitar_sitio(historiales, "juan", "github")
# #print (historiales)
# navegar_atras(historiales, "jorge")


#ejercicio 6 archivo binario

#buscamos palabras legibles >= 5, numeros, mayus,minusculas y caracteres espacio " " y -

#palabra legible = 11111, 1-3   , holAA, 1-- u, "-----"
# #, /, \, {,},(,)

#vamos recorriendo el archivo, vamos armando palabras

def listar_palabras(archivo: str) -> list[str]:
     palabras = []
     #prohibidas = [#, /, \, {,},(,)]

     with open(archivo, "br") as file:
     #file = open(archivo, "b")
          palabra = ""
          print("abri el archivo")
          secuencia = file.read()
          for byte in secuencia:
               caracter = chr(byte)
               if caracter not in prohibidas:
                    palabra+= caracter
               else:
                    if len(palabra) >= 5:
                         listar_palabras.append(palabra)
                    palabra = ""

          #caso ultima palabra
                    
          #habria que usar un archivo .mp3 posta
          #agarramos char a char(convertimos los bytes
     return palabras

listar_palabras(r'/home/cami/Desktop/consultas/archivo_prueba.mp3')
prueba = open("prueba", "w")
