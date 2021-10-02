# generador de contraseñas aleatorias

import random

def generar_contrasena():
    mayusculas = ['A','B','C','D','E','F','G']
    minusculas = ['a','b','c','d','e','f','g']
    simbolos = ['!','#','$','&','/','(',')']
    numeros = ['1','2','3','4','5','6','7','8','9','0']
     
    # unir listas  
    caracteres = mayusculas + minusculas + simbolos + numeros

    contrasena = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)
        
    # convertir la lista en un string 
    contrasena = "".join(contrasena)
    return contrasena 


def run():
    contrasena = generar_contrasena()
    print('Tu nueva contraseña es: ' + contrasena)
