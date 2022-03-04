# Proyecto-Semestre 
# ¿Qué es Python? 💫

Python es un lenguaje de programación de alto nivel, orientado a objetos, con una semántica dinámica integrada, principalmente para el desarrollo web y de aplicaciones informáticas. Se trata de un lenguaje interpretado, lo que significa que el código escrito no se traduce realmente a un formato legible por el ordenador en tiempo de ejecución.

# ¿Qué es una variable?

Una variable es un nombre para representar un valor de un dato, por ejemplo, si tenemos un programa que suma dos números, necesitamos un nombre para identificar el valor1 y el valor2 (mira, esto mismo nos serviría como variables, valor1 y valor2 podrían ser el nombre de nuestras variables)

## Nombrando una variable

Para poder nombrar una variable correctamente, tenemos que tomar en cuenta las siguientes reglas al definir una variable, y no tener problemas con el compilador:

Una variable siempre debe iniciar con una letra minúscula o un guion bajo ( _ ), solamente puede contener números después de  la primer letra (siguiendo la regla anterior).
No es permitido dejar un espacio en blanco a lo largo de la variable (en el caso de tener que separar palabras, utilizaremos el guion bajo " _ ". A lo largo de tu programa, la variable debe escribirse exactamente igual, utiliza un nombre que exprese algo del contexto en el cual la estás declarando.

Una manera correcta de nombrar una variable se vería así:
```python
suma_valores =
```
## Asignando valores a una variable

Para asignar un valor (un dato) a una variable se utiliza el operador de asignación "=".

En la operación de asignación se ven involucradas tres partes:

1.-El operador de asignación "="

2.-Un identificador o nombre de variable, a la izquierda del operador

3.-Un literal, una expresión, una llamada a una función o una combinación de todos ellos a la derecha del operador de asignación

Por ejemplo:
```python
#Asignamos una variable al resultado de la suma entre 1 y 2
suma_valores = 1+2
```
## Operadores básicos

Dentro de los operadores básicos tenemos los siguientes, con sus respectivos símbolos:
```python
suma: (+)
resta: (-)
multiplicación: (*)
división: (/)
división entera: (//)
módulo: (%)
potenciación: (**)
```
### Suma

Para poder efectuar una suma:
```python
#Definimos variables para nuestros valores numéricos 
a = 5
b = 6

#Definimos una variable para la operación que realizaremos, en este caso la suma:
suma = a + b

#Esta operacio0n se ejecutará, e imprimiremos su resultado de una manera presentable:
print ("El resultado de la suma es:", suma)        # El resultado de la suma es: 11
```
### Resta

La realizaremos de la misma manera que en la suma, solo que esta vez utilizaremos el signo correspondiente a la operación. 
```python
#Definimos variables para nuestros valores numéricos 
a = 5
b = 6

#Definimos una variable para la operación que realizaremos, en este caso la suma:
resta = a-b

#Esta operacio0n se ejecutará, e imprimiremos su resultado de una manera presentable:
print ("El resultado de la resta es:", resta)        #El resultado de la resta es: -1
```
### Multiplicación

Para esta operación, utilizaremos su signo correspondiente (*)
```python
#Definimos variables para nuestros valores numéricos 
a = 10
b = 5

#Definimos una variable para la operación que realizaremos, en este caso la suma:
multiplicación = a*b

#Esta operacio0n se ejecutará, e imprimiremos su resultado de una manera presentable:
print ("El resultado de la multiplicación es:", multiplicación)    #El resultado de la multiplicación es: 50
```
### División

En el caso de la división, será el mismo proceso, con la diferencia que se realizará con su signo correspondiente.
```python
#Definimos variables para nuestros valores numéricos 
a = 10
b = 5

#Definimos una variable para la operación que realizaremos, en este caso la suma:
división = a/b

#Esta operacio0n se ejecutará, e imprimiremos su resultado de una manera presentable:
print ("El resultado de la división es:", división)              #El resultado de la división es: 2
```
### Módulo

```python
#Definimos variables para nuestros valores numéricos 
a = 10
b = 5

#Definimos una variable para la operación que realizaremos, en este caso la suma:
módulo = a % b

#Esta operacio0n se ejecutará, e imprimiremos su resultado de una manera presentable:
print ("Su módulo será:", módulo)                #Su módulo será: 0
```
# Tipos de datos en Python

## Integer
El tipo int (del inglés integer, que significa «entero») permite representar números enteros.

Los valores que puede tomar un int son todos los números enteros:
``` ... -3, -2, -1, 0, 1, 2, 3, ... ```

## Float
Sirve para poder interpretar y representar los números decimales, por ejemplo: 
```
1.25
0.14
-5.68
```
## String
A los valores que representan texto se les llama strings, y tienen el tipo str. Las cadenas (o strings) son un tipo de datos compuestos por secuencias de caracteres que representan texto. Estas cadenas de texto son de tipo str y se delimitan mediante el uso de comillas simples o dobles. Por ejemplo:
```python 
a="Hello world"
print(a)
```
## Casting en Python
Hacer un cast o casting significa convertir un tipo de dato a otro, tipos de datos como los int, string o float.
```python
#Como podemos ver tenemos dos variables, la primera tipo int y la segunda en float
a= 6
b= 1.5
suma= a + b
#Añadiendole el int a la operación, esta nos convertirá el valor y nos devolverá un número entero
print ("El resultado es:",int(suma))             #El resultado es: 7
```
## List
Las listas en Python son un tipo de dato que permite almacenar datos de cualquier tipo. Son mutables y dinámicas, lo cual es la principal diferencia con los sets y las tuplas, una lista sea crea con [] separando sus elementos con comas " , ". A continuación un ejemplo:
```python
lista = [10, "Bryan", 3.67, [1, 6, 9]]
print(lista)                              #[10, 'Bryan', 3.67, [1, 2, 3]]
#O también puede crearse una lista de la siguiente manera:
lista = list("123456789b")                
print(lista)                              #['1', '2', '3', '4', '5', '6', '7', '8', '9', 'b']
```
## Tuple
Son un tipo o estructura de datos que permite almacenar datos de una manera muy parecida a las listas, con la salvedad de que son inmutables, lo que significa que no pueden ser modificadas una vez declaradas, y en vez de inicializarse con corchetes se hace con (). Dependiendo de lo que queramos hacer, las tuplas pueden ser más rápidas. A continuación un ejemplo:
```python
tupla = (0, 100, 200)
print(tupla)                     #(0, 100, 200)
#También puede escribirse sin parentésis ( ), separando con respectivas comas " , ".
tupla = 0, 100, 200
print(tupla)                     #(0, 100, 200)
```
## Dictionary

# Tomando decisiones

## Sentencia if

## Ciclo For

## Ciclo While

## Break

## Continue
