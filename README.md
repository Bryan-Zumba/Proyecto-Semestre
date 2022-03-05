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
suma_valores = 1 + 2
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

#Su print se verá así:
print ("El resultado de la suma es:", suma)       # El resultado de la suma es: 11
```
### Resta

La realizaremos de la misma manera que en la suma, solo que esta vez utilizaremos el signo correspondiente a la operación. 
```python
#Definimos variables para nuestros valores numéricos 
a = 5
b = 6

#Definimos una variable para la operación que realizaremos, en este caso la resta:
resta = a - b

#Su print se verá así:
print ("El resultado de la resta es:", resta)        #El resultado de la resta es: -1
```
### Multiplicación

Para esta operación, utilizaremos su signo correspondiente ( * )
```python
#Definimos variables para nuestros valores numéricos 
a = 10
b = 5

#Definimos una variable para la operación que realizaremos, en este caso la multiplicación:
multiplicación = a * b

#Su print se verá así:
print ("El resultado de la multiplicación es:", multiplicación) 	   #El resultado de la multiplicación es: 50
```
### División

En el caso de la división, será el mismo proceso de la multiplicación, con la diferencia que se realizará con su signo correspondiente.
```python
#Definimos variables para nuestros valores numéricos 
a = 10
b = 5

#Definimos una variable para la operación que realizaremos, en este caso la división:
división = a / b

#Su print se verá así:
print ("El resultado de la división es:", división)              #El resultado de la división es: 2
```
### Módulo

```python
#Definimos variables para nuestros valores numéricos 
a = 10
b = 5

#Definimos una variable para la operación:
módulo = a % b

#Su print se verá así:
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
A los valores que representan texto se les llama strings, y tienen el tipo str. Las cadenas (o strings) son un tipo de datos compuestos por secuencias de caracteres que representan texto. Estas cadenas se delimitan mediante el uso de comillas simples o dobles. Por ejemplo:
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
Las listas en Python son un tipo de dato que permite almacenar datos de cualquier tipo. Son mutables y dinámicas, lo cual es la principal diferencia con los sets y las tuplas, una lista sea crea con [  ] separando sus elementos con comas " , ". A continuación, un ejemplo:
```python
lista = [10, "Bryan", 3.67, [1, 6, 9]]
print(lista)                              #[10, 'Bryan', 3.67, [1, 2, 3]]
#O también puede crearse una lista de la siguiente manera:
lista = list("123456789b")                
print(lista)                              #['1', '2', '3', '4', '5', '6', '7', '8', '9', 'b']
```
## Tuple
Son un tipo o estructura de datos que permite almacenar datos de una manera muy parecida a las listas, con la salvedad de que son inmutables, lo que significa que no pueden ser modificadas una vez declaradas, y en vez de inicializarse con corchetes se hace con ( ). Dependiendo de lo que queramos hacer, las tuplas pueden ser más rápidas. A continuación, un ejemplo:
```python
tupla = (0, 100, 200)
print(tupla)                     #(0, 100, 200)
#También puede escribirse sin paréntesis (  ), separando con respectivas comas " , ".
tupla = 0, 100, 200
print(tupla)                     #(0, 100, 200)
```
## Dictionary
Los diccionarios son poderosas estructuras de datos en Python que almacenan datos como pares de claves, siendo está representada en la siguiente forma: Clave-Valor. La comprensión de diccionarios (o dict comprehension) puede ser muy útil en crear nuevos diccionarios basados en diccionarios existentes e iterables.

*Todos los elementos en el diccionario se encuentran encerrados en un par de corchetes { }.*

*Cada elemento en un diccionario contiene una clave y un valor - es decir un par de clave-valor.*

*Cada par de clave-valor es denominado como elemento (item).*

*La ventaja de esto es que puedes acceder a todos los valores almacenados usando simplemente las claves.*
```python
#Ejemplo
diccionario = {  
  "total": 55,
  "subtotal":50
}
#Y con el print se vería de la siguiente manera:
print("Diccionario =",diccionario)            #Diccionario = {'total': 55, 'subtotal': 50}
```
# Tomando decisiones
## Sentencia if
La estructura de control "if" permite que un programa ejecute unas instrucciones cuando se cumplan una condición. La estructura de control if, else, permite que un programa ejecute unas instrucciones cuando se cumple una condición y otras instrucciones cuando no se cumple esa condición. En inglés "if" significa "si" (condición) y "else" significa "si no".
Por ejemplo:
```python
#Calcular el mayor de dos números enteros introducidos por el teclado
#Entrada
num1= int(input('Ingreso num 1:'))
num2= int(input('Ingreso num 2:'))

#Proceso
if num1 > num2:
    #Salida
    print('El numero mayor es:',num1)
elif num2> num1:
    #Salida
    print('El numero mayor es:',num2)
else:
    #Salida
    print('Los números son iguales')
```
## Ciclo For
El bucle for se utiliza para recorrer los elementos de un objeto iterable (lista, tupla, conjunto, diccionario, …) y ejecutar un bloque de código. En cada paso de la iteración se tiene en cuenta a un único elemento del objeto iterable, sobre el cuál se pueden aplicar una serie de operaciones.
Por ejemplo:
```python
nums = [4, 78, 9, 84]
for n in nums:
    print(n)
#Su print se verá así:
#4
#78
#9
#84
```
## Ciclo While
El uso del while nos permite ejecutar una sección de código repetidas veces, de ahí su nombre. El código se ejecutará mientras una condición determinada se cumpla. Cuando se deje de cumplir, se saldrá del bucle y se continuará la ejecución normal.
Por ejemplo:
```python
#Cuando se deje de cumplir la orden, se saldrá del bucle
x = 0
while x < 5:
    x +=1
    print(x)
#Su print se verá así:
#1
#2
#3
#4
#5
```
## Break
La sentencia break permite terminar con la ejecución del bucle. Esto significa que una vez se encuentra la palabra break, el bucle se habrá terminado.
Por ejemplo:
```python
#Cuando se encuentre con el número 3, el programa terminará
x = 0
while x < 5:
    x +=1
    if x==3:
        print("Se encontró el 3")
        break
    print(x)
#Su print se verá así:
# 1
# 2
# Se encontró el 3
```
## Continue
El continue se salta todo el código restante en la iteración actual y vuelve al principio en el caso de que aún queden iteraciones por completar. La diferencia entre el break y continue es que el continue no rompe el bucle, si no que pasa a la siguiente iteración saltando el código pendiente.
Por ejemplo:
```python
#Cuando se encuentre con el número 3, se saltará y continuará con los demás print
x = 0
while x < 5:
    x +=1
    if x==3:
        continue
    print(x)
#Su print se verá así:
# 1
# 2
# 4
# 5
```
