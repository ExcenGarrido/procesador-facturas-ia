"""numeros = [1,2,3,4,5]
cuadrados = [numero ** 3 for numero in numeros]
print(cuadrados)  # [1, 4, 9, 16, 25] """

"""
numeros = [1, 2, 3, 4, 5]
mayores = [numero for numero in numeros if numero >= 3]
print(mayores)  # [4, 5]
"""

"""
nombres = ["ana", "juan", "pedro"]
en_mayusculas = [nombre.upper() for nombre in nombres]
print(en_mayusculas)  # ['ANA', 'JUAN', 'PEDRO']
"""
"""
nombres = ["ana", "juan", "pedro"]
largos = [nombre for nombre in nombres if len(nombre) > 3]
print(largos)  # ['juan', 'pedro']
"""


"""
Ejercicio a
edades = [12, 25, 8, 40, 17, 33, 5]

edades_mayores = [edad for edad in edades if edad >18]
print(edades_mayores)
"""
"""
Ejercicio b
precios = [100, 250, 80, 1500, 30]
precio_21 = [precio * 1.21 for precio in precios]
print(precio_21)
"""



"""
Ejercicio c
numeros = [3, 7, 10, 15, 22, 30]
mayores_10 = [numero *2 for numero in numeros if numero >10]
print(mayores_10)

"""

"""
Ejercicio d
palabras = ["sol", "luna", "estrella", "mar"]
palabra_longitud = [(palabra, len(palabra)) for palabra in palabras]
print(palabra_longitud)

"""