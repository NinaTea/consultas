# Consultas

## En general

Para acceder a un diccionario siempre es:

nombre_del_diccionario[clave] <- Eso te devuelve el valor asociado a la clave.

Por ejemplo

mi_diccionario = {"a": 1, "b": 2}
print(mi_diccionario["a"]) # Imprime 1


## Trabajando con punteros

Cuando usamos pilas y colas y tenemos que preservar sus valores, por lo general creamos un nuevo objeto que luego vamos llenando y al final reasignamos ese objeto a la variable(pila o cola) que entró.

Hay que recordar que las variables creadas dentro de la función sólo existen dentro del contexto de esa función. Dejo caso preguntado por una alumna.

Al intentar restaurar la cola porque es de tipo int, no se restaura y sigue quedando vacía, envío un ejemplo de como lo planteo:
```python

def crear_listac (c:Cola) -> list:
    q = Cola()
    lista: list = []
    while not(c.empty()):
        x = c.get()
        lista.append(x)
        q.put(x)
    c = q
    return lista

```

Al intentar probar con una cola que sea c = [1,2,3,4,5], veo que luego de aplicar la funcion, c = [].
Qué sería lo que está mal aplicado? o qué forma debería utilizar?

La respuesta fue dada por el profe Javier Godoy. Créditos a él.

El problema es que cuando haces, en la última línea, "c = q" la variable local "c" cambia la refencia a la que apunta. Entonces si ves los elementos de c después de esa linea, vas a ver que tiene los elementos originales. Sin embargo, cuando salis de la función, la cola que habías pasado sigue vacía. Dejo comentarios por si ayuda:
    
```python
def crear_listac (c:Cola[int]) -> list[int]:
    #acá la variable "c" es una referencia a "cola"
    q: Cola[int] = Cola()
    lista: list[int] = []
    while not(c.empty()):
        x = c.get() #acá estas modificando "cola"
        lista.append(x)
        q.put(x)
    #acá "cola" está vacía, y como "c" apunta a "cola", "c" es vacía tmb
    c = q # Acá "c" ya no apunta a "cola", sino a "q". "cola" sigue vacía.
    return lista

cola: Cola[int] = Cola()
cola.put(1)
cola.put(5)
# acá cola tiene los elementos 1 y 5
crear_listac(cola)
# acá cola está vacía
```
 
Entonces lo que tenes que hacer es un 2do ciclo, en donde volvés a agregar uno por uno los elementos de "q" a "c". Como "c" apunta a "cola", cuando salgas de la función cola va a seguir teniendo los valores que tenía originalmente.

