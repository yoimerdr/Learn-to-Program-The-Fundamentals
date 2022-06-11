# Documentación Básica Para Programar en Python

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