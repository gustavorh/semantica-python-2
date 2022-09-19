# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 20:02:20 2021

Nombre: Gustavo Reyes Herrera
RUT: oculto

Mis respuestas en este trabajo son propias, y están realizadas
en conformidad con la formación ética de la universidad.

"""

# La variable 'n' determinará la cantidad de términos a calcular (o exactitud de Pi)
n = int(input("Ingrese la cantidad de terminos a calcular: "))
denominador = 1  # Inicializamos la variable 'denominador' con valor int 1
signo = 1  # Inicializamos la variable 'signo' con valor int 1, esta variable será la que irá alternando entre positivo y negativo en la suma de términos
suma = 0  # Inicializamos la variable 'suma' con valor int 0, esta variable será usada para almacenar la suma de los términos

for i in range(1, n+1):  # Contador que calculará la cantidad de términos dados por 'n'
    terminos = 1 / denominador * signo  # 1/1 - 1/3 + 1/5 - 1/7 ...
    suma += terminos  # Asignamos la suma anterior a la variable 'suma'
    denominador += 2  # Incrementamos el denominador de 2 en 2
    signo *= -1  # Alternamos entre positivo y negativo al multiplicar por -1
pi = suma * 4  # Luego de calcular la suma de términos, multiplicamos por 4

# Entregamos el resultado final
print(f'El valor de Pi con {n} términos usados para la suma es: {pi}')
