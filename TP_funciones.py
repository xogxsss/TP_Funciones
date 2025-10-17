#1. Crear una función que imprima el mensaje "Hola mundo"
def imprimir_hola_mundo ():
    print("¡Hola mundo!")

imprimir_hola_mundo()

#2. Crear una función para generar un saludo personalizado
def saludar_usuario (nombre):
    print(f"¡Hola, {nombre}!")

nombre = input('¿Cómo te llamas?')
saludar_usuario(nombre)

#3. Crear una función que reciba 4 parámetros e imprima un mensaje por pantalla
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
edad = int(input('Ingrese su edad: '))
residencia = input('Ingrese su lugar de residencia: ')

informacion_personal(nombre, apellido, edad, residencia)


#4. Crear dos funciones que calculen el área y perímetro de un círculo, recibiendo el radio como parámetro
# A = PI.r^2
# P = 2.PI.r
from math import pi

def calcular_area_circulo(radio):
    area = pi*(radio**2)
    return round(area, 2)

def calcular_perimetro_circulo(radio):
    perimetro = 2*pi*radio
    return round(perimetro, 2)

radio = float(input('Ingrese el radio de su circunferencia: '))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f'Área: {area}\nPerímetro: {perimetro}')

#5. Crear una función para convertir segundos a horas
#1 hora = 3600 segundos
def segundos_a_horas(segundos):
    horas = (segundos/3600)
    return round(horas, 2)

segundos = int(input('Ingrese la cantidad de segundos: '))
horas = segundos_a_horas(segundos)

print(f"{segundos}s = {horas}h")

#6. Crear una función para mostrar la tabla de multiplicación del 1 al 10 de x número
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {(numero*i)}")

numero = int(input('Ingrese un número: '))
print(f"Tabla de multiplicar de {numero}")
tabla_multiplicar(numero)

#7. Crear una función que devuelva una tubla con el resultado de operaciones básicas entre dos números

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    división = a / b
    tupla = (suma, resta, multiplicacion, división)
    return tupla

num1 = int(input('Ingrese el primer número: '))
num2 = int(input('Ingrese el segundo número: '))

resultado= operaciones_basicas(num1, num2)

print(f"Suma: {resultado[0]}\nResta: {resultado[1]}\nMultiplicación: {resultado[2]}\nDivisión: {resultado[3]}")

#8. Crear una función que calcule el IMC; parámetros: altura (m) y peso (kg). Mostrar el resultado con dos decimales
#IMC = peso / (altura**2)
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input('Ingrese su peso, en kilogramos: '))
altura = float(input('Ingrese su altura, en metros: '))

resultado = calcular_imc(peso, altura)

print(f"IMC: {resultado:.2f}")

#9. Crear una función para convertir celsius a fahrenheit
#fahrenheit = (celsius * 9/5) + 32

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input('Ingrese su temperatura, en grados Celsius: '))
resultado = celsius_a_fahrenheit(celsius)

print(f"{celsius:.2f}°C = {resultado:.2f}°F")

#10. Crear una función apra calcular el promedio de tres parámetros
from statistics import mean

def calcular_promedio(a, b, c):
    lista = [a, b, c]
    resultado = mean(lista)
    return resultado

num1 = float(input('Ingrese el primer número: '))
num2 = float(input('Ingrese el segundo número: '))
num3 = float(input('Ingrese el tercer número: '))

resultado = calcular_promedio(num1, num2, num3)

print(f"Promedio: {resultado:.2f}")