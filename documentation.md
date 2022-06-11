# Documentación Básica Para Programar en Python

## Indice de contenidos
* [Operaciones Básicas](#operaciones-básicas)
* [Funciones](#funciones)
* [Bools](#bools)
* [Importar Módulos](#importar-módulos)
* [Condicionales](#condicionales)
* [Ciclos](#ciclos)
* [Input y Output](#input-y-output)
* [Comentarios](#comentarios)
* [Funciones help y dir](#funciones-help-y-dir)
* [Strings](#strings)
* [Listas](#listas)
* [Rangos](#rangos)
* [Archivos](#archivos)
* [Tuplas](#tuplas)
* [Diccionarios](#diccionarios)
## Operaciones Básicas

Para programar en python, como en cualquier otro lenguaje de programación
existen ciertos símbolos para las operaciones básicas con números enteros y flotantes. 

| Símbolo | Operación        |  
|---------|------------------|
| `+`     | Suma             | 
| `-`     | Resta            |
| `*`     | Multiplicación   |
| `**`    | Potencia         |
| `/`     | División         |
| `//`    | División Entera  |
| `%`     | Módulo o Residuo |

## Funciones

La definición de funciones en Python tiene la siguiente estructura
```
def nombre_funcion(parametros):
    '''
    Descripción de la función
    Tambien conocido como docstring, aquí puedes poner los tipos de datos de los parametros que la función
    pide, así como el tipo de dato que la función retorna. Además, también puedes describir brevemente lo 
    que la función hace.
    '''
    #cuerpo de la functión
```

## Bools

Para las operaciones con valores booleanos, se utilizan los siguientes operadores.  

| Operador | Operación                           |
|----------|-------------------------------------|
| `<`      | Menor que                           |
| `>`      | Mayor que                           |
| `==`     | Igual a                             |
| `>=`     | Mayor o igual a                     |
| `<=`     | Menor o igual a                     |
| `!=`     | Diferente a                         |
| `not`    | Negación                            |
| `and`    | Y, `&&` de c++ o java               |
| `or`     | O, &verbar;&verbar; de c++ o java   |

## Importar Módulos

Para importar módulos en Python se utilizan las siguientes declaraciones.

| Declaración                                | Usar Funciones                                                       |
|--------------------------------------------|----------------------------------------------------------------------|
| `import nombre_modulo`                     | `nombre_modulo.nombre_funcion` Se puede llamar a todas las funciones |
| `from nombre_modulo import nombre_funcion` | `nombre_funcion` Solo se puede llamar a `nombre_funcion`             |
| `from nombre_modulo import *`              | `nombre_funcion`  Se puede llamar a todas las funciones              |


## Condicionales

Para usar declaraciones condicionales se usa, generalmente, la siguiente estructura.
```
if expresión_condicional:
    #cuerpo del if
elif expresión_condicional:  #Puede existir 0 o más claúsulas elif. Solo puede existir con la declaración if
    #cuerpo del elif
else:  #Puede existir 0 o 1 claúsula else. Solo puede existir si hay una declaración if
    #cuerpo del else
```

## Ciclos

Para usar ciclos repetitivos tenemos las siguientes estructuras.
```
for varibe_name in objecto_iterable: varibe_name toma todos los valos dentro de objecto_iterable
    #Cuerpo del for

while expresión_condicional:
    #Cuerpo del while
```

## Input y Output

Para el control de entrada y salida de datos, podemos usar las siguientes funciones
```
print(arguments) #Para imprimir datos en consola
input(arguments) #Para captar datos desde consol

```

## Comentarios

Para realizar comentarios en Python podemos utilizar las siguientes declaraciones.
```
'''
Comentario de
muchas lineas.
'''
#Comentario de una sola liena
```

## Funciones help y dir

En Python existen funciones para obtener información de módulos, clases o funciones.
```
help(objecto) #retorna la descripción de objeto
dir(objeto) #retorna todos los valores de las funciones que tiene objeto
```

## Strings

Los strings o cadena de texto en python, son valores que están entre `''` o `""`   
Para las operaciones con strings:

| Símbolo        | Operación         |
|----------------|-------------------|
| `+`            | concatenación     |
| `*`            | Repetición        |
| `==`           | Igual a           |
| `!=`           | Diferente a       |
| `<`            | Menor que         |
| `>`            | Mayor que         |
| `>=`           | Mayor o igual que |
| `<=`           | Menor o igual que |
| `in`           | Está en           |
| `len(string)`  | Tamaño del string |

Para indexación con strings en python:
```
string[index] #index >= 0 < len(string). Retorna el caracter en la posicion dada.
string[index] #-len(string) <= index < 0. Retorna el caracter en la posicion dada en reversa.
string[n:m] #Retorna un substring desde la posición n hasta la posición m.
string[n:] #Retorna un substring desde la posición n hasta el final del string.
string[:m] #Retorna un substring desde el principio del string hasta la posición m.
string[:] #Retorna el string completo.

```
String es una cadena de texto inmutable, por lo que no se puede modificar los elementos(caracteres) dentro de el.

## Listas

Clase para una collección de datos. Es de tipo mutable.  
Para definir una lista en python se utiliza la siguiente declaración `variable_name = [element1, element2... elementN]`.  
Y como cualquier objeto, una lista en python también tiene métodos. A continuación se listan algunos.

Métodos que modifican la lista:

| Método                   | Descripción                                                                   |
|--------------------------|-------------------------------------------------------------------------------|
| `.append(object)`        | Añade `object` al final de la lista                                           |
| `.extend(list)`          | Añade los elementos del parámetro `list` a la lista                           |
| `.pop(index)`            | Elimina y devuelve el elemento en `index` (por defecto el último) de la lista |
| `.remove(object)`        | Elimina la primera aparición de `object`; error si no existe                  |
| `.reverse()`             | Invierte la lista                                                             | 
| `.sort()`                | Ordena la lista de menor a mayor                                              |
| `.insert(index, object)` | Inserta `object` en el `index` dado                                           |

Métodos que no modifican la lista:

| Método                | Descripción                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| `list.count(object)`  | Devuelve el número de veces que `object` aparece en la lista                |
| `list.index(object)`  | Devuelve el índice de la primera aparición de `object`; error si no existe  |

Con listas en python se pueden usar los siguientes operadores:

| Operador    | Descripción                                                                            |
|-------------|----------------------------------------------------------------------------------------|
| `in`        | Si un valor está en la lista                                                           |
| `len(list)` | Tamaño de la lista                                                                     |
| `min(list)` | Devuelve el elemento mínimo de la lista                                                |
| `max(list)` | Devuelve el elemento máximo de la lista                                                |
| `sum(list)` | Devuelve la suma de todos los elementos de la lista, los elementos deben ser numéricos |

Puesto que list es un objeto iterable, las misma reglas de indexación de los string funcionan para las listas.

## Rangos
range, se utiliza para crear una secuencia númerica iterable. Se suele usar en bucles for: `for i in range(n):`  
Tiene la siguiente estructura:  
```
"""
range(start, end, step) Empieza en start, inclusivo, finaliza en end, exclusivo, y avanza segun el valor de step.
Así, la siguiente declaración:
    for i in range(1,6,2):
        for body
Crea una secuencia que va desde 1 hasta 4 y avanza de 2 en 2.
"""
```

## Archivos
En python para abrir un archivo, generalmente de texto plano, se utiliza la siguente función `open(filename, mode)`.  
```
"""
Donde:
filename #nombre del archivo(ruta completa)
'r' #abre el archivo en modo lectura
'w' #abre el archivo en modo escritura
'a' #abre el archivo en modo añadir, añade a lo que ya está en el archivo
"""
```

## Tuplas
Funciona como las listas, pero los valores de las tuplas son inmutables.
Para la declarar un tupla se usa la siguiente estructura: `tuple_name = (item1, item2...)`

## Diccionarios
En python, un diccionario es una colección de datos clave-valor. Para declarar un diccionario se sigue la siguiente sintaxis: `dictionary_name = { key1 : value1, key2 : value2... keyN : valueN }`  
Las keys dentro del diccionario deben ser únicas, los valores pueden ser duplicados.  

Operadores con diccionarios

| Operador           | Descripción                                   |
|--------------------|-----------------------------------------------|
| `in`               | Contiene                                      |
| `del`              | Elimina                                       |
| `len(dictionary)`  | Número de pares clave:valor en el diccionario |

Ejemplo de uso de operadores de los diccionarios:
```
dic = { "a1" : 2, "a2" : 3, "a3":4 } #declaración del diccionario
print("a1" in dic) #Imprime True, porque la llave "a1" existe en el diccionario
print(3 in dic) #Imprime False, porque la llave 3 no existe en el diccionario
print("pairs key:value in dic", len(dic), sep=', ') #Imprime "pairs key:value in dic, 3", porque hay 3 pares llave:valor en dic

del dic["a1"] #elimina el par "a1":2 de dic
print("pairs key:value in dic", len(dic), sep=', ') #Imprime "pairs key:value in dic, 2", porque ahora hay 2 pares llave:valor in dic, el par "a1":2 fue eliminado
```